"""
实验记录模块
功能：
1. 记录初始生成的AADL代码
2. 记录修复后的AADL代码
3. 计算修复行数
4. 对错误类型进行 T1-T5 分类
5. 生成实验报告
"""

import os
import re
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class ErrorClassification:
    """错误分类结果"""
    T1: int = 0  # 词法与基础语法
    T2: int = 0  # 外部引用与上下文
    T3: int = 0  # 架构组件结构违规
    T4: int = 0  # 声明与标识符冲突
    T5: int = 0  # 类型与数值逻辑

    def to_dict(self) -> Dict[str, int]:
        return asdict(self)

    def has_any_error(self) -> bool:
        return sum([self.T1, self.T2, self.T3, self.T4, self.T5]) > 0


class ErrorClassifier:
    """错误分类器 - 仅使用 LLM 将验证错误分类为 T1-T5"""

    # 缓存每个错误的分类结果
    _error_type_cache: Dict[str, str] = {}

    @classmethod
    def classify_error(cls, error_text: str) -> List[str]:
        """
        将单个错误分类，返回可能的类型列表（T1-T5）
        先检查缓存，如果没有则返回 ["T1"] 作为兜底

        Args:
            error_text: 错误信息文本

        Returns:
            错误类型列表，如 ["T4"]
        """
        if error_text in cls._error_type_cache:
            return [cls._error_type_cache[error_text]]
        return ["T1"]

    @classmethod
    def classify_errors(cls, errors: List[str], aadl_code: Optional[str] = None) -> ErrorClassification:
        """
        批量分类错误 - 仅使用 LLM 进行智能分类

        Args:
            errors: 错误信息列表
            aadl_code: 可选的 AADL 代码上下文

        Returns:
            ErrorClassification 对象
        """
        result = ErrorClassification()
        cls._error_type_cache.clear()

        if not errors:
            return result

        # 必须使用 LLM 错误分析器
        from error_type_analyzer import LLMErrorAnalyzer

        print(f"\n[LLM 错误分类] 开始分析 {len(errors)} 个错误...")
        analyzer = LLMErrorAnalyzer()

        # 逐个分析错误，同时缓存每个错误的分类结果
        for error in errors:
            error_type = analyzer.analyze_single_error(error, aadl_code)
            cls._error_type_cache[error] = error_type

            if error_type == "T1":
                result.T1 += 1
            elif error_type == "T2":
                result.T2 += 1
            elif error_type == "T3":
                result.T3 += 1
            elif error_type == "T4":
                result.T4 += 1
            elif error_type == "T5":
                result.T5 += 1

            print(f"  [LLM] {error_type}: {error[:80]}...")

        print(f"[LLM 错误分类] 完成 - T1:{result.T1}, T2:{result.T2}, T3:{result.T3}, T4:{result.T4}, T5:{result.T5}")

        return result


class CodeChangeAnalyzer:
    """代码变更分析器 - 计算修复行数"""

    @classmethod
    def count_changed_lines(cls, original_code: str, fixed_code: str) -> int:
        """
        计算变更的行数

        Args:
            original_code: 原始代码
            fixed_code: 修复后的代码

        Returns:
            变更的行数
        """
        original_lines = original_code.strip().splitlines()
        fixed_lines = fixed_code.strip().splitlines()

        # 简单的行对比
        changed = 0
        max_lines = max(len(original_lines), len(fixed_lines))

        for i in range(max_lines):
            orig_line = original_lines[i] if i < len(original_lines) else ""
            fix_line = fixed_lines[i] if i < len(fixed_lines) else ""

            if orig_line.strip() != fix_line.strip():
                changed += 1

        return changed

    @classmethod
    def get_line_changes(cls, original_code: str, fixed_code: str) -> List[Dict[str, Any]]:
        """
        获取详细的行变更信息

        Args:
            original_code: 原始代码
            fixed_code: 修复后的代码

        Returns:
            变更列表，每个元素包含行号、原始内容、修复后内容
        """
        original_lines = original_code.strip().splitlines()
        fixed_lines = fixed_code.strip().splitlines()

        changes = []
        max_lines = max(len(original_lines), len(fixed_lines))

        for i in range(max_lines):
            orig_line = original_lines[i] if i < len(original_lines) else ""
            fix_line = fixed_lines[i] if i < len(fixed_lines) else ""

            if orig_line.strip() != fix_line.strip():
                changes.append({
                    "line_number": i + 1,
                    "original": orig_line,
                    "fixed": fix_line
                })

        return changes


