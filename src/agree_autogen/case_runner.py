import os
import re
from typing import Any, Dict, Optional

from .runtime import format_file_link


_BUILTIN_PACKAGE_NAMES = {
    "aadl_project",
    "agree_constants",
    "agree_nodes",
    "agree_pltl",
    "agree_stdlib",
    "arinc429",
    "arinc653",
    "arp4761",
    "base_types",
    "behavior_properties",
    "code_generation_properties",
    "communication_properties",
    "data_model",
    "deployment",
    "deployment_properties",
    "dreal",
    "emv2",
    "errorlibrary",
    "linearizer",
    "memory_properties",
    "milstd882",
    "modeling_properties",
    "physical",
    "physicalresources",
    "programming_properties",
    "qs_properties",
    "sei",
    "thread_properties",
    "timing_properties",
}


def _repo_root() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _static_lib_dir() -> str:
    return os.environ.get(
        "AGREE_VALIDATOR_STATIC_LIBS",
        os.path.join(_repo_root(), "tools", "agree-validator", "static-libs"),
    )


def _external_aadl_lib_roots() -> list[str]:
    configured = os.environ.get("AGREE_AADL_LIB_WORKSPACE", "")
    roots = [path.strip() for path in configured.split(os.pathsep) if path.strip()]
    configured_dirs = os.environ.get("AGREE_AADL_LIB_DIRS", "")
    roots.extend(path.strip() for path in configured_dirs.split(os.pathsep) if path.strip())
    seen = set()
    existing = []
    for root in roots:
        normalized = os.path.normpath(root)
        key = normalized.lower()
        if key in seen or not os.path.isdir(normalized):
            continue
        seen.add(key)
        existing.append(normalized)
    return existing


def _top_level_package(model_unit: str) -> str:
    return model_unit.split("::", 1)[0].strip()


def _package_declared_in(content: str, package_name: str) -> bool:
    pattern = rf"(?im)^\s*(?:public\s+)?package\s+{re.escape(package_name)}(?:\b|::)"
    return re.search(pattern, content) is not None


def _library_unit_declared_in(content: str, unit_name: str) -> bool:
    normalized = (unit_name or "").strip().replace(".", "::")
    if not normalized:
        return False
    package_pattern = rf"(?im)^\s*(?:public\s+)?package\s+{re.escape(normalized)}(?:\b|::)"
    property_pattern = rf"(?im)^\s*property\s+set\s+{re.escape(normalized)}\b"
    return re.search(package_pattern, content) is not None or re.search(property_pattern, content) is not None


def _strip_aadl_line_comments(content: str) -> str:
    return re.sub(r"(?m)--.*$", "", content or "")


def _extract_qualified_unit_references(content: str) -> list[str]:
    refs: list[str] = []
    for match in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)+)\b", _strip_aadl_line_comments(content or "")):
        parts = match.group(1).split("::")
        if len(parts) < 2:
            continue
        if parts[0].lower() in _BUILTIN_PACKAGE_NAMES:
            continue
        for size in range(len(parts), 1, -1):
            candidate = "::".join(parts[:size])
            refs.append(candidate)
    return list(dict.fromkeys(refs))


def _find_dependency_file(package_name: str, preferred_dirs: list[str]) -> Optional[str]:
    primary_roots = preferred_dirs + _external_aadl_lib_roots()
    static_roots = [_static_lib_dir()]
    top_level = _top_level_package(package_name)
    lookup_order = [package_name]
    if top_level and top_level.lower() != package_name.lower():
        lookup_order.append(top_level)

    for roots in (primary_roots, static_roots):
        for candidate in lookup_order:
            for file_name in (f"{candidate}.aadl", f"{candidate}_nodes.aadl"):
                for root in roots:
                    if not root or not os.path.isdir(root):
                        continue
                    direct = os.path.join(root, file_name)
                    if os.path.isfile(direct):
                        return os.path.normpath(direct)
            for root in roots:
                if not root or not os.path.isdir(root):
                    continue
                for dirpath, _, filenames in os.walk(root):
                    for filename in filenames:
                        if not filename.lower().endswith(".aadl"):
                            continue
                        path = os.path.join(dirpath, filename)
                        try:
                            with open(path, "r", encoding="utf-8", errors="replace") as file:
                                content = file.read()
                        except OSError:
                            continue
                        if _library_unit_declared_in(content, candidate):
                            return os.path.normpath(path)
    return None


def _add_reference(references: list[dict[str, str]], seen_paths: set[str], path: str, label: str) -> bool:
    normalized = os.path.normpath(path)
    path_key = os.path.abspath(normalized).lower()
    if not os.path.exists(normalized) or path_key in seen_paths:
        return False
    with open(normalized, "r", encoding="utf-8", errors="replace") as file:
        content = file.read()
    references.append({"path": normalized, "content": content})
    seen_paths.add(path_key)
    print(f"{label}: {format_file_link(normalized)}")
    return True


