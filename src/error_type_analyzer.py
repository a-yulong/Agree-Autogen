"""
错误类型分析工具 - 使用 LLM 智能分析 AADL 错误并进行 T1-T5 分类
独立脚本，可单独运行，也可被 demo12.py 调用
"""

import os
import re
import json
import sys
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from openai import OpenAI


# ==================== 配置 ====================

# LLM 配置 - 与 demo12.py 保持一致
LLM_BASE_URL = os.environ.get("AGREE_ERROR_ANALYZER_BASE_URL", os.environ.get("AGREE_MODEL_BASE_URL", "https://api.openai.com/v1"))
LLM_API_KEY = os.environ.get("AGREE_ERROR_ANALYZER_API_KEY", os.environ.get("AGREE_MODEL_API_KEY", ""))
LLM_MODEL_NAME = os.environ.get("AGREE_ERROR_ANALYZER_MODEL", os.environ.get("AGREE_MODEL_NAME", "gpt-4o-mini"))


@dataclass
class ErrorClassification:
    """错误分类结果"""
    T1: int = 0  # 词法与基础语法
    T2: int = 0  # 外部引用与上下文
    T3: int = 0  # 架构组件结构违规
    T4: int = 0  # 声明与标识符冲突
    T5: int = 0  # 类型与数值逻辑

    def to_dict(self) -> Dict[str, int]:
        return {
            "T1": self.T1,
            "T2": self.T2,
            "T3": self.T3,
            "T4": self.T4,
            "T5": self.T5
        }

    def total(self) -> int:
        return self.T1 + self.T2 + self.T3 + self.T4 + self.T5


class LLMErrorAnalyzer:
    """基于 LLM 的错误类型分析器"""

    # 错误类型定义（用于提示词）
    ERROR_TYPE_DEFINITIONS = """
T1 (词法与基础语法): 关键词拼写错误、符号错误、语法结构错误、缺少分号、括号不匹配等
T2 (外部引用与上下文): 跨包引用错误、未定义的引用、找不到包/库、import/with 语句错误等
T3 (架构组件结构违规): 组件定义错误、system/implementation 结构问题、connection/port/feature 配置错误、子组件结构问题等
T4 (声明与标识符冲突): 重复声明、命名冲突、标识符重定义、eq/const/assign 声明问题等
T5 (类型与数值逻辑): 类型错误、类型不匹配、数值逻辑问题、布尔/整数/实数类型相关错误、条件判断错误等
"""

    def __init__(self, base_url: str = LLM_BASE_URL, api_key: str = LLM_API_KEY, model_name: str = LLM_MODEL_NAME):
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key
        )
        self.model_name = model_name

    def analyze_single_error(self, error_text: str, aadl_code: Optional[str] = None) -> str:
        """
        分析单个错误，返回其类型 (T1-T5)

        Args:
            error_text: 错误信息文本
            aadl_code: 可选的 AADL 代码上下文

        Returns:
            错误类型，如 "T1"
        """
        system_prompt = """你是一个专业的 AADL 错误分类专家。请将给定的错误信息归类到以下 5 种类型之一：

T1 (词法与基础语法): 关键词拼写错误、符号错误、语法结构错误、缺少分号、括号不匹配、"no viable alternative" 等解析错误
T2 (外部引用与上下文): 跨包引用错误、未定义的引用、找不到包/库、import/with 语句错误、"Couldn't resolve reference" 等
T3 (架构组件结构违规): 组件定义错误、system/implementation 结构问题、connection/port/feature 配置错误、子组件结构问题等
T4 (声明与标识符冲突): 重复声明、命名冲突、标识符重定义、eq/const/assign 声明问题、"Multiple assignments" 等
T5 (类型与数值逻辑): 类型错误、类型不匹配、数值逻辑问题、布尔/整数/实数类型相关错误、条件判断错误等

注意：错误信息可能带有 "[AGREE Validator]" 或 "[AADL Validator]" 前缀，请忽略这些前缀，只关注错误内容本身。

请只返回一个结果：T1、T2、T3、T4 或 T5，不要任何其他解释。"""

        # 清理错误信息，移除前缀
        clean_error = error_text
        if clean_error.startswith("[AGREE Validator] "):
            clean_error = clean_error[len("[AGREE Validator] "):]
        elif clean_error.startswith("[AADL Validator] "):
            clean_error = clean_error[len("[AADL Validator] "):]

        user_prompt = f"请分析以下错误信息，返回它的类型（T1-T5）：\n\n错误信息：\n{clean_error}"

        if aadl_code:
            user_prompt += f"\n\nAADL 代码上下文（可选参考）：\n{aadl_code[:1000]}"

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.1,
                max_tokens=50
            )
            result = response.choices[0].message.content.strip()

            # 提取 T1-T5
            match = re.search(r"T[1-5]", result)
            if match:
                return match.group(0)

            # 兜底：如果没明确提取到，尝试匹配
            if "T1" in result or "语法" in result or "词法" in result:
                return "T1"
            elif "T2" in result or "引用" in result or "外部" in result:
                return "T2"
            elif "T3" in result or "组件" in result or "架构" in result:
                return "T3"
            elif "T4" in result or "声明" in result or "冲突" in result:
                return "T4"
            elif "T5" in result or "类型" in result or "逻辑" in result:
                return "T5"

            # 默认返回 T1
            return "T1"

        except Exception as e:
            print(f"LLM 分析失败: {e}，使用默认 T1")
            return "T1"

    def analyze_errors(self, errors: List[str], aadl_code: Optional[str] = None) -> ErrorClassification:
        """
        批量分析错误

        Args:
            errors: 错误信息列表
            aadl_code: 可选的 AADL 代码上下文

        Returns:
            ErrorClassification 对象
        """
        result = ErrorClassification()

        print(f"\n===== 开始分析 {len(errors)} 个错误 =====\n")

        for i, error in enumerate(errors, 1):
            error_type = self.analyze_single_error(error, aadl_code)
            print(f"  [{i}/{len(errors)}] {error_type}: {error[:100]}...")

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

        print(f"\n===== 分析完成 =====")
        print(f"  T1: {result.T1}")
        print(f"  T2: {result.T2}")
        print(f"  T3: {result.T3}")
        print(f"  T4: {result.T4}")
        print(f"  T5: {result.T5}")
        print(f"  总计: {result.total()}")

        return result


