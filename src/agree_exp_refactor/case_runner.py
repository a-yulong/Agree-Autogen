import os
import re
from typing import Dict, Any, Optional

from .runtime import format_file_link

def _collect_declared_component_names(aadl_model: str) -> list[str]:
    """
    收集模型中声明过的组件/实现名称，保留原大小写。
    """
    names: list[str] = []
    patterns = [
        r'^\s*(system|process|thread|device|abstract|subprogram)\s+implementation\s+([A-Za-z_][A-Za-z0-9_\.]*)',
        r'^\s*(system|process|thread|device|abstract|subprogram)\s+([A-Za-z_][A-Za-z0-9_\.]*)',
    ]
    for line in aadl_model.splitlines():
        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                names.append(match.group(2))
                break
    return list(dict.fromkeys(names))


def _normalize_component_name(name: str) -> str:
    return re.sub(r'[^A-Za-z0-9_]', '', name).lower()


def _resolve_component_name(candidate: str, declared_names: list[str]) -> Optional[str]:
    """
    将需求中抽到的候选名称和模型里真实存在的名称对齐。
    """
    if not candidate:
        return None

    candidate = candidate.strip().strip('.,;:()[]{}')
    candidate_norm = _normalize_component_name(candidate)
    if not candidate_norm:
        return None

    exact_map = {_normalize_component_name(name): name for name in declared_names}
    if candidate_norm in exact_map:
        return exact_map[candidate_norm]

    # 允许 ACAS_Monitor / ACAS_Monitor_impl / ACAS_Monitor.impl 这类变体互相匹配
    partial_matches = []
    for declared in declared_names:
        declared_norm = _normalize_component_name(declared)
        if candidate_norm in declared_norm or declared_norm in candidate_norm:
            partial_matches.append(declared)

    if partial_matches:
        # 优先返回更具体的声明名，例如 Supervisor.impl 而不是 Supervisor
        return max(partial_matches, key=len)

    return None


def _find_declared_name_in_requirement(requirement_text: str, declared_names: list[str]) -> Optional[str]:
    """
    优先从需求文本中直接匹配模型里真实声明过的组件名或其常见别名。
    """
    if not requirement_text or not declared_names:
        return None

    matches = []
    for declared in declared_names:
        aliases = {declared}
        parts = declared.split('.')
        aliases.add(parts[0])
        aliases.add(parts[-1])

        normalized_declared = _normalize_component_name(declared)
        if normalized_declared.endswith('.impl'):
            aliases.add(declared.rsplit('.', 1)[0])
        if normalized_declared.endswith('_impl'):
            aliases.add(re.sub(r'[_\.]?impl$', '', declared, flags=re.IGNORECASE))
        aliases.add(re.sub(r'[_\.]?impl$', '', parts[-1], flags=re.IGNORECASE))

        for alias in aliases:
            alias = alias.strip()
            if not alias:
                continue
            if re.search(rf'(?<![A-Za-z0-9_]){re.escape(alias)}(?![A-Za-z0-9_])', requirement_text):
                score = len(alias)
                if re.search(r'impl', declared, re.IGNORECASE):
                    score += 1000
                matches.append((score, len(declared), declared))

    if matches:
        matches.sort(reverse=True)
        return matches[0][2]

    return None


def extract_target_component(requirement_text: str, aadl_model: str) -> str:
    """
    从需求文本中提取目标组件名，并尽量映射到模型中真实存在的组件/实现。
    """
    declared_names = _collect_declared_component_names(aadl_model)

    mentioned_declared = _find_declared_name_in_requirement(requirement_text, declared_names)
    if mentioned_declared:
        return mentioned_declared

    patterns = [
        r"请为\s*([A-Za-z_][A-Za-z0-9_\.]*)",
        r"请为\s*.*?\b([A-Za-z_][A-Za-z0-9_\.]*)\b",
        r"请在\s*([A-Za-z_][A-Za-z0-9_\.]*)\s*组件",
        r"请根据\s*([A-Za-z_][A-Za-z0-9_\.]*)\s*的",
        r"针对\s*([A-Za-z_][A-Za-z0-9_\.]*)\s*组件",
        r"组件\s*([A-Za-z_][A-Za-z0-9_\.]*)",
        r"系统组件\s*([A-Za-z_][A-Za-z0-9_\.]*)",
        r"实现层\s*([A-Za-z_][A-Za-z0-9_\.]*)",
    ]

    candidate = None
    for pattern in patterns:
        match = re.search(pattern, requirement_text)
        if match:
            candidate = match.group(1)
            break

    resolved = _resolve_component_name(candidate or "", declared_names)

    # 如果需求里显式提到实现名，优先返回实现名
    if resolved and re.search(r'impl', resolved, re.IGNORECASE):
        return resolved
    if candidate and re.search(r'impl', candidate, re.IGNORECASE):
        return candidate

    # 否则尝试为基础组件补实现名
    base_name = resolved or candidate
    if base_name:
        normalized_base = _normalize_component_name(base_name)
        explicit_impls = [
            name for name in declared_names
            if re.search(r'impl', name, re.IGNORECASE)
            and _normalize_component_name(name).startswith(normalized_base)
        ]
        if explicit_impls:
            return max(explicit_impls, key=len)

        implementation_candidates = [
            f"{base_name}.{base_name}_impl",
            f"{base_name}.{base_name}_Impl",
            f"{base_name}.impl",
        ]
        for impl_name in implementation_candidates:
            impl_resolved = _resolve_component_name(impl_name, declared_names)
            if impl_resolved:
                return impl_resolved
        return f"{base_name}.impl"

    # 最后兜底：如果模型里只有一个实现，直接用它
    impls = [name for name in declared_names if re.search(r'impl', name, re.IGNORECASE)]
    if len(impls) == 1:
        return impls[0]

    raise ValueError("无法从需求文本中提取目标组件名")