def _collect_declared_component_names(aadl_model: str) -> list[str]:
    """Collect component type and implementation names declared in an AADL model."""
    names: list[str] = []
    patterns = [
        r"^\s*(system|process|thread|device|abstract|subprogram)\s+implementation\s+([A-Za-z_][A-Za-z0-9_\.]*)",
        r"^\s*(system|process|thread|device|abstract|subprogram)\s+([A-Za-z_][A-Za-z0-9_\.]*)",
    ]
    for line in aadl_model.splitlines():
        for pattern in patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                names.append(match.group(2))
                break
    return list(dict.fromkeys(names))


def _normalize_component_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]", "", name).lower()


def _resolve_component_name(candidate: str, declared_names: list[str]) -> Optional[str]:
    """Resolve a candidate name against names declared in the model."""
    if not candidate:
        return None

    candidate = candidate.strip().strip(".,;:()[]{}")
    candidate_norm = _normalize_component_name(candidate)
    if not candidate_norm:
        return None

    exact_map = {_normalize_component_name(name): name for name in declared_names}
    if candidate_norm in exact_map:
        return exact_map[candidate_norm]

    partial_matches = []
    for declared in declared_names:
        declared_norm = _normalize_component_name(declared)
        if candidate_norm in declared_norm or declared_norm in candidate_norm:
            partial_matches.append(declared)

    if partial_matches:
        return max(partial_matches, key=len)
    return None


def _find_declared_name_in_requirement(requirement_text: str, declared_names: list[str]) -> Optional[str]:
    """Prefer an explicit component or implementation name found in the requirement text."""
    if not requirement_text or not declared_names:
        return None

    matches = []
    for declared in declared_names:
        aliases = {declared}
        parts = declared.split(".")
        aliases.add(parts[0])
        aliases.add(parts[-1])
        aliases.add(re.sub(r"[_\.]?impl$", "", declared, flags=re.IGNORECASE))
        aliases.add(re.sub(r"[_\.]?impl$", "", parts[-1], flags=re.IGNORECASE))

        for alias in aliases:
            alias = alias.strip()
            if not alias:
                continue
            if re.search(rf"(?<![A-Za-z0-9_]){re.escape(alias)}(?![A-Za-z0-9_])", requirement_text):
                score = len(alias)
                if re.search(r"impl", declared, re.IGNORECASE):
                    score += 1000
                matches.append((score, len(declared), declared))

    if matches:
        matches.sort(reverse=True)
        return matches[0][2]
    return None