def extract_errors_from_report(report_content: str) -> List[str]:
    """
    从 AADL Inspector 报告中提取错误信息

    Args:
        report_content: 报告内容

    Returns:
        错误信息列表
    """
    errors = []

    # 尝试提取 TextEditor::fastaddText 格式的错误
    error_patterns = re.findall(
        r'\$\{sbpText\}\.text fastinsert end (\d+) d\d+.*?TextEditor::fastaddText \$sbpText "(.*?)"',
        report_content,
        re.DOTALL
    )

    for line_num, error_text in error_patterns:
        error_text = error_text.strip()
        if error_text and not any(ignore in error_text.lower() for ignore in ["set lines(error)", "<any-"]):
            errors.append(f"[行号 {line_num}] {error_text}")

    # 如果没找到，尝试简单提取
    if not errors:
        text_editor_errors = re.findall(r'TextEditor::fastaddText \$sbpText "(.*?)"', report_content, re.DOTALL)
        for error_text in text_editor_errors:
            error_text = error_text.strip()
            if error_text and not any(ignore in error_text.lower() for ignore in ["set lines(error)", "<any-"]):
                errors.append(error_text)

    return errors


def analyze_case_report(case_num: str, case_letter: str,
                        base_dir: str = None,
                        use_llm: bool = True) -> Dict[str, Any]:
    """
    分析单个案例的报告

    Args:
        case_num: 案例编号，如 "01"
        case_letter: 案例字母，如 "A"
        base_dir: 基础目录
        use_llm: 是否使用 LLM 分析（False 则使用基于规则的方法）

    Returns:
        分析结果字典
    """
    # 查找报告文件
    result_report_dir = os.path.join(base_dir, "Result", f"Case{case_num}_{case_letter}", "Report")
    sources_report_dir = os.path.join(base_dir, "Sources", f"Case{case_num}_{case_letter}", "Report")

    report_file = os.path.join(result_report_dir, f"Case{case_num}_report.txt")
    if not os.path.exists(report_file):
        report_file = os.path.join(sources_report_dir, f"Case{case_num}_report.txt")

    if not os.path.exists(report_file):
        print(f"错误：找不到报告文件: {report_file}")
        return {"success": False, "error": "报告文件不存在"}

    # 读取报告
    print(f"读取报告: {report_file}")
    with open(report_file, 'r', encoding='utf-8', errors='ignore') as f:
        report_content = f.read()

    # 提取错误
    errors = extract_errors_from_report(report_content)
    print(f"提取到 {len(errors)} 个错误")

    # 读取 AADL 代码（可选）
    aadl_code = None
    initial_code_file = os.path.join(result_report_dir, f"Case{case_num}_initial.txt")
    if os.path.exists(initial_code_file):
        with open(initial_code_file, 'r', encoding='utf-8') as f:
            aadl_code = f.read()

    # 分析错误类型
    if use_llm:
        analyzer = LLMErrorAnalyzer()
        classification = analyzer.analyze_errors(errors, aadl_code)
    else:
        # 使用基于规则的方法（从 experiment_recorder 导入）
        try:
            from experiment_recorder import ErrorClassifier
            classification = ErrorClassifier.classify_errors(errors)
        except ImportError:
            print("警告：无法导入 experiment_recorder，使用空分类")
            classification = ErrorClassification()

    # 构建结果
    result = {
        "success": True,
        "case_id": f"Case{case_num}_{case_letter}",
        "report_file": report_file,
        "total_errors": len(errors),
        "errors": errors,
        "error_classification": classification.to_dict(),
        "total": classification.total()
    }

    # 保存分析结果
    output_file = os.path.join(result_report_dir, f"Case{case_num}_error_analysis.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\n分析结果已保存到: {output_file}")

    return result


