import os
import re
import hashlib
import subprocess
import time
import tempfile
import threading
import shutil
import json
from pathlib import Path
from typing import List, Dict, Optional, Any

from openai import OpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

from . import runtime
from .runtime import logger, format_file_link, HAS_WIN32, start_window_monitor, create_recorder
from .agents import (
    Conversation,
    RequirementsAnalystAgent,
    AGREEGeneratorAgent,
    AADLModelAnalystAgent,
    AADLMergeAgent,
    AADLValidatorAgent,
)

class AGREEVerificationPipeline:
    """
    AGREE 形式化规范生成与验证流水线
    支持：
      - 加载 PDF/TXT 文档（含 @@@...@@@ 标记的 AGREE 代码块）
      - 构建双路向量库（生成用 + 验证用）
      - 解析 AADL 模型结构（JSON 输出）
      - 多Agent协作：需求分析师、AGREE生成器、AADL验证器
    """

    def __init__(self, docs_directory: str, force_rebuild: bool = False, use_rag: bool = True):
        self.docs_directory = docs_directory
        self.force_rebuild = force_rebuild
        self.use_rag = use_rag  # 控制是否使用RAG增强
        self.state = {}  # 存储各阶段中间结果
        # Token统计变量
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_tokens = 0

        # 向量库配置
        self.chunk_size_gen = 512  # 生成时使用较大 chunk
        self.chunk_size_val = 512   # 验证时使用小 chunk 提高精度
        self.chunk_overlap = 50
        self.top_k = 8
        self.embedding_model = "BAAI/bge-base-en-v1.5"
        self.collection_name_gen = "agree-unified-generate-v3"
        self.collection_name_val = "agree-code-v3"
        self.vectorstore_dir = "./vectorstore_cache"

        # LLM 配置
        self.llm_api_key = runtime.MODEL_API_KEY
        self.llm_base_url = runtime.MODEL_BASE_URL
        self.llm_model_name = runtime.MODEL_NAME
        self.result_root = runtime.GLM_RESULT_ROOT
        self.client = OpenAI(api_key=self.llm_api_key, base_url=self.llm_base_url)

        # AGREE standalone 验证器配置
        self.osate_path = os.environ.get("OSATE_HOME", "")
        self.standalone_validator_root = os.environ.get("AGREE_VALIDATOR_ROOT", os.path.abspath("tools/agree-validator-standalone"))
        self.standalone_validator_out = os.path.join(self.standalone_validator_root, "out")
        self.standalone_validator_main = "com.example.agreevalidator.AgreeValidationCli"
        self.standalone_java_home = os.environ.get("JAVA_HOME", "")
        self.static_libs_dir = os.path.join(self.standalone_validator_root, "static-libs")
        self._dependency_catalog = None

        preferred_java = os.path.join(self.standalone_java_home, "bin", "java.exe") if self.standalone_java_home else ""
        self.java_path = preferred_java if os.path.exists(preferred_java) else "java"

        # 初始化向量数据库
        self._initialize_vectorstore_gen()
        self._initialize_vectorstore_val()
        logger.info("向量数据库初始化完成")
        
        # 初始化Agent
        self.analyst_agent = RequirementsAnalystAgent(self)
        self.generator_agent = AGREEGeneratorAgent(self)
        self.validator_agent = AADLValidatorAgent(self)
        
        # 创建共享对话对象
        self.conversation = Conversation()
        self.analyst_agent.set_conversation(self.conversation)
        self.generator_agent.set_conversation(self.conversation)
        self.validator_agent.set_conversation(self.conversation)

    def _extract_with_units(self, aadl_text: str) -> List[str]:
        units = []
        if not aadl_text:
            return units
        for line in aadl_text.splitlines():
            match = re.match(r'^\s*with\s+([^;]+);\s*$', line)
            if not match:
                continue
            units.extend([part.strip() for part in match.group(1).split(",") if part.strip()])
        return units

    def _is_builtin_unit(self, unit_name: str) -> bool:
        builtins = {
            "aadl_project",
            "base_types",
            "communication_properties",
            "data_model",
            "data_model",
            "deployment_properties",
            "memory_properties",
            "modeling_properties",
            "programming_properties",
            "thread_properties",
            "timing_properties",
        }
        return unit_name.lower() in builtins

    def _declared_units_in_file(self, file_path: str) -> Dict[str, str]:
        declared = {}
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                header = f.read(4096)
        except Exception:
            return declared

        patterns = [
            r'^\s*package\s+([A-Za-z0-9_:]+)\b',
            r'^\s*property\s+set\s+([A-Za-z0-9_]+)\s+is\b',
        ]
        for pattern in patterns:
            for match in re.finditer(pattern, header, re.MULTILINE):
                declared[match.group(1).lower()] = file_path
        return declared

    def _build_dependency_catalog(self) -> Dict[str, str]:
        if self._dependency_catalog is not None:
            return self._dependency_catalog

        catalog = {}
        roots = [
            self.static_libs_dir,
            self.osate_path,
        ]
        for root in roots:
            if not os.path.isdir(root):
                continue
            for dirpath, dirnames, filenames in os.walk(root):
                if ".metadata" in dirpath:
                    continue
                for filename in filenames:
                    if not filename.lower().endswith(".aadl"):
                        continue
                    file_path = os.path.join(dirpath, filename)
                    for unit_name, declared_path in self._declared_units_in_file(file_path).items():
                        catalog.setdefault(unit_name, declared_path)

        self._dependency_catalog = catalog
        return catalog

    def _scan_case_declared_units(self, case_num: str, case_letter: str) -> Dict[str, str]:
        case_num = f"{int(case_num):02d}"
        case_dir = os.path.join(os.environ.get("AGREE_SOURCE_ROOT", os.path.abspath("data/Sources")), f"Case{case_num}_{case_letter}")
        package_dir = os.path.join(case_dir, f"Case{case_num}")
        declared = {}

        for root in [case_dir, package_dir]:
            if not os.path.isdir(root):
                continue
            for dirpath, dirnames, filenames in os.walk(root):
                if ".metadata" in dirpath:
                    continue
                for filename in filenames:
                    if not filename.lower().endswith(".aadl"):
                        continue
                    file_path = os.path.join(dirpath, filename)
                    declared.update(self._declared_units_in_file(file_path))

        return declared

    def _sync_case_dependencies(self, case_num: str, case_letter: str, aadl_text: str = "") -> List[str]:
        case_num = f"{int(case_num):02d}"
        case_dir = os.path.join(os.environ.get("AGREE_SOURCE_ROOT", os.path.abspath("data/Sources")), f"Case{case_num}_{case_letter}")
        package_dir = os.path.join(case_dir, f"Case{case_num}")
        os.makedirs(package_dir, exist_ok=True)

        required_units = set(self._extract_with_units(aadl_text))
        base_txt = os.path.join(case_dir, f"Case{case_num}_Base.txt")
        if os.path.exists(base_txt):
            with open(base_txt, "r", encoding="utf-8", errors="ignore") as f:
                required_units.update(self._extract_with_units(f.read()))

        local_units = self._scan_case_declared_units(case_num, case_letter)
        catalog = self._build_dependency_catalog()

        for unit_name in sorted(required_units):
            if self._is_builtin_unit(unit_name) or unit_name.lower() in local_units:
                continue
            source_path = catalog.get(unit_name.lower())
            if not source_path or not os.path.exists(source_path):
                continue
            target_path = os.path.join(package_dir, os.path.basename(source_path))
            if not os.path.exists(target_path):
                shutil.copy2(source_path, target_path)
                print(f"已补充缺失依赖: {format_file_link(target_path)}")
            local_units.update(self._declared_units_in_file(target_path))

        support_files = []
        for root in [case_dir, package_dir]:
            if not os.path.isdir(root):
                continue
            for dirpath, dirnames, filenames in os.walk(root):
                if ".metadata" in dirpath:
                    continue
                for filename in filenames:
                    if filename.lower().endswith(".aadl"):
                        support_files.append(os.path.join(dirpath, filename))

        return sorted(set(support_files))

    def _load_document(self, file_path: str) -> List[Document]:
        """加载 PDF 或 TXT 文件，提取内容或 AGREE 代码块"""
        documents = []
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        if file_path.lower().endswith(".pdf"):
            logger.info(f"正在加载 PDF 文件: {path.name}")
            loader = PyPDFLoader(file_path)
            pages = loader.load()
            with open(file_path, 'rb') as f:
                content_hash = hashlib.md5(f.read()).hexdigest()
            for i, page in enumerate(pages):
                page.metadata.update({
                    "source": str(path),
                    "page": i + 1,
                    "type": "pdf_content",
                    "file_hash": content_hash,
                    "content_hash": hashlib.md5(page.page_content.encode('utf-8')).hexdigest()
                })
            documents.extend(pages)

        elif file_path.lower().endswith(".txt"):
            logger.info(f"正在加载 TXT 文件: {path.name}")
            with open(file_path, 'r', encoding='utf-8') as f:
                full_text = f.read()
            file_hash = hashlib.md5(full_text.encode('utf-8')).hexdigest()
            agree_code_blocks = re.findall(r"@@@\s*(.*?)\s*@@@", full_text, re.DOTALL)

            if agree_code_blocks:
                for idx, code in enumerate(agree_code_blocks, start=1):
                    code = code.strip()
                    if not code:
                        # 移除迭代修复逻辑，直接返回错误信息
                        return {
                            "success": False,
                            "error": "验证失败",
                            "errors": errors,
                            "verification_result": inspection_result.get('report_content', '')
                        }
                    content_hash = hashlib.md5(code.encode('utf-8')).hexdigest()
                    doc = Document(page_content=code, metadata={
                        "source": str(path),
                        "type": "agree_code",
                        "file_hash": file_hash,
                        "code_block_index": idx,
                        "content_hash": content_hash
                    })
                    documents.append(doc)
            else:
                content_hash = hashlib.md5(full_text.encode('utf-8')).hexdigest()
                doc = Document(page_content=full_text, metadata={
                    "source": str(path),
                    "type": "txt_plain",
                    "file_hash": file_hash,
                    "content_hash": content_hash
                })
                documents.append(doc)
                logger.warning(f"TXT 文件未找到 @@@ 代码块，按普通文本加载")

        return documents

    def _deduplicate_documents(self, documents: List[Document]) -> List[Document]:
        seen_hashes = set()
        unique_docs = []
        for doc in documents:
            content_hash = doc.metadata.get("content_hash") or hashlib.md5(doc.page_content.encode('utf-8')).hexdigest()
            doc.metadata["content_hash"] = content_hash
            if content_hash not in seen_hashes:
                seen_hashes.add(content_hash)
                unique_docs.append(doc)
        logger.info(f"文档去重完成: 原始 {len(documents)} 个，去重后 {len(unique_docs)} 个")
        return unique_docs

    def _load_all_documents(self) -> List[Document]:
        all_docs = []
        directory_path = Path(self.docs_directory)
        if not directory_path.exists():
            raise FileNotFoundError(f"文档目录不存在: {self.docs_directory}")

        target_files = list(directory_path.glob("*.pdf")) + list(directory_path.glob("*.txt"))
        if not target_files:
            raise FileNotFoundError(f"在目录中未找到任何 PDF 或 TXT 文件: {self.docs_directory}")

        for file_path in target_files:
            try:
                docs = self._load_document(str(file_path))
                all_docs.extend(docs)
                logger.info(f"成功加载: {file_path.name}（{len(docs)} 个文档片段）")
            except Exception as e:
                logger.error(f"加载失败: {file_path}, 错误: {e}")

        return self._deduplicate_documents(all_docs)

    def _initialize_vectorstore_gen(self):
        """初始化【生成】专用向量数据库"""
        embedder = HuggingFaceEmbeddings(
            model_name=self.embedding_model,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )

        vectorstore_gen_path = os.path.join(self.vectorstore_dir, self.collection_name_gen)
        if os.path.exists(vectorstore_gen_path) and not self.force_rebuild:
            logger.info("从缓存加载【生成】用向量数据库...")
            self.vectorstore_gen = Chroma(
                persist_directory=vectorstore_gen_path,
                embedding_function=embedder,
                collection_name=self.collection_name_gen
            )
        else:
            logger.info("正在构建【生成】用向量数据库...")
            raw_docs = self._load_all_documents()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size_gen,
                chunk_overlap=self.chunk_overlap,
                separators=["\n\n### ", "\n\n#### ", "\n\n", r"(?<=\.)\s+", "\n", ";", "。", "；", " "]
            )
            split_docs = splitter.split_documents(raw_docs)
            os.makedirs(vectorstore_gen_path, exist_ok=True)
            self.vectorstore_gen = Chroma.from_documents(
                documents=split_docs,
                embedding=embedder,
                collection_name=self.collection_name_gen,
                persist_directory=vectorstore_gen_path
            )

    def _initialize_vectorstore_val(self):
        """初始化【验证】专用向量数据库"""
        embedder = HuggingFaceEmbeddings(
            model_name=self.embedding_model,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )

        vectorstore_val_path = os.path.join(self.vectorstore_dir, self.collection_name_val)
        if os.path.exists(vectorstore_val_path) and not self.force_rebuild:
            logger.info("从缓存加载【验证】用向量数据库...")
            self.vectorstore_val = Chroma(
                persist_directory=vectorstore_val_path,
                embedding_function=embedder,
                collection_name=self.collection_name_val
            )
        else:
            logger.info("正在构建【验证】用向量数据库...")
            raw_docs = self._load_all_documents()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size_val,
                chunk_overlap=self.chunk_overlap,
                separators=["\n\n### ", "\n\n#### ", "\n\n", r"(?<=\.)\s+", "\n", ";", "。", "；", " "]
            )
            split_docs = splitter.split_documents(raw_docs)
            os.makedirs(vectorstore_val_path, exist_ok=True)
            self.vectorstore_val = Chroma.from_documents(
                documents=split_docs,
                embedding=embedder,
                collection_name=self.collection_name_val,
                persist_directory=vectorstore_val_path
            )

    def _augment_prompt(self, query: str, mode: str = "generate", context: Optional[Dict] = None) -> str:
        """使用向量数据库检索相关知识，增强提示词
        如果use_rag为False，则不进行RAG检索，直接返回原始查询
        """
        # 检查是否启用RAG
        if not self.use_rag:
            logger.info(f"[RAG已禁用] 不进行知识库检索，直接使用原始查询")
            return query
            
        vectorstore = self.vectorstore_gen if mode == "generate" else self.vectorstore_val
        
        # 针对不同模式，设置不同的检索数量
        if mode == "validate":
            # 验证模式获取5个文档
            k_value = 5
            
            # 优化查询，确保包含AADL语法相关关键词
            enhanced_query = query
            # 如果查询包含错误信息，提取错误类型关键词以增强检索
            if "unexpected keyword" in query or "parsing" in query:
                enhanced_query = query + " AADL语法规则 错误修复 AGREE规范"
            
            results = vectorstore.similarity_search(enhanced_query, k=k_value)
        elif mode == "generate":
            # AGREE生成模式获取15个文档
            results = vectorstore.similarity_search(query, k=15)
        else:
            # 其他模式使用默认值
            results = vectorstore.similarity_search(query, k=self.top_k)
        
        # 构建 source_knowledge
        source_knowledge = ""
        for r in results:
            source = r.metadata.get("source", "unknown")
            doc_type = r.metadata.get("type", "N/A")
            source_knowledge += (
                f"【来源: {Path(source).name} | 类型: {doc_type}】\n"
                f"{r.page_content}\n\n"
            )
        
        # 构建增强提示词，针对不同模式有不同的指导
        if mode == "validate":
            augmented_prompt = f"""
请基于以下知识库信息修复AADL代码中的语法错误：

重要提示：
- 仔细分析每个错误信息
- 从参考知识中查找对应的正确语法规则
- 优先使用AGREE_knowledge_dataset中的示例和规范
- 确保修复后的代码符合AADL语法标准

参考知识：
{source_knowledge}

待修复代码和错误信息：
{query}
"""
        else:
            augmented_prompt = f"""
请基于以下知识库信息来回答问题或生成代码：

参考知识：
{source_knowledge}

问题或需求：
{query}
"""
        
        return augmented_prompt

    def _infer_target_component(self, target_component: Optional[str] = None) -> Optional[str]:
        """
        推断目标组件名称
        
        Args:
            target_component: 可选的目标组件名称，如果提供则直接返回
            
        Returns:
            目标组件名称或None
        """
        # 如果提供了目标组件，则直接返回
        if target_component:
            print(f"使用指定的目标组件: {target_component}")
            return target_component
            
        # 否则使用自动推断逻辑
        print("\n使用自动推断逻辑，判断应该插入AGREE代码的位置...")
        
        # 使用原始的自动推断逻辑
        components = self.state.get('aadl_analysis', {}).get('components', [])
        if not isinstance(components, list) or not components:
            print("错误：未找到组件信息")
            return None

        for comp in components:
            if isinstance(comp, dict) and comp.get('type') == 'system_implementation' and comp.get('name'):
                print(f"自动推断的目标组件: {comp['name']}")
                return comp['name']

        for comp in components:
            if isinstance(comp, dict) and comp.get('type') == 'system' and comp.get('name'):
                print(f"自动推断的目标组件: {comp['name']}")
                return comp['name']

        first_comp = components[0]
        if isinstance(first_comp, dict) and 'name' in first_comp:
            print(f"自动推断的目标组件: {first_comp['name']}")
            return first_comp['name']

        print("错误：无法推断目标组件")
        return None


    def run_aadl_validation_inspection(self, state, inspector_exe=None, report_dir=None):
        """运行AADL Inspector分析生成的AADL模型并解析结果"""
        result = {
            "inspection_successful": False,
            "has_errors": False,
            "has_warnings": False,
            "errors": [],
            "warnings": [],
            "report_path": None
        }
        
        try:
            # 获取模型文件路径
            model_path = state.get("final_model_path")
            if not model_path or not os.path.exists(model_path):
                print("\n错误：无法找到AADL模型文件\n")
                return result
            
            # 确定AADL Inspector可执行文件路径
            if not inspector_exe:
                # 尝试从环境变量获取，或使用默认路径
                inspector_exe = os.environ.get("AADL_INSPECTOR_PATH", 
                                              "E:\\AI-1.10\\bin\\AADLInspector.exe")
            
            # 确定报告保存目录和文件名
            if not report_dir:
                report_dir = os.environ.get("AADL_REPORT_DIR", 
                                          os.path.dirname(model_path))
            
            # 确保报告目录存在
            os.makedirs(report_dir, exist_ok=True)
            
            # 输出标题，优化可读性
            print("\n===== AADL 模型验证分析 =====\n")

            # 从state中获取Case编号和字母（优先）
            case_num = state.get('case_num')
            case_letter = state.get('case_letter')

            # 如果state中没有，尝试从model_path中提取
            if case_num is None or case_letter is None:
                case_match = re.search(r'Case(\d+)_gen_([A-Z])', model_path)
                if case_match:
                    case_num = case_match.group(1)
                    case_letter = case_match.group(2)
                else:
                    case_match = re.search(r'Case(\d+)', model_path)
                    case_num = case_match.group(1) if case_match else '01'
                    case_letter = 'A'
            
            case_str = f"Case{case_num}"
            case_dir = f"Case{case_num}_{case_letter}"
            merged_aadl = state.get("merged_aadl", "")
            self._sync_case_dependencies(case_num, case_letter, merged_aadl)

            # 构建命令
            # 注意：在Windows系统中，路径需要正确转义
            # 使用用户指定的命令行格式

            # 将 modified_model.aadl 的内容写入到 CaseXX_Base.aadl（备份原文件）
            sources_case_dir = os.path.join(os.environ.get("AGREE_SOURCE_ROOT", os.path.abspath("data/Sources")), case_dir)
            original_aadl = os.path.join(sources_case_dir, f"{case_str}_Base.aadl")

            # 将 modified_model.aadl 的内容写入到 CaseXX_Base.aadl
            try:
                with open(model_path, 'r', encoding='utf-8') as f_src:
                    content = f_src.read()
                with open(original_aadl, 'w', encoding='utf-8') as f_dst:
                    f_dst.write(content)
            except Exception as e:
                print(f"[警告] 写入文件失败: {e}")

            main_aadl = original_aadl

            # 收集 Sources 目录下的所有 AADL 文件（包括子目录 CaseXX/）
            project_root = os.path.join(sources_case_dir, case_str)

            # 先在 Sources 目录下生成报告（AADL Inspector喜欢在这里）
            sources_report_dir = os.path.join(sources_case_dir, "Report")
            os.makedirs(sources_report_dir, exist_ok=True)
            sources_result_file = os.path.join(sources_report_dir, f"{case_str}_report.txt")

            # 同时准备 Result 目录
            result_report_dir = os.path.join(self.result_root, case_dir, "Report")
            os.makedirs(result_report_dir, exist_ok=True)
            result_file = os.path.join(result_report_dir, f"{case_str}_report.txt")

            # 动态生成临时的.aic文件，放在 Sources 目录下（和AADL文件在一起）
            temp_aic = os.path.join(sources_case_dir, "temp_project.aic")

            # 收集所有AADL文件
            aadl_files = [main_aadl]
            # 扫描子文件夹中所有的 aadl 文件
            if os.path.exists(project_root):
                for root, dirs, files in os.walk(project_root):
                    for file in files:
                        if file.endswith(".aadl"):
                            aadl_files.append(os.path.join(root, file))

            # 写入 .aic 文件 (每行一个路径)
            with open(temp_aic, 'w', encoding='utf-8') as f:
                for path in aadl_files:
                    f.write(f"{path}\n")

            # 添加--show false参数，解决文件未被选中的问题 - 在Sources目录生成报告
            inspector_command = f'"E:\\AI-1.10\\bin\\AADLInspector.exe" -a "{temp_aic}" --plugin Static.parse --result "{sources_result_file}" --show false --aadlVersion V2'
            print(f"正在执行命令: {inspector_command}\n")

            # 启动弹窗监控线程
            stop_event = threading.Event()
            monitor_thread = None
            if HAS_WIN32:
                monitor_thread = start_window_monitor(stop_event)
                print("[提示] 已启动弹窗自动关闭监控")

            try:
                # 执行命令（不使用 check=True，因为许可证问题可能导致非零退出码，但报告仍可能成功生成）
                proc = subprocess.run(inspector_command, shell=True, timeout=120)
            except Exception as e:
                # 即使命令执行出错，也继续尝试读取报告文件
                print(f"AADL Inspector 执行时出现异常（继续尝试读取报告）: {str(e)}")
                proc = None
            finally:
                # 停止监控线程
                stop_event.set()
                if monitor_thread:
                    monitor_thread.join(timeout=1.0)

            print(f"AADL Inspector 分析完成")
            print(f"尝试读取报告: {result_file}\n")

            report_to_read = self._resolve_inspector_report_file(
                [sources_result_file, result_file],
                [sources_report_dir, result_report_dir],
                case_str
            )

            if report_to_read and os.path.normcase(report_to_read) != os.path.normcase(result_file):
                try:
                    shutil.copy2(report_to_read, result_file)
                    report_to_read = result_file
                except Exception:
                    pass

            # 读取并解析分析报告（优先从Result目录读取）
            if report_to_read and os.path.exists(report_to_read):
                # 尝试多种编码读取文件，解决编码错误问题
                encodings = ['utf-8', 'utf-16', 'latin-1']
                report_content = ""
                for encoding in encodings:
                    try:
                        with open(report_to_read, 'r', encoding=encoding) as f:
                            report_content = f.read()
                        break  # 成功读取后跳出循环
                    except UnicodeDecodeError:
                        continue

                # 如果所有编码都失败，使用二进制模式读取并转换
                if not report_content:
                    with open(report_to_read, 'rb') as f:
                        binary_content = f.read()
                    # 使用latin-1作为兜底编码（可以解码任何字节序列）
                    report_content = binary_content.decode('latin-1')

                # 改进的错误检测逻辑
                # 1. 首先检查是否有明确的成功标志
                success_markers = ["Model parsed successfully", "解析成功", "成功通过"]
                is_success = any(marker in report_content for marker in success_markers)

                # 2. 定义更全面的错误模式，特别关注TextEditor::fastaddText中的错误信息
                error_markers = [
                    "cannot parse", "parsing error", "syntax error",
                    "parsing AADL_Declaration", "unexpected identifier",
                    "unexpected keyword", "错误", "无法解析"
                ]
                has_errors = False
                errors = []

                # 3. 检查TextEditor::fastaddText格式的错误信息（这是AADL Inspector的标准错误输出格式）
                # 同时提取错误信息和对应的行号
                error_patterns = re.findall(r'\$\{sbpText\}\.text fastinsert end (\d+) d\d+.*?TextEditor::fastaddText \$sbpText "(.*?)"', report_content, re.DOTALL)

                # 提取所有的行号-错误信息对
                line_error_map = {}
                for line_num, error_text in error_patterns:
                    error_text = error_text.strip()
                    if error_text and not any(ignore in error_text.lower() for ignore in ["set lines(error)", "<any-"]):
                        line_error_map[line_num] = error_text

                # 提取单独的错误行号信息（从lappend lines(error)行）
                error_lines = re.findall(r'lappend lines\(error\) (\d+)', report_content)
                for line_num in error_lines:
                    if line_num not in line_error_map:
                        # 如果这个行号还没有对应的错误信息，尝试查找附近的错误文本
                        pass

                # 构建带行号的错误信息
                for line_num, error_text in sorted(line_error_map.items(), key=lambda x: int(x[0])):
                    errors.append(f"[行号 {line_num}] {error_text}")

                # 如果没有找到带行号的错误，使用原来的方法提取
                if not errors:
                    text_editor_errors = re.findall(r'TextEditor::fastaddText \$sbpText "(.*?)"', report_content, re.DOTALL)
                    for error_text in text_editor_errors:
                        error_text = error_text.strip()
                        if error_text and not any(ignore in error_text.lower() for ignore in ["set lines(error)", "<any-"]):
                            errors.append(error_text)

                # 4. 如果没找到TextEditor格式错误，检查其他错误标记
                if not errors:
                    for marker in error_markers:
                        if marker.lower() in report_content.lower():
                            has_errors = True
                            # 尝试提取相关错误上下文
                            context_pattern = r'((?:\w+\s*:\s*)?.*?' + re.escape(marker) + r'.*?)(?:\n|$)'
                            context_matches = re.findall(context_pattern, report_content, re.IGNORECASE)
                            for match in context_matches[:5]:  # 限制数量避免过多
                                errors.append(match.strip())
                else:
                    has_errors = True

                # 5. 检查警告
                warning_markers = ["warning", " 警告"]
                has_warnings = any(marker in report_content.lower() for marker in warning_markers)

                # 整理结果
                result["report_content"] = report_content
                result["has_errors"] = has_errors
                result["has_warnings"] = has_warnings
                result["inspection_successful"] = True  # 只要能读取报告就算成功
                result["inspection_report_path"] = report_to_read
                result["errors"] = list(set(errors))  # 去重

                # 输出分析结果，优化格式和可读性，同时保存带序号的格式化错误
                print("===== 验证结果 =====\n")
                formatted_errors_with_index = []  # 保存带序号的错误信息，如"错误 1: [行号 75] ..."
                if is_success:
                    print("模型解析成功，无需修复错误\n")
                elif has_errors and errors:
                    print(f"发现 {len(result['errors'])} 个错误需要修复\n")
                    for i, error in enumerate(result['errors'], 1):
                        formatted_error = f"错误 {i}: {error}"
                        print(f"  {formatted_error}")
                        print()  # 每个错误后添加空行
                        formatted_errors_with_index.append(formatted_error)
                elif has_errors:
                    print("分析报告发现存在错误，但无法提取具体错误信息\n")
                else:
                    print("分析报告未发现明确错误，但也没有成功标志\n")
                    # 增加安全性检查：如果报告很短或包含特定关键词，可能存在问题
                    if len(report_content.strip()) < 100 or "parsing" in report_content.lower():
                        print("警告：报告内容异常，可能存在未检测到的解析问题\n")
                        result["has_errors"] = True
                        result["errors"].append("报告内容异常，可能存在解析问题")

                # 保存带序号的格式化错误信息
                result["formatted_errors_with_index"] = formatted_errors_with_index
            else:
                print(f"错误：无法找到生成的分析报告: {result_file} 或 {sources_result_file}\n")
                result["errors"].append(f"报告文件不存在: {result_file}")
                if proc is not None:
                    result["errors"].append(f"AADL Inspector 返回码: {proc.returncode}")

        except Exception as e:
            print(f"运行AADL Inspector时发生错误: {str(e)}\n")
            import traceback
            traceback.print_exc()
            result["errors"].append(f"执行错误: {str(e)}")

        # 分析完成后清理：删除临时.aic文件
        if os.path.exists(temp_aic):
            try:
                os.remove(temp_aic)
            except Exception as e:
                pass
        # 【暂时保留】不删除Sources目录下的报告文件，用于调试
        # if os.path.exists(sources_result_file):
        #     try:
        #         os.remove(sources_result_file)
        #     except Exception as e:
        #         pass

        # 将检查结果保存到状态中
        state["inspection_result"] = result
        return result

    def build_agree_validator_classpath(self) -> str:
        """构建当前 standalone AGREE 验证器的 classpath"""
        return os.pathsep.join([
            self.standalone_validator_out,
            os.path.join(self.osate_path, "plugins", "*")
        ])

    def _ensure_standalone_validator_ready(self) -> None:
        if not os.path.isdir(self.standalone_validator_root):
            raise FileNotFoundError(f"找不到 standalone 验证器目录: {self.standalone_validator_root}")
        if not os.path.isdir(self.standalone_validator_out):
            raise FileNotFoundError(
                f"找不到 standalone 验证器编译输出目录: {self.standalone_validator_out}。请先运行 build.ps1 编译验证器。"
            )
        if not os.path.isdir(os.path.join(self.osate_path, "plugins")):
            raise FileNotFoundError(f"找不到 OSATE plugins 目录: {self.osate_path}")

    def _write_temp_project_file(self, project_dir: str, project_name: str) -> None:
        project_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
    <name>{project_name}</name>
    <comment></comment>
    <projects>
    </projects>
    <buildSpec>
        <buildCommand>
            <name>org.eclipse.xtext.ui.shared.xtextBuilder</name>
            <arguments>
            </arguments>
        </buildCommand>
    </buildSpec>
    <natures>
        <nature>org.osate.core.aadlnature</nature>
        <nature>org.eclipse.xtext.ui.shared.xtextNature</nature>
    </natures>