def extract_target_component(requirement_text: str, aadl_model: str) -> str:
    """Extract the target component from requirements and align it with model declarations."""
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
        r"(?:component|system|implementation)\s+([A-Za-z_][A-Za-z0-9_\.]*)",
        r"for\s+(?:the\s+)?([A-Za-z_][A-Za-z0-9_\.]*)\s+(?:component|system|implementation)",
        r"(?:specification|contract)\s+for\s+(?:the\s+)?([A-Za-z_][A-Za-z0-9_\.]*)",
    ]

    candidate = None
    for pattern in patterns:
        match = re.search(pattern, requirement_text, flags=re.IGNORECASE)
        if match:
            candidate = match.group(1)
            break

    resolved = _resolve_component_name(candidate or "", declared_names)
    if resolved and re.search(r"impl", resolved, re.IGNORECASE):
        return resolved

    base_name = resolved or candidate
    if base_name:
        normalized_base = _normalize_component_name(base_name)
        explicit_impls = [
            name
            for name in declared_names
            if re.search(r"impl", name, re.IGNORECASE)
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

    impls = [name for name in declared_names if re.search(r"impl", name, re.IGNORECASE)]
    if len(impls) == 1:
        return impls[0]

    raise ValueError("Unable to extract a target component from the requirement text")


def run_single_case(pipeline, case_num: int, case_letter: str = "A", setting: str = "E2") -> Dict[str, Any]:
    case_str = f"Case{case_num:03d}"
    legacy_case_str = f"Case{case_num:02d}"
    source_root = os.environ.get("AGREE_SOURCE_ROOT", os.path.abspath("data/benchmark/cases"))
    case_dirs = []
    if case_letter:
        case_dirs.append(f"{case_str}_{case_letter}")
        case_dirs.append(f"{legacy_case_str}_{case_letter}")
    case_dirs.append(case_str)
    case_dirs.append(legacy_case_str)
    case_dir = None
    case_file_label = case_str
    for candidate in case_dirs:
        candidate_path = os.path.join(source_root, candidate)
        for label in (case_str, legacy_case_str):
            if os.path.exists(os.path.join(candidate_path, f"{label}_Base.txt")) and os.path.exists(os.path.join(candidate_path, f"{label}_Req.txt")):
                case_dir = candidate
                case_file_label = label
                break
        if case_dir:
            break
    if case_dir is None:
        raise FileNotFoundError(f"No source case with Base/Req files found for {case_str}: {case_dirs}")

    txt_file_path = os.path.join(source_root, case_dir, f"{case_file_label}_Base.txt")
    req_file_path = os.path.join(source_root, case_dir, f"{case_file_label}_Req.txt")
    aadl_file_path = os.path.join(source_root, case_dir, f"{case_file_label}_Base.aadl")

    if not os.path.exists(txt_file_path):
        raise FileNotFoundError(f"Base model file does not exist: {txt_file_path}")
    if not os.path.exists(req_file_path):
        raise FileNotFoundError(f"Requirement file does not exist: {req_file_path}")

    with open(txt_file_path, "r", encoding="utf-8") as file:
        aadl_model = file.read()

    with open(aadl_file_path, "w", encoding="utf-8") as file:
        file.write(aadl_model)
    print(f"Generated AADL input file: {aadl_file_path}")

    print("\nCollecting related AADL models...")
    models = collect_aadl_models(aadl_file_path)

    with open(req_file_path, "r", encoding="utf-8") as file:
        user_requirements = file.read().strip()
    print(f"Loaded requirement file: {req_file_path}")

    target_component = extract_target_component(user_requirements, aadl_model)
    print(f"Target component: {target_component}")

    normalized_setting = setting.upper()
    if normalized_setting == "E1":
        result = pipeline.run_bare_pipeline(
            aadl_model,
            user_requirements,
            target_component=target_component,
            models=models,
            case_num=f"{case_num:03d}",
            case_letter=case_letter,
        )
    else:
        result = pipeline.run_full_pipeline(
            aadl_model,
            user_requirements,
            target_component=target_component,
            models=models,
            case_num=f"{case_num:03d}",
            case_letter=case_letter,
        )

    return {
        "case_num": f"{case_num:03d}",
        "case_letter": case_letter,
        "setting": normalized_setting,
        "target_component": target_component,
        "result": result,
    }


def collect_aadl_models(main_aadl_path):
    with open(main_aadl_path, "r", encoding="utf-8") as file:
        main_content = file.read()

    references = []
    seen_paths = {os.path.abspath(os.path.normpath(main_aadl_path)).lower()}
    base_dir = os.path.dirname(main_aadl_path)
    base_name = os.path.basename(base_dir)

    case_dir_match = re.search(r"Case(\d+)", base_name)
    case_num = case_dir_match.group(1) if case_dir_match else "01"
    package_dir = os.path.join(base_dir, f"Case{case_num}")
    package_dirs = [package_dir]
    for name in sorted(os.listdir(base_dir)):
        path = os.path.join(base_dir, name)
        if os.path.isdir(path) and re.match(r"(?i)^Case\d+", name) and path not in package_dirs:
            package_dirs.append(path)

    with_statements = []
    for clause in re.findall(r"(?im)^\s*with\s+([^;]+);", _strip_aadl_line_comments(main_content)):
        parts = [part.strip() for part in clause.split(",")]
        with_statements.extend([part for part in parts if part])

    for pkg in with_statements:
        top_pkg = _top_level_package(pkg)
        possible_paths = [
            os.path.join(base_dir, f"{pkg}.aadl"),
            os.path.join(base_dir, f"{pkg}_nodes.aadl"),
            os.path.join(base_dir, f"{top_pkg}.aadl"),
            os.path.join(base_dir, f"{top_pkg}_nodes.aadl"),
        ]
        for local_package_dir in package_dirs:
            possible_paths.extend(
                [
                    os.path.join(local_package_dir, f"{pkg}.aadl"),
                    os.path.join(local_package_dir, f"{pkg}_nodes.aadl"),
                    os.path.join(local_package_dir, f"{top_pkg}.aadl"),
                    os.path.join(local_package_dir, f"{top_pkg}_nodes.aadl"),
                ]
            )
        found = False
        for path in possible_paths:
            if _add_reference(references, seen_paths, path, "Collected referenced package model"):
                found = True
                break
        if found:
            continue
        if top_pkg.lower() in _BUILTIN_PACKAGE_NAMES:
            continue
        dependency = _find_dependency_file(pkg, [base_dir] + package_dirs)
        if dependency:
            _add_reference(references, seen_paths, dependency, "Collected external dependency model")
        else:
            print(f"Dependency not found for with clause: {pkg}")

    for local_package_dir in package_dirs:
        if os.path.isdir(local_package_dir):
            for file_name in sorted(os.listdir(local_package_dir)):
                if not file_name.lower().endswith(".aadl"):
                    continue
                full_path = os.path.normpath(os.path.join(local_package_dir, file_name))
                _add_reference(references, seen_paths, full_path, "Collected case-local model")

    dependency_scan_content = "\n".join([main_content] + [ref.get("content", "") for ref in references])
    for unit in _extract_qualified_unit_references(dependency_scan_content):
        dependency = _find_dependency_file(unit, [base_dir] + package_dirs)
        if dependency:
            _add_reference(references, seen_paths, dependency, "Collected qualified reference dependency model")

    return {"main": main_content, "references": references}
