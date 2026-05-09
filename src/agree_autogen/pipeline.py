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
    AGREE 
    
      -  PDF/TXT  @@@...@@@  AGREE 
      -  + 
      -  AADL JSON 
      - AgentAGREEAADL
    """

    def __init__(self, docs_directory: str, force_rebuild: bool = False, use_rag: bool = True):
        self.docs_directory = docs_directory
        self.force_rebuild = force_rebuild
        self.use_rag = use_rag  # RAG
        self.state = {}  # 
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        self.total_tokens = 0

        self.chunk_size_gen = 512  #  chunk
        self.chunk_size_val = 512   #  chunk 
        self.chunk_overlap = 50
        self.top_k = 8
        self.embedding_model = "BAAI/bge-base-en-v1.5"
        self.collection_name_gen = "agree-unified-generate-v3"
        self.collection_name_val = "agree-code-v3"
        self.vectorstore_dir = "./vectorstore_cache"

        self.llm_api_key = runtime.MODEL_API_KEY
        self.llm_base_url = runtime.MODEL_BASE_URL
        self.llm_model_name = runtime.MODEL_NAME
        self.result_root = runtime.RESULT_ROOT
        self.client = OpenAI(api_key=self.llm_api_key, base_url=self.llm_base_url)

        self.osate_path = os.environ.get("OSATE_HOME", "")
        self.standalone_validator_root = os.environ.get("AGREE_VALIDATOR_ROOT", os.path.abspath("tools/agree-validator"))
        self.standalone_validator_out = os.path.join(self.standalone_validator_root, "out")
        self.standalone_validator_main = "org.agreeautogen.validator.AgreeValidationCli"
        self.standalone_java_home = os.environ.get("JAVA_HOME", "")
        self.static_libs_dir = os.path.join(self.standalone_validator_root, "static-libs")
        self._dependency_catalog = None

        preferred_java = os.path.join(self.standalone_java_home, "bin", "java.exe") if self.standalone_java_home else ""
        self.java_path = preferred_java if os.path.exists(preferred_java) else "java"

        self._initialize_vectorstore_gen()
        self._initialize_vectorstore_val()
        logger.info("AGREE verification pipeline initialized")
        
        self.analyst_agent = RequirementsAnalystAgent(self)
        self.generator_agent = AGREEGeneratorAgent(self)
        self.validator_agent = AADLValidatorAgent(self)
        
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
                print(f"Copied dependency model: {format_file_link(target_path)}")
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
        """Load a PDF or text document for RAG indexing."""
        documents = []
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Document file not found: {file_path}")

        if file_path.lower().endswith(".pdf"):
            logger.info(f" PDF : {path.name}")
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
            logger.info(f" TXT : {path.name}")
            with open(file_path, 'r', encoding='utf-8') as f:
                full_text = f.read()
            file_hash = hashlib.md5(full_text.encode('utf-8')).hexdigest()
            agree_code_blocks = re.findall(r"@@@\s*(.*?)\s*@@@", full_text, re.DOTALL)

            if agree_code_blocks:
                for idx, code in enumerate(agree_code_blocks, start=1):
                    code = code.strip()
                    if not code:
                        return {
                            "success": False,
                            "error": "",
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
                logger.warning(f"TXT  @@@ ")

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
        logger.info("Deduplicated documents: %s input chunks, %s unique chunks", len(documents), len(unique_docs))
        return unique_docs

    def _load_all_documents(self) -> List[Document]:
        all_docs = []
        directory_path = Path(self.docs_directory)
        if not directory_path.exists():
            raise FileNotFoundError(f"RAG document directory not found: {self.docs_directory}")

        target_files = list(directory_path.glob("*.pdf")) + list(directory_path.glob("*.txt"))
        if not target_files:
            raise FileNotFoundError(f"No PDF or TXT documents found in RAG directory: {self.docs_directory}")

        for file_path in target_files:
            try:
                docs = self._load_document(str(file_path))
                all_docs.extend(docs)
                logger.info("Loaded RAG document %s with %s chunks", file_path.name, len(docs))
            except Exception as e:
                logger.error("Failed to load RAG document %s: %s", file_path, e)

        return self._deduplicate_documents(all_docs)

    def _initialize_vectorstore_gen(self):
        """"""
        embedder = HuggingFaceEmbeddings(
            model_name=self.embedding_model,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )

        vectorstore_gen_path = os.path.join(self.vectorstore_dir, self.collection_name_gen)
        if os.path.exists(vectorstore_gen_path) and not self.force_rebuild:
            logger.info("...")
            self.vectorstore_gen = Chroma(
                persist_directory=vectorstore_gen_path,
                embedding_function=embedder,
                collection_name=self.collection_name_gen
            )
        else:
            logger.info("...")
            raw_docs = self._load_all_documents()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size_gen,
                chunk_overlap=self.chunk_overlap,
                separators=["\n\n### ", "\n\n#### ", "\n\n", r"(?<=\.)\s+", "\n", ";", "", "", " "]
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
        """"""
        embedder = HuggingFaceEmbeddings(
            model_name=self.embedding_model,
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )

        vectorstore_val_path = os.path.join(self.vectorstore_dir, self.collection_name_val)
        if os.path.exists(vectorstore_val_path) and not self.force_rebuild:
            logger.info("...")
            self.vectorstore_val = Chroma(
                persist_directory=vectorstore_val_path,
                embedding_function=embedder,
                collection_name=self.collection_name_val
            )
        else:
            logger.info("...")
            raw_docs = self._load_all_documents()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.chunk_size_val,
                chunk_overlap=self.chunk_overlap,
                separators=["\n\n### ", "\n\n#### ", "\n\n", r"(?<=\.)\s+", "\n", ";", "", "", " "]
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
        """
        Augment a prompt with retrieved RAG context when RAG is enabled.
        """
        if not self.use_rag:
            logger.info("[RAG] disabled")
            return query
            
        vectorstore = self.vectorstore_gen if mode == "generate" else self.vectorstore_val
        
        if mode == "validate":
            k_value = 5
            
            enhanced_query = query
            if "unexpected keyword" in query or "parsing" in query:
                enhanced_query = query + " AADL  AGREE"
            
            results = vectorstore.similarity_search(enhanced_query, k=k_value)
        elif mode == "generate":
            results = vectorstore.similarity_search(query, k=15)
        else:
            results = vectorstore.similarity_search(query, k=self.top_k)
        
        source_knowledge = ""
        for r in results:
            source = r.metadata.get("source", "unknown")
            doc_type = r.metadata.get("type", "N/A")
            source_knowledge += (
                f"Source: {Path(source).name} | Type: {doc_type}\n"
                f"{r.page_content}\n\n"
            )
        
        if mode == "validate":
            augmented_prompt = f"""