def run_single_case(pipeline, case_num: int, case_letter: str = "A") -> Dict[str, Any]:
    case_str = f"Case{case_num:02d}"
    case_dir = f"{case_str}_{case_letter}"
    source_root = os.environ.get("AGREE_SOURCE_ROOT", os.path.abspath("data/Sources"))

    txt_file_path = os.path.join(source_root, case_dir, f"{case_str}_Base.txt")
    req_file_path = os.path.join(source_root, case_dir, f"{case_str}_Req.txt")
    aadl_file_path = os.path.join(source_root, case_dir, f"{case_str}_Base.aadl")

    if not os.path.exists(txt_file_path):
        raise FileNotFoundError(f"基础模型文件不存在: {txt_file_path}")
    if not os.path.exists(req_file_path):
        raise FileNotFoundError(f"需求文件不存在: {req_file_path}")

    with open(txt_file_path, 'r', encoding='utf-8') as f:
        aadl_model = f.read()

    with open(aadl_file_path, 'w', encoding='utf-8') as f:
        f.write(aadl_model)
    print(f"已生成 {aadl_file_path}")

    print("\n收集所有相关的AADL模型...")
    models = collect_aadl_models(aadl_file_path)

    with open(req_file_path, 'r', encoding='utf-8') as f:
        user_requirements = f.read().strip()
    print(f"已读取用户需求文件: {req_file_path}")

    target_component = extract_target_component(user_requirements, aadl_model)
    print(f"本次目标组件: {target_component}")

    result = pipeline.run_full_pipeline(
        aadl_model,
        user_requirements,
        target_component=target_component,
        models=models,
        case_num=f"{case_num:02d}",
        case_letter=case_letter
    )

    return {
        "case_num": f"{case_num:02d}",
        "case_letter": case_letter,
        "target_component": target_component,
        "result": result
    }



def collect_aadl_models(main_aadl_path):
    with open(main_aadl_path, 'r', encoding='utf-8') as f:
        main_content = f.read()

    references = []
    seen_paths = set()
    base_dir = os.path.dirname(main_aadl_path)
    base_name = os.path.basename(base_dir)

    case_dir_match = re.search(r'Case(\d+)', base_name)
    case_num = case_dir_match.group(1) if case_dir_match else "01"
    package_dir = os.path.join(base_dir, f"Case{case_num}")

    with_statements = []
    for clause in re.findall(r'with\s+([^;]+);', main_content):
        parts = [part.strip() for part in clause.split(",")]
        with_statements.extend([part for part in parts if part])

    for pkg in with_statements:
        possible_paths = [
            os.path.join(base_dir, f"{pkg}.aadl"),
            os.path.join(base_dir, f"{pkg}_nodes.aadl"),
            os.path.join(package_dir, f"{pkg}.aadl"),
            os.path.join(package_dir, f"{pkg}_nodes.aadl"),
        ]

        for path in possible_paths:
            normalized = os.path.normpath(path)
            if not os.path.exists(normalized) or normalized in seen_paths:
                continue
            with open(normalized, 'r', encoding='utf-8') as f:
                content = f.read()
            references.append({"path": normalized, "content": content})
            seen_paths.add(normalized)
            file_link = format_file_link(normalized)
            print(f"已收集引用包模型: {file_link}")
            break

    if os.path.isdir(package_dir):
        for file_name in sorted(os.listdir(package_dir)):
            if not file_name.lower().endswith(".aadl"):
                continue
            full_path = os.path.normpath(os.path.join(package_dir, file_name))
            if full_path in seen_paths:
                continue
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            references.append({"path": full_path, "content": content})
            seen_paths.add(full_path)
            file_link = format_file_link(full_path)
            print(f"已补充 Case 目录模型: {file_link}")

    return {"main": main_content, "references": references}