</projectDescription>
"""
        with open(os.path.join(project_dir, ".project"), "w", encoding="utf-8") as f:
            f.write(project_content)

    def _build_temp_agree_project(self, model_path: str, merged_aadl: str, workspace_dir: str, state: Dict[str, Any] = None) -> Dict[str, str]:
        project_name = "CaseProject"
        project_dir = os.path.join(workspace_dir, project_name)
        os.makedirs(project_dir, exist_ok=True)
        self._write_temp_project_file(project_dir, project_name)

        main_file_name = os.path.basename(model_path) if model_path else "modified_model.aadl"
        temp_model_path = os.path.join(project_dir, main_file_name)
        with open(temp_model_path, "w", encoding="utf-8") as f:
            f.write(merged_aadl)

        case_num = state.get("case_num") if state else None
        case_letter = state.get("case_letter") if state else None
        if case_num is not None and case_letter:
            support_files = self._sync_case_dependencies(case_num, case_letter, merged_aadl)
            support_dir = os.path.join(project_dir, "External_Libs")
            os.makedirs(support_dir, exist_ok=True)
            for support_file in support_files:
                if os.path.normcase(support_file) == os.path.normcase(model_path):
                    continue
                base_name = os.path.basename(support_file)
                if re.fullmatch(rf"Case{int(case_num):02d}_Base\.aadl", base_name, re.IGNORECASE):
                    continue
                target_path = os.path.join(support_dir, base_name)
                if os.path.normcase(target_path) != os.path.normcase(support_file):
                    shutil.copy2(support_file, target_path)

        return {
            "workspace_dir": workspace_dir,
            "project_dir": project_dir,
            "model_path": temp_model_path,
        }

    def _resolve_inspector_report_file(self, primary_paths: List[str], fallback_dirs: List[str], case_str: str) -> Optional[str]:
        for _ in range(20):
            for path in primary_paths:
                if path and os.path.exists(path) and os.path.getsize(path) > 0:
                    return path
            time.sleep(0.5)

        candidates = []
        for folder in fallback_dirs:
            if not folder or not os.path.isdir(folder):
                continue
            for name in os.listdir(folder):
                if not name.lower().endswith(".txt"):
                    continue
                if case_str.lower() not in name.lower() and "report" not in name.lower():
                    continue
                file_path = os.path.join(folder, name)
                if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
                    candidates.append(file_path)

        if not candidates:
            return None

        candidates.sort(key=lambda p: os.path.getmtime(p), reverse=True)
        return candidates[0]

    def _format_standalone_issue(self, issue: Dict[str, Any]) -> str:
        message = str(issue.get("issue", "")).strip()
        file_path = str(issue.get("file", "")).strip()
        line_no = issue.get("line")

        location_parts = []
        if file_path:
            location_parts.append(file_path)
        if line_no not in (None, "", 0):
            location_parts.append(f"行 {line_no}")

        if location_parts:
            return f"[{' | '.join(location_parts)}] {message}"
        return message

    def filter_java_output(self, stdout, stderr):
        """
        过滤 Java 输出，去除无效提示，只保留真正的验证结果

        修改点：只保留从 "AGREE Validation Results" 开始的内容，
             同时过滤掉 "Package ... has duplicates" 这类重复包错误
        """
        filtered_lines = []
        removed_count = 0
        duplicate_error_found = False
        errors_line_index = -1

        # 合并 stdout 和 stderr
        all_lines = []
        if stdout:
            all_lines.extend(stdout.splitlines())
        if stderr:
            all_lines.extend(stderr.splitlines())

        # 策略1：查找 "AGREE Validation Results"，只保留从这里开始的内容
        found_results = False
        for i, line in enumerate(all_lines):
            line_stripped = line.strip()

            # 检查是否找到验证结果开始标记
            if "AGREE Validation Results" in line_stripped:
                found_results = True

            if found_results:
                # 检查是否是需要过滤的特定错误
                is_filtered_error = False

                # 过滤 "Package ... has duplicates" 错误
                if "ERROR:" in line_stripped and "has duplicates" in line_stripped:
                    is_filtered_error = True
                    duplicate_error_found = True
                    removed_count += 1

                # 记录 Errors: 行的位置，稍后可能需要更新
                if line_stripped.startswith("Errors:"):
                    errors_line_index = len(filtered_lines)

                if not is_filtered_error:
                    filtered_lines.append(line)
            else:
                # 前面的内容都过滤掉
                removed_count += 1

        # 如果发现了重复包错误，并且有 Errors: 行，更新计数
        if duplicate_error_found and errors_line_index >= 0 and errors_line_index < len(filtered_lines):
            line = filtered_lines[errors_line_index]
            line_stripped = line.strip()
            if line_stripped.startswith("Errors:"):
                try:
                    error_count = int(line_stripped.split(":")[1].strip())
                    if error_count > 0:
                        error_count -= 1
                        filtered_lines[errors_line_index] = f"Errors: {error_count}"
                except:
                    pass

        # 如果没有找到验证结果标记，尝试策略2：只保留问题信息
        if not filtered_lines:
            for line in all_lines:
                line_stripped = line.strip()

                # 检查是否是需要过滤的特定错误
                is_filtered_error = False
                if "ERROR:" in line_stripped and "has duplicates" in line_stripped:
                    is_filtered_error = True
                    duplicate_error_found = True
                    removed_count += 1

                if not is_filtered_error:
                    # 只保留错误、警告、信息行
                    if (line_stripped.startswith("ERROR:") or
                        line_stripped.startswith("WARNING:") or
                        line_stripped.startswith("INFO:") or
                        line_stripped.startswith("Issues:") or
                        line_stripped.startswith("-------") or
                        "Errors:" in line_stripped or
                        "Warnings:" in line_stripped or
                        "Info:" in line_stripped):
                            filtered_lines.append(line)
                    else:
                        removed_count += 1

            # 如果发现了重复包错误，更新计数（策略2）
            if duplicate_error_found:
                for i, line in enumerate(filtered_lines):
                    line_stripped = line.strip()
                    if line_stripped.startswith("Errors:"):
                        try:
                            error_count = int(line_stripped.split(":")[1].strip())
                            if error_count > 0:
                                error_count -= 1
                                filtered_lines[i] = f"Errors: {error_count}"
                        except:
                            pass

        return filtered_lines, removed_count

    def run_agree_validation(self, state) -> Dict[str, Any]:
        """运行当前 standalone AGREE 验证器"""
        result = {
            "validation_successful": False,
            "has_errors": False,
            "has_warnings": False,
            "errors": [],
            "warnings": [],
            "info": []
        }

        try:
            self._ensure_standalone_validator_ready()
            model_path = state.get("final_model_path")
            if not model_path or not os.path.exists(model_path):
                print("\n错误：无法找到AADL模型文件进行AGREE验证\n")
                return result

            merged_aadl = state.get("merged_aadl", "")
            if not merged_aadl:
                print("\n错误：无法找到合并后的AADL内容进行AGREE验证\n")
                return result

            print("\n===== AGREE 语法验证 =====\n")
            with tempfile.TemporaryDirectory(prefix="agree_cli_") as workspace_dir:
                temp_project = self._build_temp_agree_project(model_path, merged_aadl, workspace_dir, state)
                output_json = os.path.join(workspace_dir, "agree_validation_result.json")

                cmd = [
                    self.java_path,
                    "-cp",
                    self.build_agree_validator_classpath(),
                    self.standalone_validator_main,
                    "--workspace",
                    temp_project["workspace_dir"],
                    "--project",
                    temp_project["project_dir"],
                    "--osate-home",
                    self.osate_path,
                    "--output",
                    output_json,
                    "--focus-file",
                    "modified_model.aadl",
                ]

                print("正在执行 standalone AGREE 验证器...")
                proc = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace"
                )

                stdout = proc.stdout.strip()
                stderr = proc.stderr.strip()
                if stderr:
                    print("AGREE 验证器标准错误输出：")
                    print(stderr)

                if not os.path.exists(output_json):
                    raise RuntimeError(
                        "standalone AGREE 验证器未生成结果文件\n"
                        f"stdout:\n{stdout}\n\nstderr:\n{stderr}"
                    )

                with open(output_json, "r", encoding="utf-8") as f:
                    payload = json.load(f)

                issues = payload.get("issues", [])
                errors = []
                warnings = []
                info_msgs = []
                for issue in issues:
                    formatted_issue = self._format_standalone_issue(issue)
                    severity = str(issue.get("severity", "")).lower()
                    if severity == "error":
                        errors.append(formatted_issue)
                    elif severity == "warning":
                        warnings.append(formatted_issue)
                    elif severity == "info":
                        info_msgs.append(formatted_issue)

                result["validation_successful"] = True
                result["has_errors"] = len(errors) > 0
                result["has_warnings"] = len(warnings) > 0
                result["errors"] = errors
                result["warnings"] = warnings
                result["info"] = info_msgs
                result["raw_output"] = json.dumps(payload, ensure_ascii=False, indent=2)

                print("===== AGREE 验证结果 =====\n")
                if stdout:
                    print("AGREE 验证器标准输出：")
                    print(stdout)
                    print()

                if not result["has_errors"] and not result["has_warnings"]:
                    print("AGREE 验证通过，无错误和警告\n")
                else:
                    if result["has_errors"]:
                        print(f"发现 {len(result['errors'])} 个AGREE错误：")
                        for i, err in enumerate(result["errors"], 1):
                            print(f"  [AGREE错误 {i}]: {err}")
                        print()
                    if result["has_warnings"]:
                        print(f"发现 {len(result['warnings'])} 个AGREE警告：")
                        for i, warn in enumerate(result["warnings"], 1):
                            print(f"  [AGREE警告 {i}]: {warn}")
                        print()

        except Exception as e:
            print(f"运行AGREE验证器时发生错误: {str(e)}\n")
            import traceback
            traceback.print_exc()
            result["errors"].append(f"AGREE验证器执行错误: {str(e)}")

        state["agree_validation_result"] = result
        return result

    def run_dual_validation(self, state):
        """运行双重验证：AADL Inspector + AGREE Validator"""
        print("\n" + "=" * 70)
        print("开始双重验证流程")
        print("=" * 70)

        # 运行 AADL Inspector
        print("\n[步骤 1/2] 运行 AADL Inspector...")
        inspection_result = self.run_aadl_validation_inspection(
            state,
            inspector_exe=state.get("inspector_exe"),
            report_dir=state.get("report_dir")
        )

        # 运行 AGREE Validator
        print("\n[步骤 2/2] 运行 AGREE 语法验证器...")
        agree_result = self.run_agree_validation(state)

        # 汇总错误
        all_errors = []
        all_warnings = []

        # 添加 AADL Inspector 错误（带前缀）
        for err in inspection_result.get("errors", []):
            all_errors.append(f"[AADL Inspector] {err}")

        # 添加 AGREE Validator 错误（带前缀）
        for err in agree_result.get("errors", []):
            # 跳过 AGREE 验证器本身的编译错误
            if "Unresolved compilation problem" not in err:
                all_errors.append(f"[AGREE Validator] {err}")

        # 添加警告
        for warn in inspection_result.get("warnings", []):
            all_warnings.append(f"[AADL Inspector] {warn}")
        for warn in agree_result.get("warnings", []):
            all_warnings.append(f"[AGREE Validator] {warn}")

        # 判断错误层级
        aadl_errors = [e for e in all_errors if "[AADL Inspector]" in e]
        agree_errors = [e for e in all_errors if "[AGREE Validator]" in e]

        # 获取AADL Inspector带序号的格式化错误信息（如"错误 1: [行号 75] ..."）
        inspection_formatted_errors = inspection_result.get("formatted_errors_with_index", [])

        error_level_info = {
            "has_aadl_errors": len(aadl_errors) > 0,
            "has_agree_errors": len(agree_errors) > 0,
            "aadl_errors": aadl_errors,
            "agree_errors": agree_errors,
            "all_errors": all_errors,
            "all_warnings": all_warnings,
            # 保存带序号的格式化错误信息（优先使用这个传给LLM）
            "inspection_formatted_errors": inspection_formatted_errors,
            # 需求2：保存原始完整输出
            "agree_raw_output": agree_result.get("raw_output", ""),
            "inspection_raw_output": inspection_result.get("report_content", "")
        }

        # 输出错误层级判断信息
        print("\n" + "=" * 70)
        print("错误层级判断")
        print("=" * 70)

        if error_level_info["has_aadl_errors"]:
            print(f"\n检测到AADL层级语法错误（共{len(aadl_errors)}个），接下来调用AADL修复智能体进行修复")
        if error_level_info["has_agree_errors"]:
            print(f"\n检测到AGREE层级语法错误（共{len(agree_errors)}个），接下来调用AGREE修复智能体进行修复")

        if not error_level_info["has_aadl_errors"] and not error_level_info["has_agree_errors"]:
            print("\n未检测到任何语法错误，验证通过！")

        print()

        return {
            "inspection_result": inspection_result,
            "agree_result": agree_result,
            "error_level_info": error_level_info
        }

    # ==================== Agent 协作流水线 ====================
    def run_full_pipeline(self, aadl_model: str, user_requirements: str, target_component: Optional[str] = None, models: Optional[Dict] = None, case_num: str = '01', case_letter: str = 'A') -> Dict[str, Any]:
        """
        执行完整的AADL+AGREE形式化验证流水线
        
        Args:
            aadl_model: AADL模型代码
            user_requirements: 用户需求描述     
            target_component: 可选的目标组件名称，用于指定AGREE附件插入的位置
            
        Returns:
            执行结果字典
        """
        # 记录开始时间
        start_time = time.time()
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_tokens = 0

        def record_early_failure(stage: str, message: str, initial_code: str = "", fixed_code: str = "") -> None:
            try:
                recorder = create_recorder()
                recorder.result_dir = self.result_root
                recorder.generate_failure_report(
                    case_num,
                    case_letter,
                    stage,
                    message,
                    {
                        "prompt_tokens": self.total_prompt_tokens,
                        "completion_tokens": self.total_completion_tokens,
                        "total_tokens": self.total_tokens,
                    },
                    time.time() - start_time,
                    initial_code,
                    fixed_code,
                )
                print(f"[实验记录] 已生成失败报告: {stage}")
            except Exception as report_error:
                logger.error(f"生成失败报告失败: {report_error}")
        
        print("=" * 70)
        print("开始执行基于多Agent协作的 AADL+AGREE 形式化验证流水线")
        print("=" * 70)

        # 如果提供了目标组件，打印信息
        if target_component:
            print(f"使用指定的目标组件: {target_component}")

        # 重置状态
        self.state = {}

        # 保存Case编号和字母到状态
        self.state['case_num'] = case_num
        self.state['case_letter'] = case_letter

        # 存储所有相关的AADL模型到状态中
        if models:
            self.state['all_models'] = models
            print(f"已存储 {len(models.get('references', [])) + 1} 个AADL模型到状态中")
        
        # 存储用户需求到状态中
        self.state['user_requirements'] = user_requirements
        print(f"已存储用户需求到状态中")
        
        # 初始化对话对象（如果还没有初始化）    
        if not hasattr(self, 'conversation'):
            self.conversation = Conversation()  

        # 确保所有Agent已经初始化
        if not hasattr(self, 'model_analyst_agent'):
            self.model_analyst_agent = AADLModelAnalystAgent(self)
        if not hasattr(self, 'req_analyst_agent'):
            self.req_analyst_agent = RequirementsAnalystAgent(self)
        if not hasattr(self, 'agree_generator_agent'):
            self.agree_generator_agent = AGREEGeneratorAgent(self)
        if not hasattr(self, 'aadl_merge_agent'):
            self.aadl_merge_agent = AADLMergeAgent(self)
        if not hasattr(self, 'aadl_validator_agent'):
            self.aadl_validator_agent = AADLValidatorAgent(self)

        # 设置共享的对话对象
        self.model_analyst_agent.set_conversation(self.conversation)
        self.req_analyst_agent.set_conversation(self.conversation)
        self.agree_generator_agent.set_conversation(self.conversation)
        self.aadl_merge_agent.set_conversation(self.conversation)
        self.aadl_validator_agent.set_conversation(self.conversation)

        # 使用AADL模型分析Agent解析模型
        print("AADL模型分析Agent 开始工作...")  
        result1 = self.model_analyst_agent.analyze_model_structure(aadl_model)
        if not result1["success"]:
            print(f"初始步骤失败: {result1.get('error', '未知错误')}")
            record_early_failure("model_analysis", result1.get('error', '未知错误'))
            return {
                "success": False,
                "error": "AADL 模型解析失败",   
                "details": result1.get('error', '')
            }

        # 不需要将模型解析结果添加到对话历史，避免重复输出

        try:
            # 1. 需求分析师 Agent 处理
            print("需求分析师 Agent 开始工作...")
            req_result = self.req_analyst_agent.parse_requirements(user_requirements)
            if not req_result["success"]:       
                print(f"需求分析失败: {req_result.get('error', '未知错误')}")
                record_early_failure("requirements_analysis", req_result.get('error', '未知错误'))
                return {
                    "success": False,
                    "error": "需求分析失败",    
                    "details": req_result.get('error', '')
                }

            # 2. AGREE 生成器 Agent 处理        
            print("AGREE 生成器 Agent 开始工作...")
            # 获取目标组件（传递指定的目标组件参数）
            target_component = self._infer_target_component(target_component)
            if not target_component:
                print("无法推断目标组件")       
                record_early_failure("target_component_inference", "无法推断目标组件")
                return {
                    "success": False,
                    "error": "无法推断目标组件" 
                }

            agree_result = self.agree_generator_agent.generate_spec(target_component)
            if not agree_result["success"]:     
                print(f"AGREE 规范生成失败: {agree_result.get('error', '未知错误')}")
                record_early_failure("agree_generation", agree_result.get('error', '未知错误'))
                return {
                    "success": False,
                    "error": "AGREE 规范生成失败",
                    "details": agree_result.get('error', '')
                }

            # 3. AADL 融合 Agent 处理
            print("AADL 融合 Agent 开始工作...")
            merge_result = self.aadl_merge_agent.merge_spec_into_model(target_component)        
            if not merge_result["success"]:     
                print(f"融合失败: {merge_result.get('error', '未知错误')}")
                record_early_failure("aadl_merge", merge_result.get('error', '未知错误'))
                return {
                    "success": False,
                    "error": "AADL 融合失败",   
                    "details": merge_result.get('error', '')
                }

            # 4. 融合后立即运行双重验证（AADL Inspector + AGREE Validator）
            print("融合完成，立即运行双重验证...")
            # 保存融合后的代码到文件
            output_file_path = os.path.abspath(os.environ.get("AGREE_WORK_MODEL", "modified_model.aadl"))
            try:
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    f.write(merge_result['result'])
                    # 需求3：确保文件写入完成并刷新到磁盘
                    f.flush()
                    os.fsync(f.fileno())
                    self.state["final_model_path"] = output_file_path
                    self.state["merged_aadl"] = merge_result['result']
            except Exception as e:
                print(f"保存文件失败: {str(e)}")

            # 生成输出目录：Result/CaseXX_X/
            case_str = f"Case{case_num}"
            case_output_dir = os.path.join(self.result_root, f"{case_str}_{case_letter}")
            os.makedirs(case_output_dir, exist_ok=True)

            # 需要一个临时文件用于验证器读取
            temp_output_file = output_file_path
            with open(temp_output_file, 'w', encoding='utf-8') as f:
                f.write(merge_result['result'])
                f.flush()
                os.fsync(f.fileno())

            # 更新final_model_path为临时文件路径
            self.state["final_model_path"] = temp_output_file

            # ===== 实验记录：保存初始代码 =====
            recorder = create_recorder()
            recorder.result_dir = self.result_root
            initial_code = merge_result['result']
            recorder.save_initial_code(case_num, case_letter, initial_code)
            print(f"\n[实验记录] 已保存初始代码")

            # 运行双重验证
            dual_result = self.run_dual_validation(self.state)
            error_info = dual_result.get("error_level_info", {})

            # 提取AADL和AGREE错误（初始错误，用于报告统计）
            initial_aadl_errors = error_info.get("aadl_errors", [])
            initial_agree_errors = error_info.get("agree_errors", [])

            # 保存初始错误
            recorder.save_errors(case_num, case_letter, initial_aadl_errors, initial_agree_errors)
            print(f"[实验记录] 已保存初始错误信息")

            # 检查验证结果，根据错误层级决定修复流程
            has_errors = error_info.get("has_aadl_errors", False) or error_info.get("has_agree_errors", False)

            # 初始化变量。即使后续修复器拒绝了无效输出，也要保留首次验证结果，
            # 这样流程可以生成失败报告，而不是在收尾阶段因 None 崩溃。
            repair_count = 0
            final_dual_result = dual_result

            if has_errors:
                print("发现验证错误，启动自动修复流程...")
                # 调用验证Agent进行修复（传入错误层级信息）
                validate_result = self.aadl_validator_agent.validate_and_fix(
                    error_level_info=error_info
                )
                if validate_result.get("success", False):
                    # 获取修复后的模型
                    fixed_model = validate_result.get("result", "")
                    repair_count = validate_result.get("repair_count", 0)
                    final_dual_result = validate_result.get("final_dual_result")
                    if fixed_model:
                        # 更新状态
                        self.state["merged_aadl"] = fixed_model
                        print(f"\n修复完成，修复次数: {repair_count}，修复后的模型将保存到 Report 文件夹")
                else:
                    print(f"自动修复失败: {validate_result.get('error', '未知错误')}")
                    final_dual_result = validate_result.get("final_dual_result") or final_dual_result
            else:
                print("双重验证通过，无需修复")
                # 没有错误时，使用第一次的验证结果
                final_dual_result = dual_result

            # 最终验证和结果汇总
            final_model = self.state.get("merged_aadl", merge_result.get('result', ''))

            # 注意：Result 文件夹只保存首次生成的初始代码
            # 修复后的代码仅保存到 Report 文件夹

            # ===== 实验记录：保存修复后的代码并生成报告 =====
            recorder.save_fixed_code(case_num, case_letter, final_model)
            print(f"[实验记录] 已保存修复后的代码")

            # 计算token使用统计
            token_stats = {
                "prompt_tokens": self.total_prompt_tokens,
                "completion_tokens": self.total_completion_tokens,
                "total_tokens": self.total_tokens
            }

            # 计算运行时间
            end_time = time.time()
            runtime = end_time - start_time

            # 使用已有的验证结果，不再重复运行
            final_error_info = final_dual_result.get("error_level_info", {})
            final_aadl_errors = final_error_info.get("aadl_errors", [])
            final_agree_errors = final_error_info.get("agree_errors", [])
            final_success = not (final_error_info.get("has_aadl_errors", False) or final_error_info.get("has_agree_errors", False))

            # 生成完整实验报告（传入修复次数）
            # 错误类型统计必须基于首次生成代码的初始错误，而不是最终修复后的错误
            report_data = recorder.generate_report(
                case_num, case_letter,
                initial_code, final_model,
                initial_aadl_errors, initial_agree_errors,
                token_stats, runtime, final_success,
                repair_count=repair_count
            )
            print(f"[实验记录] 已生成实验报告")

            print("=" * 70)
            print("基于多Agent协作的 AADL+AGREE 形式化验证流水线执行完成")
            print("=" * 70)
            print(f"Token使用统计: {token_stats}")
            print(f"运行时间: {runtime:.2f} 秒")
            print(f"修复迭代次数: {repair_count} 次")

            return {
                "success": True,
                "final_model": final_model,
                "token_stats": token_stats,
                "dual_validation_result": final_dual_result,
                "runtime": runtime,
                "report_data": report_data,
                "repair_count": repair_count
            }
        except Exception as e:
            # 计算运行时间
            end_time = time.time()
            runtime = end_time - start_time
            
            print(f"执行流水线时发生异常: {str(e)}")
            import traceback
            traceback.print_exc()
            print(f"运行时间: {runtime:.2f} 秒")
            
            return {
                "success": False,
                "error": f"执行异常: {str(e)}",
                "runtime": runtime
            }


# ==================== 主函数 ====================