AADL


- 
- 
- AGREE_knowledge_dataset
- AADL


{source_knowledge}


{query}
"""
        else:
            augmented_prompt = f"""



{source_knowledge}


{query}
"""
        
        return augmented_prompt

    def _infer_target_component(self, target_component: Optional[str] = None) -> Optional[str]:
        """
        
        
        Args:
            target_component: 
            
        Returns:
            None
        """
        if target_component:
            print(f"Using specified target component: {target_component}")
            return target_component
            
        print("\nInferring target component for AGREE generation...")
        
        components = self.state.get('aadl_analysis', {}).get('components', [])
        if not isinstance(components, list) or not components:
            print("No components available for target inference")
            return None

        for comp in components:
            if isinstance(comp, dict) and comp.get('type') == 'system_implementation' and comp.get('name'):
                print(f"Inferred target implementation: {comp['name']}")
                return comp['name']

        for comp in components:
            if isinstance(comp, dict) and comp.get('type') == 'system' and comp.get('name'):
                print(f"Inferred target component type: {comp['name']}")
                return comp['name']

        first_comp = components[0]
        if isinstance(first_comp, dict) and 'name' in first_comp:
            print(f"Using first component candidate: {first_comp['name']}")
            return first_comp['name']

        print("Unable to infer target component")
        return None


    def run_aadl_validation_inspection(self, state, inspector_exe=None, report_dir=None):
        """Run AADL Inspector on the current generated model."""
        result = {
            "inspection_successful": False,
            "has_errors": False,
            "has_warnings": False,
            "errors": [],
            "warnings": [],
            "report_path": None
        }
        
        try:
            model_path = state.get("final_model_path")
            if not model_path or not os.path.exists(model_path):
                print("\nAADL\n")
                return result
            
            if not inspector_exe:
                inspector_exe = os.environ.get("AADL_INSPECTOR_PATH", "AADLInspector")
            
            if not report_dir:
                report_dir = os.environ.get("AADL_REPORT_DIR", 
                                          os.path.dirname(model_path))
            
            os.makedirs(report_dir, exist_ok=True)
            
            print("\n===== AADL  =====\n")

            case_num = state.get('case_num')
            case_letter = state.get('case_letter')

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


            sources_case_dir = os.path.join(os.environ.get("AGREE_SOURCE_ROOT", os.path.abspath("data/Sources")), case_dir)
            original_aadl = os.path.join(sources_case_dir, f"{case_str}_Base.aadl")

            try:
                with open(model_path, 'r', encoding='utf-8') as f_src:
                    content = f_src.read()
                with open(original_aadl, 'w', encoding='utf-8') as f_dst:
                    f_dst.write(content)
            except Exception as e:
                print(f"Warning: failed to copy generated model into source case directory: {e}")

            main_aadl = original_aadl

            project_root = os.path.join(sources_case_dir, case_str)

            sources_report_dir = os.path.join(sources_case_dir, "Report")
            os.makedirs(sources_report_dir, exist_ok=True)
            sources_result_file = os.path.join(sources_report_dir, f"{case_str}_report.txt")

            result_report_dir = os.path.join(self.result_root, case_dir, "Report")
            os.makedirs(result_report_dir, exist_ok=True)
            result_file = os.path.join(result_report_dir, f"{case_str}_report.txt")

            temp_aic = os.path.join(sources_case_dir, "temp_project.aic")

            aadl_files = [main_aadl]
            if os.path.exists(project_root):
                for root, dirs, files in os.walk(project_root):
                    for file in files:
                        if file.endswith(".aadl"):
                            aadl_files.append(os.path.join(root, file))

            with open(temp_aic, 'w', encoding='utf-8') as f:
                for path in aadl_files:
                    f.write(f"{path}\n")

            inspector_command = f'"{inspector_exe}" -a "{temp_aic}" --plugin Static.parse --result "{sources_result_file}" --show false --aadlVersion V2'
            print(f"AADL Inspector command: {inspector_command}\n")

            stop_event = threading.Event()
            monitor_thread = None
            if HAS_WIN32:
                monitor_thread = start_window_monitor(stop_event)
                print("Started AADL Inspector pop-up monitor")

            try:
                proc = subprocess.run(inspector_command, shell=True, timeout=120)
            except Exception as e:
                print(f"AADL Inspector : {str(e)}")
                proc = None
            finally:
                stop_event.set()
                if monitor_thread:
                    monitor_thread.join(timeout=1.0)

            print(f"AADL Inspector ")
            print(f"AADL Inspector report path: {result_file}\n")

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

            if report_to_read and os.path.exists(report_to_read):
                encodings = ['utf-8', 'utf-16', 'latin-1']
                report_content = ""
                for encoding in encodings:
                    try:
                        with open(report_to_read, 'r', encoding=encoding) as f:
                            report_content = f.read()
                        break  # 
                    except UnicodeDecodeError:
                        continue

                if not report_content:
                    with open(report_to_read, 'rb') as f:
                        binary_content = f.read()
                    report_content = binary_content.decode('latin-1')

                success_markers = ["Model parsed successfully", "", ""]
                is_success = any(marker in report_content for marker in success_markers)

                error_markers = [
                    "cannot parse", "parsing error", "syntax error",
                    "parsing AADL_Declaration", "unexpected identifier",
                    "unexpected keyword", "", ""
                ]
                has_errors = False
                errors = []

                error_patterns = re.findall(r'\$\{sbpText\}\.text fastinsert end (\d+) d\d+.*?TextEditor::fastaddText \$sbpText "(.*?)"', report_content, re.DOTALL)

                line_error_map = {}
                for line_num, error_text in error_patterns:
                    error_text = error_text.strip()
                    if error_text and not any(ignore in error_text.lower() for ignore in ["set lines(error)", "<any-"]):
                        line_error_map[line_num] = error_text

                error_lines = re.findall(r'lappend lines\(error\) (\d+)', report_content)
                for line_num in error_lines:
                    if line_num not in line_error_map:
                        pass

                for line_num, error_text in sorted(line_error_map.items(), key=lambda x: int(x[0])):
                    errors.append(f"[ {line_num}] {error_text}")

                if not errors:
                    text_editor_errors = re.findall(r'TextEditor::fastaddText \$sbpText "(.*?)"', report_content, re.DOTALL)
                    for error_text in text_editor_errors:
                        error_text = error_text.strip()
                        if error_text and not any(ignore in error_text.lower() for ignore in ["set lines(error)", "<any-"]):
                            errors.append(error_text)

                if not errors:
                    for marker in error_markers:
                        if marker.lower() in report_content.lower():
                            has_errors = True
                            context_pattern = r'((?:\w+\s*:\s*)?.*?' + re.escape(marker) + r'.*?)(?:\n|$)'
                            context_matches = re.findall(context_pattern, report_content, re.IGNORECASE)
                            for match in context_matches[:5]:  # 
                                errors.append(match.strip())
                else:
                    has_errors = True

                warning_markers = ["warning", " "]
                has_warnings = any(marker in report_content.lower() for marker in warning_markers)

                result["report_content"] = report_content
                result["has_errors"] = has_errors
                result["has_warnings"] = has_warnings
                result["inspection_successful"] = True  # 
                result["inspection_report_path"] = report_to_read
                result["errors"] = list(set(errors))  # 

                print("=====  =====\n")
                formatted_errors_with_index = []  # " 1: [ 75] ..."
                if is_success:
                    print("\n")
                elif has_errors and errors:
                    print(f" {len(result['errors'])} \n")
                    for i, error in enumerate(result['errors'], 1):
                        formatted_error = f" {i}: {error}"
                        print(f"  {formatted_error}")
                        print()  # 
                        formatted_errors_with_index.append(formatted_error)
                elif has_errors:
                    print("\n")
                else:
                    print("\n")
                    if len(report_content.strip()) < 100 or "parsing" in report_content.lower():
                        print("\nAADL Inspector report appears incomplete or parser-related")
                        result["has_errors"] = True
                        result["errors"].append("AADL Inspector report appears incomplete or parser-related")

                result["formatted_errors_with_index"] = formatted_errors_with_index
            else:
                print(f"AADL Inspector report not found: {result_file} or {sources_result_file}\n")
                result["errors"].append(f"AADL Inspector report not found: {result_file}")
                if proc is not None:
                    result["errors"].append(f"AADL Inspector : {proc.returncode}")

        except Exception as e:
            print(f"AADL Inspector: {str(e)}\n")
            import traceback
            traceback.print_exc()
            result["errors"].append(f"AADL Inspector exception: {str(e)}")

        if os.path.exists(temp_aic):
            try:
                os.remove(temp_aic)
            except Exception as e:
                pass
        # if os.path.exists(sources_result_file):
        #     try:
        #         os.remove(sources_result_file)
        #     except Exception as e:
        #         pass

        state["inspection_result"] = result
        return result

    def build_agree_validator_classpath(self) -> str:
        """ standalone AGREE  classpath"""
        return os.pathsep.join([
            self.standalone_validator_out,
            os.path.join(self.osate_path, "plugins", "*")
        ])

    def _ensure_standalone_validator_ready(self) -> None:
        if not os.path.isdir(self.standalone_validator_root):
            raise FileNotFoundError(f"Standalone validator root not found: {self.standalone_validator_root}")
        if not os.path.isdir(self.standalone_validator_out):
            raise FileNotFoundError(
                f"Standalone validator output directory not found: {self.standalone_validator_out}. Build the validator first."
            )
        if not os.path.isdir(os.path.join(self.osate_path, "plugins")):
            raise FileNotFoundError(f"OSATE plugins directory not found under OSATE_HOME: {self.osate_path}")

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
            location_parts.append(f" {line_no}")

        if location_parts:
            return f"[{' | '.join(location_parts)}] {message}"
        return message

    def filter_java_output(self, stdout, stderr):
        """
         Java 

         "AGREE Validation Results" 
              "Package ... has duplicates" 
        """
        filtered_lines = []
        removed_count = 0
        duplicate_error_found = False
        errors_line_index = -1

        all_lines = []
        if stdout:
            all_lines.extend(stdout.splitlines())
        if stderr:
            all_lines.extend(stderr.splitlines())

        found_results = False
        for i, line in enumerate(all_lines):
            line_stripped = line.strip()

            if "AGREE Validation Results" in line_stripped:
                found_results = True

            if found_results:
                is_filtered_error = False

                if "ERROR:" in line_stripped and "has duplicates" in line_stripped:
                    is_filtered_error = True
                    duplicate_error_found = True
                    removed_count += 1

                if line_stripped.startswith("Errors:"):
                    errors_line_index = len(filtered_lines)

                if not is_filtered_error:
                    filtered_lines.append(line)
            else:
                removed_count += 1

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

        if not filtered_lines:
            for line in all_lines:
                line_stripped = line.strip()

                is_filtered_error = False
                if "ERROR:" in line_stripped and "has duplicates" in line_stripped:
                    is_filtered_error = True
                    duplicate_error_found = True
                    removed_count += 1

                if not is_filtered_error:
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
        """ standalone AGREE """
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
                print("\nAADLAGREE\n")
                return result

            merged_aadl = state.get("merged_aadl", "")
            if not merged_aadl:
                print("\nAADLAGREE\n")
                return result

            print("\n===== AGREE  =====\n")
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

                print(" standalone AGREE ...")
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
                    print("AGREE ")
                    print(stderr)

                if not os.path.exists(output_json):
                    raise RuntimeError(
                        "standalone AGREE \n"
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

                print("===== AGREE  =====\n")
                if stdout:
                    print("AGREE ")
                    print(stdout)
                    print()

                if not result["has_errors"] and not result["has_warnings"]:
                    print("AGREE \n")
                else:
                    if result["has_errors"]:
                        print(f" {len(result['errors'])} AGREE")
                        for i, err in enumerate(result["errors"], 1):
                            print(f"  [AGREE {i}]: {err}")
                        print()
                    if result["has_warnings"]:
                        print(f" {len(result['warnings'])} AGREE")
                        for i, warn in enumerate(result["warnings"], 1):
                            print(f"  [AGREE {i}]: {warn}")
                        print()

        except Exception as e:
            print(f"AGREE: {str(e)}\n")
            import traceback
            traceback.print_exc()
            result["errors"].append(f"AGREE: {str(e)}")

        state["agree_validation_result"] = result
        return result

    def run_dual_validation(self, state):
        """AADL Inspector + AGREE Validator"""
        print("\n" + "=" * 70)
        print("Dual validation")
        print("=" * 70)

        print("\n[Step 1/2] Running AADL Inspector...")
        inspection_result = self.run_aadl_validation_inspection(
            state,
            inspector_exe=state.get("inspector_exe"),
            report_dir=state.get("report_dir")
        )

        print("\n[Step 2/2] Running standalone AGREE validator...")
        agree_result = self.run_agree_validation(state)

        all_errors = []
        all_warnings = []

        for err in inspection_result.get("errors", []):
            all_errors.append(f"[AADL Inspector] {err}")

        for err in agree_result.get("errors", []):
            if "Unresolved compilation problem" not in err:
                all_errors.append(f"[AGREE Validator] {err}")

        for warn in inspection_result.get("warnings", []):
            all_warnings.append(f"[AADL Inspector] {warn}")
        for warn in agree_result.get("warnings", []):
            all_warnings.append(f"[AGREE Validator] {warn}")

        aadl_errors = [e for e in all_errors if "[AADL Inspector]" in e]
        agree_errors = [e for e in all_errors if "[AGREE Validator]" in e]

        inspection_formatted_errors = inspection_result.get("formatted_errors_with_index", [])

        error_level_info = {
            "has_aadl_errors": len(aadl_errors) > 0,
            "has_agree_errors": len(agree_errors) > 0,
            "aadl_errors": aadl_errors,
            "agree_errors": agree_errors,
            "all_errors": all_errors,
            "all_warnings": all_warnings,
            "inspection_formatted_errors": inspection_formatted_errors,
            "agree_raw_output": agree_result.get("raw_output", ""),
            "inspection_raw_output": inspection_result.get("report_content", "")
        }

        print("\n" + "=" * 70)
        print("Validation error-level summary")
        print("=" * 70)

        if error_level_info["has_aadl_errors"]:
            print(f"\nAADL{len(aadl_errors)}AADL")
        if error_level_info["has_agree_errors"]:
            print(f"\nAGREE{len(agree_errors)}AGREE")

        if not error_level_info["has_aadl_errors"] and not error_level_info["has_agree_errors"]:
            print("\n")

        print()

        return {
            "inspection_result": inspection_result,
            "agree_result": agree_result,
            "error_level_info": error_level_info
        }

    def run_full_pipeline(self, aadl_model: str, user_requirements: str, target_component: Optional[str] = None, models: Optional[Dict] = None, case_num: str = '01', case_letter: str = 'A') -> Dict[str, Any]:
        """
        AADL+AGREE
        
        Args:
            aadl_model: AADL
            user_requirements:      
            target_component: AGREE
            
        Returns:
            
        """
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
                print(f"Generated failure report for stage: {stage}")
            except Exception as report_error:
                logger.error("Failed to generate failure report: %s", report_error)
        
        print("=" * 70)
        print("Starting Agree-Autogen pipeline")
        print("=" * 70)

        if target_component:
            print(f"Target component: {target_component}")

        self.state = {}

        self.state['case_num'] = case_num
        self.state['case_letter'] = case_letter

        if models:
            self.state['all_models'] = models
            print(f"Loaded {len(models.get('references', [])) + 1} AADL model file(s)")
        
        self.state['user_requirements'] = user_requirements
        print("Stored user requirements")
        
        if not hasattr(self, 'conversation'):
            self.conversation = Conversation()  

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

        self.model_analyst_agent.set_conversation(self.conversation)
        self.req_analyst_agent.set_conversation(self.conversation)
        self.agree_generator_agent.set_conversation(self.conversation)
        self.aadl_merge_agent.set_conversation(self.conversation)
        self.aadl_validator_agent.set_conversation(self.conversation)

        print("Running AADL model analyst agent...")
        result1 = self.model_analyst_agent.analyze_model_structure(aadl_model)
        if not result1["success"]:
            print(f"AADL model analysis failed: {result1.get('error', '')}")
            record_early_failure("model_analysis", result1.get('error', ''))
            return {
                "success": False,
                "error": "AADL model analysis failed",
                "details": result1.get('error', '')
            }


        try:
            print("Running requirement analyst agent...")
            req_result = self.req_analyst_agent.parse_requirements(user_requirements)
            if not req_result["success"]:       
                print(f"Requirement analysis failed: {req_result.get('error', '')}")
                record_early_failure("requirements_analysis", req_result.get('error', ''))
                return {
                    "success": False,
                    "error": "Requirement analysis failed",
                    "details": req_result.get('error', '')
                }

            print("Running AGREE generator agent...")
            target_component = self._infer_target_component(target_component)
            if not target_component:
                print("Target component inference failed")
                record_early_failure("target_component_inference", "Unable to infer target component")
                return {
                    "success": False,
                    "error": "Unable to infer target component"
                }

            agree_result = self.agree_generator_agent.generate_spec(target_component)
            if not agree_result["success"]:     
                print(f"AGREE : {agree_result.get('error', '')}")
                record_early_failure("agree_generation", agree_result.get('error', ''))
                return {
                    "success": False,
                    "error": "AGREE generation failed",
                    "details": agree_result.get('error', '')
                }

            print("Running AADL merge agent...")
            merge_result = self.aadl_merge_agent.merge_spec_into_model(target_component)        
            if not merge_result["success"]:     
                print(f"AADL merge failed: {merge_result.get('error', '')}")
                record_early_failure("aadl_merge", merge_result.get('error', ''))
                return {
                    "success": False,
                    "error": "AADL merge failed",
                    "details": merge_result.get('error', '')
                }

            print("Writing merged AADL model...")
            output_file_path = os.path.abspath(os.environ.get("AGREE_WORK_MODEL", "modified_model.aadl"))
            try:
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    f.write(merge_result['result'])
                    f.flush()
                    os.fsync(f.fileno())
                    self.state["final_model_path"] = output_file_path
                    self.state["merged_aadl"] = merge_result['result']
            except Exception as e:
                print(f"Failed to write merged model: {str(e)}")

            case_str = f"Case{case_num}"
            case_output_dir = os.path.join(self.result_root, f"{case_str}_{case_letter}")
            os.makedirs(case_output_dir, exist_ok=True)

            temp_output_file = output_file_path
            with open(temp_output_file, 'w', encoding='utf-8') as f:
                f.write(merge_result['result'])
                f.flush()
                os.fsync(f.fileno())

            self.state["final_model_path"] = temp_output_file

            recorder = create_recorder()
            recorder.result_dir = self.result_root
            initial_code = merge_result['result']
            recorder.save_initial_code(case_num, case_letter, initial_code)
            print("\nSaved first-pass generated model")

            dual_result = self.run_dual_validation(self.state)
            error_info = dual_result.get("error_level_info", {})

            initial_aadl_errors = error_info.get("aadl_errors", [])
            initial_agree_errors = error_info.get("agree_errors", [])

            recorder.save_errors(case_num, case_letter, initial_aadl_errors, initial_agree_errors)
            print("Saved initial validation errors")

            has_errors = error_info.get("has_aadl_errors", False) or error_info.get("has_agree_errors", False)

            repair_count = 0
            final_dual_result = dual_result

            if has_errors:
                print("Validation errors found; starting repair agent...")
                validate_result = self.aadl_validator_agent.validate_and_fix(
                    error_level_info=error_info
                )
                if validate_result.get("success", False):
                    fixed_model = validate_result.get("result", "")
                    repair_count = validate_result.get("repair_count", 0)
                    final_dual_result = validate_result.get("final_dual_result")
                    if fixed_model:
                        self.state["merged_aadl"] = fixed_model
                        print(f"\nRepair completed after {repair_count} round(s)")
                else:
                    print(f"Repair failed: {validate_result.get('error', '')}")
                    final_dual_result = validate_result.get("final_dual_result") or final_dual_result
            else:
                print("No validation errors found")
                final_dual_result = dual_result

            final_model = self.state.get("merged_aadl", merge_result.get('result', ''))


            recorder.save_fixed_code(case_num, case_letter, final_model)
            print("Saved final model")

            token_stats = {
                "prompt_tokens": self.total_prompt_tokens,
                "completion_tokens": self.total_completion_tokens,
                "total_tokens": self.total_tokens
            }

            end_time = time.time()
            runtime = end_time - start_time

            final_error_info = final_dual_result.get("error_level_info", {})
            final_aadl_errors = final_error_info.get("aadl_errors", [])
            final_agree_errors = final_error_info.get("agree_errors", [])
            final_success = not (final_error_info.get("has_aadl_errors", False) or final_error_info.get("has_agree_errors", False))

            report_data = recorder.generate_report(
                case_num, case_letter,
                initial_code, final_model,
                initial_aadl_errors, initial_agree_errors,
                token_stats, runtime, final_success,
                repair_count=repair_count
            )
            print("Generated experiment report")

            print("=" * 70)
            print("Agree-Autogen pipeline completed")
            print("=" * 70)
            print(f"Token: {token_stats}")
            print(f"Runtime seconds: {runtime:.2f}")
            print(f"Repair rounds: {repair_count}")

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
            end_time = time.time()
            runtime = end_time - start_time
            
            print(f"Pipeline exception: {str(e)}")
            import traceback
            traceback.print_exc()
            print(f"Runtime seconds: {runtime:.2f}")
            
            return {
                "success": False,
                "error": f"Pipeline exception: {str(e)}",
                "runtime": runtime
            }