def print_error_summary(analysis_result: Dict[str, Any]):
    """打印错误类型统计摘要"""
    if not analysis_result.get("success"):
        print("分析失败")
        return

    ec = analysis_result["error_classification"]
    print("\n" + "=" * 60)
    print("错误类型统计")
    print("=" * 60)
    print(f"| 错误类型              | 数量 | 说明                          |")
    print(f"|-----------------------|------|-------------------------------|")
    print(f"| T1 (词法与基础语法)   | {ec['T1']:4} | 关键词拼写、符号错误等        |")
    print(f"| T2 (外部引用与上下文) | {ec['T2']:4} | 跨包引用、未定义引用          |")
    print(f"| T3 (架构组件结构违规) | {ec['T3']:4} | 组件结构、连接问题            |")
    print(f"| T4 (声明与标识符冲突) | {ec['T4']:4} | 重复声明、命名冲突            |")
    print(f"| T5 (类型与数值逻辑)   | {ec['T5']:4} | 类型错误、数值逻辑            |")
    print(f"| **总计**              | {analysis_result['total']:4} |                               |")
    print("=" * 60)


def main():
    """主函数 - 命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description="AADL 错误类型分析工具")
    parser.add_argument("--case", type=str, default="42", help="案例编号，如 42")
    parser.add_argument("--letter", type=str, default="A", help="案例字母，如 A")
    parser.add_argument("--base-dir", type=str, default=os.environ.get("AGREE_DATA_ROOT", os.path.abspath("data")), help="基础目录")
    parser.add_argument("--no-llm", action="store_true", help="不使用 LLM，使用基于规则的分类")
    parser.add_argument("--report", type=str, default="", help="直接指定报告文件路径")

    args = parser.parse_args()

    if args.report:
        # 直接分析指定的报告文件
        if not os.path.exists(args.report):
            print(f"错误：文件不存在: {args.report}")
            return

        print(f"读取报告: {args.report}")
        with open(args.report, 'r', encoding='utf-8', errors='ignore') as f:
            report_content = f.read()

        errors = extract_errors_from_report(report_content)
        print(f"提取到 {len(errors)} 个错误")

        if not args.no_llm:
            analyzer = LLMErrorAnalyzer()
            classification = analyzer.analyze_errors(errors)
        else:
            try:
                from experiment_recorder import ErrorClassifier
                classification = ErrorClassifier.classify_errors(errors)
            except ImportError:
                classification = ErrorClassification()

        result = {
            "success": True,
            "report_file": args.report,
            "total_errors": len(errors),
            "errors": errors,
            "error_classification": classification.to_dict(),
            "total": classification.total()
        }

        output_file = args.report.replace(".txt", "_analysis.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\n分析结果已保存到: {output_file}")

        print_error_summary(result)

    else:
        # 分析案例
        result = analyze_case_report(
            args.case,
            args.letter,
            args.base_dir,
            use_llm=not args.no_llm
        )
        print_error_summary(result)


if __name__ == "__main__":
    main()