class ExperimentRecorder:
    """实验记录器 - 管理整个实验记录流程"""

    def __init__(self, base_dir: str = None):
        if base_dir is None:
            base_dir = os.environ.get("AGREE_DATA_ROOT", os.path.abspath("data"))
        self.base_dir = base_dir
        self.sources_dir = os.path.join(base_dir, "Sources")
        self.result_dir = os.path.join(base_dir, "Result")

    def get_case_dir(self, case_num: str, case_letter: str) -> str:
        """获取案例目录"""
        return os.path.join(self.result_dir, f"Case{case_num}_{case_letter}")

    def get_report_dir(self, case_num: str, case_letter: str) -> str:
        """获取报告目录"""
        case_dir = self.get_case_dir(case_num, case_letter)
        return os.path.join(case_dir, "Report")

    def ensure_report_dir(self, case_num: str, case_letter: str) -> str:
        """确保报告目录存在"""
        report_dir = self.get_report_dir(case_num, case_letter)
        os.makedirs(report_dir, exist_ok=True)
        return report_dir

    def _stage_display_name(self, stage: str) -> str:
        stage_map = {
            "aadl_model_analysis": "AADL 模型分析阶段",
            "requirement_analysis": "需求分析阶段",
            "agree_generation": "AGREE 规范生成阶段",
            "pipeline_exception": "流水线执行异常阶段",
        }
        return stage_map.get(stage, stage)

    def _extract_error_items(self, report_dir: str, limit: int = 8) -> List[str]:
        error_file = None
        for name in os.listdir(report_dir):
            if name.endswith("_errors.txt"):
                error_file = os.path.join(report_dir, name)
                break

        if not error_file or not os.path.exists(error_file):
            return []

        items: List[str] = []
        with open(error_file, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if re.match(r"^\d+\.\s+", stripped):
                    items.append(re.sub(r"^\d+\.\s+", "", stripped))
                if len(items) >= limit:
                    break
        return items

    def _infer_failure_summary(self, stage: str, error_message: str, report_dir: str) -> Dict[str, Any]:
        error_items = self._extract_error_items(report_dir)
        lowered = (error_message or "").lower()
        joined_errors = "\n".join(error_items).lower()

        direct_cause = "当前日志不足以唯一定位直接原因。"
        likely_category = "其他失败"
        interpretation = "需要结合错误列表和运行日志进一步判断。"

        if "nonetype" in lowered and (".get" in lowered or "attribute 'get'" in lowered or 'attribute "get"' in lowered):
            direct_cause = "后续汇总阶段访问了空对象，触发了空值访问异常。"
            likely_category = "后期修复失败后的框架异常包装"
            interpretation = (
                "这通常不代表模型在前期就崩溃，而是前面某一步未产出有效结果，"
                "后续汇总时仍把空对象当作字典继续读取。"
            )
        elif "未找到合并后的aadl代码" in error_message:
            direct_cause = "修复阶段未拿到有效的合并后 AADL 代码。"
            likely_category = "后期修复失败"
            interpretation = "模型初稿已进入验证修复链路，但修复后的有效结果没有成功产出。"
        elif "未能生成有效的agree规范" in error_message:
            direct_cause = "AGREE 生成结果不满足提取器要求，未形成有效规范。"
            likely_category = "前期崩溃"
            interpretation = "这类失败通常说明模型对输出格式和提示词约束遵循不足。"
        elif "缺少必要字段" in error_message or "json" in lowered:
            direct_cause = "结构化输出未满足预期格式约束。"
            likely_category = "前期崩溃"
            interpretation = "这类失败通常发生在模型分析阶段，说明模型难以稳定返回严格结构化结果。"

        if error_items:
            unresolved_refs = [e for e in error_items if "Couldn't resolve reference" in e]
            type_errors = [
                e for e in error_items
                if "must be of the same type" in e or "is of type" in e or "type" in e.lower()
            ]
            lhs_errors = [e for e in error_items if "LHS of assignment must" in e or "left hand side" in e.lower()]
            if unresolved_refs or type_errors or lhs_errors:
                fragments = []
                if unresolved_refs:
                    fragments.append("存在未定义引用/作用域不成立")
                if type_errors:
                    fragments.append("存在类型不一致")
                if lhs_errors:
                    fragments.append("存在非法赋值目标")
                interpretation += " 从验证错误看，" + "、".join(fragments) + "。"

        return {
            "stage_display": self._stage_display_name(stage),
            "direct_cause": direct_cause,
            "likely_category": likely_category,
            "interpretation": interpretation,
            "top_errors": error_items[:6],
        }

    def save_initial_code(self, case_num: str, case_letter: str, code: str) -> str:
        """
        保存初始生成的代码

        Args:
            case_num: 案例编号，如 "01"
            case_letter: 案例字母，如 "A" 或 "B"
            code: 初始生成的 AADL 代码

        Returns:
            保存的文件路径
        """
        report_dir = self.ensure_report_dir(case_num, case_letter)
        file_path = os.path.join(report_dir, f"Case{case_num}_initial.txt")
        first_file_path = os.path.join(report_dir, f"Case{case_num}_first.txt")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        with open(first_file_path, 'w', encoding='utf-8') as f:
            f.write(code)

        return file_path

    def save_fixed_code(self, case_num: str, case_letter: str, code: str) -> str:
        """
        保存修复后的代码

        Args:
            case_num: 案例编号，如 "01"
            case_letter: 案例字母，如 "A" 或 "B"
            code: 修复后的 AADL 代码

        Returns:
            保存的文件路径
        """
        report_dir = self.ensure_report_dir(case_num, case_letter)
        file_path = os.path.join(report_dir, f"Case{case_num}_fixed.txt")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)

        return file_path

    def save_errors(self, case_num: str, case_letter: str,
                     aadl_errors: List[str], agree_errors: List[str]) -> str:
        """
        保存检测到的错误

        Args:
            case_num: 案例编号
            case_letter: 案例字母
            aadl_errors: AADL 验证器检测到的错误
            agree_errors: AGREE 验证器检测到的错误

        Returns:
            保存的文件路径
        """
        report_dir = self.ensure_report_dir(case_num, case_letter)
        file_path = os.path.join(report_dir, f"Case{case_num}_errors.txt")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("AADL VALIDATOR ERRORS\n")
            f.write("=" * 80 + "\n\n")
            for i, error in enumerate(aadl_errors, 1):
                f.write(f"{i}. {error}\n")

            f.write("\n" + "=" * 80 + "\n")
            f.write("AGREE VALIDATOR ERRORS\n")
            f.write("=" * 80 + "\n\n")
            for i, error in enumerate(agree_errors, 1):
                f.write(f"{i}. {error}\n")

        return file_path

    def generate_report(self, case_num: str, case_letter: str,
                        initial_code: str, fixed_code: str,
                        aadl_errors: List[str], agree_errors: List[str],
                        token_stats: Dict[str, int], runtime: float,
                        success: bool, repair_count: int = 0) -> Dict[str, Any]:
        """
        生成完整的实验报告

        Args:
            case_num: 案例编号
            case_letter: 案例字母
            initial_code: 初始代码
            fixed_code: 修复后的代码
            aadl_errors: AADL 错误列表
            agree_errors: AGREE 错误列表
            token_stats: Token 使用统计
            runtime: 运行时间（秒）
            success: 是否成功
            repair_count: 修复迭代次数

        Returns:
            报告数据字典
        """
        report_dir = self.ensure_report_dir(case_num, case_letter)

        # 分类错误（使用 LLM）
        all_errors = aadl_errors + agree_errors
        error_classification = ErrorClassifier.classify_errors(all_errors, initial_code)

        # 计算变更行数
        changed_lines = CodeChangeAnalyzer.count_changed_lines(initial_code, fixed_code)
        line_changes = CodeChangeAnalyzer.get_line_changes(initial_code, fixed_code)

        # 构建报告数据
        report_data = {
            "case_id": f"Case{case_num}_{case_letter}",
            "timestamp": datetime.now().isoformat(),
            "success": success,
            "token_stats": token_stats,
            "runtime_seconds": runtime,
            "changed_lines": changed_lines,
            "repair_count": repair_count,
            "error_classification": error_classification.to_dict(),
            "all_errors_count": len(all_errors),
            "aadl_errors_count": len(aadl_errors),
            "agree_errors_count": len(agree_errors),
        }

        # 保存 JSON 报告
        json_path = os.path.join(report_dir, f"Case{case_num}_report.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)

        # 保存 Markdown 报告
        md_path = os.path.join(report_dir, f"Case{case_num}_report.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# 实验报告: Case{case_num}_{case_letter}\n\n")
            f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write("## 基本信息\n\n")
            f.write(f"| 项目 | 内容 |\n")
            f.write(f"|------|------|\n")
            f.write(f"| 案例编号 | Case{case_num}_{case_letter} |\n")
            f.write(f"| 最终状态 | {'Success' if success else 'Fail'} |\n")
            f.write(f"| 运行时间 | {runtime:.2f} 秒 |\n")
            f.write(f"| 修复行数 | {changed_lines} 行 |\n")
            f.write(f"| 修复迭代次数 | {repair_count} 次 |\n\n")

            f.write("## Token 使用统计\n\n")
            f.write(f"| 类型 | Token 数 |\n")
            f.write(f"|------|----------|\n")
            f.write(f"| Prompt | {token_stats.get('prompt_tokens', 0)} |\n")
            f.write(f"| Completion | {token_stats.get('completion_tokens', 0)} |\n")
            f.write(f"| **总计** | **{token_stats.get('total_tokens', 0)}** |\n\n")

            f.write("## 错误类型统计\n\n")
            f.write(f"| 错误类型 | 数量 | 说明 |\n")
            f.write(f"|---------|------|------|\n")
            f.write(f"| T1 (词法与基础语法) | {error_classification.T1} | 关键词拼写、符号错误等 |\n")
            f.write(f"| T2 (外部引用与上下文) | {error_classification.T2} | 跨包引用、未定义引用 |\n")
            f.write(f"| T3 (架构组件结构违规) | {error_classification.T3} | 组件结构、连接问题 |\n")
            f.write(f"| T4 (声明与标识符冲突) | {error_classification.T4} | 重复声明、命名冲突 |\n")
            f.write(f"| T5 (类型与数值逻辑) | {error_classification.T5} | 类型错误、数值逻辑 |\n")
            f.write(f"| **总计** | **{sum(error_classification.to_dict().values())}** | |\n\n")

            f.write("## 详细错误列表\n\n")
            if aadl_errors:
                f.write("### AADL Validator 错误\n\n")
                for i, error in enumerate(aadl_errors, 1):
                    types = ErrorClassifier.classify_error(error)
                    f.write(f"{i}. [{', '.join(types)}] {error}\n\n")

            if agree_errors:
                f.write("### AGREE Validator 错误\n\n")
                for i, error in enumerate(agree_errors, 1):
                    types = ErrorClassifier.classify_error(error)
                    f.write(f"{i}. [{', '.join(types)}] {error}\n\n")

            if not success:
                f.write("## 失败分析\n\n")
                if not aadl_errors and not agree_errors:
                    f.write("- 本案例未提供可用于归因的验证错误列表。\n")
                    f.write("- 该失败更可能来自前置阶段、修复阶段或流程控制层。\n\n")
                else:
                    dominant_types = []
                    for key, value in error_classification.to_dict().items():
                        if value > 0:
                            dominant_types.append(f"{key}={value}")
                    f.write(f"- 该案例未通过最终验证，主要错误类型分布为：{', '.join(dominant_types) if dominant_types else '无'}。\n")
                    if agree_errors and not aadl_errors:
                        f.write("- 错误主要集中在 AGREE 层，说明 AADL 外层结构基本可解析，但合同生成或修复结果未收敛。\n")
                    elif aadl_errors and not agree_errors:
                        f.write("- 错误主要集中在 AADL 层，说明模型在外层语法或结构约束上存在明显问题。\n")
                    else:
                        f.write("- 错误同时出现在 AADL 与 AGREE 层，说明该案例同时存在外层结构与合同内容问题。\n")
                    if repair_count > 0:
                        f.write(f"- 本案例已进入修复链路，并尝试修复 {repair_count} 轮，但最终仍未通过。\n\n")
                    else:
                        f.write("- 本案例未形成有效的修复收敛结果。\n\n")

            if line_changes:
                f.write("## 代码变更详情\n\n")
                for change in line_changes:
                    f.write(f"### 第 {change['line_number']} 行\n\n")
                    f.write(f"```\n原始: {change['original']}\n")
                    f.write(f"修复: {change['fixed']}\n```\n\n")

        return report_data

    def generate_failure_report(self, case_num: str, case_letter: str,
                                stage: str, error_message: str,
                                token_stats: Dict[str, int], runtime: float,
                                initial_code: str = "", fixed_code: str = "") -> Dict[str, Any]:
        """为前置阶段失败但未进入完整验证流程的 case 生成最小报告。"""
        report_dir = self.ensure_report_dir(case_num, case_letter)
        failure_summary = self._infer_failure_summary(stage, error_message, report_dir)

        report_data = {
            "case_id": f"Case{case_num}_{case_letter}",
            "timestamp": datetime.now().isoformat(),
            "success": False,
            "failed_stage": stage,
            "error_message": error_message,
            "failure_summary": {
                "stage_display": failure_summary["stage_display"],
                "direct_cause": failure_summary["direct_cause"],
                "likely_category": failure_summary["likely_category"],
                "interpretation": failure_summary["interpretation"],
                "top_errors": failure_summary["top_errors"],
            },
            "token_stats": token_stats,
            "runtime_seconds": runtime,
            "changed_lines": CodeChangeAnalyzer.count_changed_lines(initial_code, fixed_code),
            "repair_count": 0,
            "error_classification": {
                "T1": 0,
                "T2": 0,
                "T3": 0,
                "T4": 0,
                "T5": 0,
            },
            "all_errors_count": 1 if error_message else 0,
            "aadl_errors_count": 0,
            "agree_errors_count": 0,
        }

        json_path = os.path.join(report_dir, f"Case{case_num}_report.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)

        md_path = os.path.join(report_dir, f"Case{case_num}_report.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# 实验报告: Case{case_num}_{case_letter}\n\n")
            f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## 结果\n\n")
            f.write(f"- 状态: Fail\n")
            f.write(f"- 失败阶段: {failure_summary['stage_display']}\n")
            f.write(f"- 错误信息: {error_message}\n")
            f.write(f"- 运行时间: {runtime:.2f} 秒\n")
            f.write(f"- Prompt Tokens: {token_stats.get('prompt_tokens', 0)}\n")
            f.write(f"- Completion Tokens: {token_stats.get('completion_tokens', 0)}\n")
            f.write(f"- Total Tokens: {token_stats.get('total_tokens', 0)}\n")
            f.write("\n## 失败原因分析\n\n")
            f.write(f"- 直接触发原因: {failure_summary['direct_cause']}\n")
            f.write(f"- 归因类别: {failure_summary['likely_category']}\n")
            f.write(f"- 解释: {failure_summary['interpretation']}\n")
            if failure_summary["top_errors"]:
                f.write("\n## 关键错误线索\n\n")
                for idx, item in enumerate(failure_summary["top_errors"], 1):
                    f.write(f"{idx}. {item}\n")
                f.write("\n")
            f.write("## 用于模型筛选的判读建议\n\n")
            f.write("- 如果失败发生在模型分析或 AGREE 生成前期，通常可视为“前期崩溃”，说明模型对格式或提示词约束遵循不足。\n")
            f.write("- 如果失败发生在验证/修复之后，更应记录为“进入完整流程但未收敛”或“后期修复失败”，而不应简单归为前期崩溃。\n")
            f.write("- 如果错误信息包含空对象访问或类似程序异常，则应区分“模型生成问题”和“流程汇总阶段异常包装”两个层次。\n")

        if initial_code:
            self.save_initial_code(case_num, case_letter, initial_code)
        if fixed_code:
            self.save_fixed_code(case_num, case_letter, fixed_code)

        return report_data


# 快捷函数
def create_recorder() -> ExperimentRecorder:
    """创建实验记录器"""
    return ExperimentRecorder()
