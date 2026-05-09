import os
import re
import json
from typing import List, Dict, Optional, Any

from .runtime import logger, normalize_token_usage

class Conversation:
    """
    对话历史管理类，支持多Agent对话
    以[{"role": "analyst", "content": "..."}]格式存储消息
    """
    
    def __init__(self):
        self.messages = []  # 存储对话历史，格式为 [{'role': 'analyst', 'content': '...'}, ...]
    
    def add_message(self, role: str, content: str):
        """
        添加一条消息到对话历史
        
        Args:
            role: 消息发送者角色（analyst/generator/validator/system/user）
            content: 消息内容
        """
        if not role or not content:
            return
        
        self.messages.append({"role": role, "content": content})
        logger.info(f"[{role}] 添加到对话历史")
    
    def format_for_llm(self, system_prompt: str, user_prompt: str) -> List[Dict[str, str]]:
        """
        将对话历史格式化为LLM可接受的格式
        
        Args:
            system_prompt: 系统提示词
            user_prompt: 当前用户提示词
            
        Returns:
            List[Dict]: 格式化后的消息列表
        """
        # 系统消息
        messages = [{"role": "system", "content": system_prompt}]
        
        # 转换历史消息角色
        role_mapping = {
            "analyst": "assistant",
            "generator": "assistant", 
            "validator": "assistant",
            "system": "system",
            "user": "user"
        }
        
        # 添加历史消息
        for msg in self.messages:
            original_role = msg.get("role")
            llm_role = role_mapping.get(original_role, "assistant")
            content = msg.get("content", "")
            
            # 为不同专业领域角色的消息添加标识前缀
            if original_role in ["analyst", "generator", "validator"]:
                # 使用特殊格式标记不同专业领域Agent的输出
                content = f"[专业领域: {original_role.upper()}] {content}"
                
            messages.append({"role": llm_role, "content": content})
        
        # 添加当前用户消息
        messages.append({"role": "user", "content": user_prompt})
        
        return messages

    def __str__(self) -> str:
        """
        返回对话历史的字符串表示
        """
        result = []
        newline = "\n"
        for msg in self.messages:
            content = msg.get('content', '')
            first_line = content.split(newline)[0] if newline in content else content
            result.append(f"[{msg.get('role', 'unknown')}]: {first_line}")
        return "\n".join(result)
    
    def get_history(self) -> List[Dict[str, str]]:
        """
        获取对话历史
        
        Returns:
            List[Dict]: 对话历史消息列表
        """
        return self.messages


class BaseAgent:
    """
    基础Agent类，提供共享功能
    """
    
    def __init__(self, name: str, pipeline):
        self.name = name
        self.pipeline = pipeline
        self.conversation = None
    
    def set_conversation(self, conversation: Conversation):
        """
        设置对话对象
        """
        self.conversation = conversation
    
    def call_llm(self, system_prompt: str, user_prompt: str, temperature: float = 0.2, max_tokens: int = 2000, use_conversation_history: bool = True) -> str:
        """
        调用LLM接口（OpenAI兼容格式）

        Args:
            use_conversation_history: 是否使用对话历史（需求1：修复迭代时设为False）
        """
        try:
            # 打印LLM调用信息
            print("\n=== 调用LLM的完整内容 ===")
            print(f"模型名称: {self.pipeline.llm_model_name}")
            print(f"temperature: {temperature}")
            print(f"max_tokens: {max_tokens}")
            print(f"使用对话历史: {bool(self.conversation) and use_conversation_history}")

            if self.conversation and use_conversation_history:
                # 使用对话历史
                messages = self.conversation.format_for_llm(system_prompt, user_prompt)
                print("\n消息内容:")
                for i, msg in enumerate(messages):
                    print(f"  消息 {i+1}:")
                    print(f"    角色: {msg['role']}")
                    print(f"    内容: {msg['content']}")

                completion = self.pipeline.client.chat.completions.create(
                    model=self.pipeline.llm_model_name,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
            else:
                # 不使用对话历史
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
                print("\n消息内容:")
                print(f"  消息 1:")
                print(f"    角色: system")
                print(f"    内容: {system_prompt}")
                print(f"  消息 2:")
                print(f"    角色: user")
                print(f"    内容: {user_prompt}")

                completion = self.pipeline.client.chat.completions.create(
                    model=self.pipeline.llm_model_name,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

            response = completion.choices[0].message.content.strip()

            token_stats = normalize_token_usage(messages, response, completion.usage)
            prompt_tokens = token_stats["prompt_tokens"]
            completion_tokens = token_stats["completion_tokens"]
            total_tokens = token_stats["total_tokens"]

            self.pipeline.total_prompt_tokens += prompt_tokens
            self.pipeline.total_completion_tokens += completion_tokens
            self.pipeline.total_tokens += total_tokens

            # 打印LLM返回结果
            print("\n=== LLM 返回结果 ===")
            print(f"响应内容: {response}")
            print("\n=== Token 使用统计 ===")
            print(f"提示词token数: {prompt_tokens}")
            print(f"回复token数: {completion_tokens}")
            print(f"总token数: {total_tokens}")
            if token_stats["used_estimated_prompt"] or token_stats["used_estimated_completion"]:
                print(
                    "统计说明: provider usage 异常，已使用本地估算兜底"
                    f" (provider_prompt={token_stats['provider_prompt_tokens']},"
                    f" provider_completion={token_stats['provider_completion_tokens']},"
                    f" estimated_prompt={token_stats['estimated_prompt_tokens']},"
                    f" estimated_completion={token_stats['estimated_completion_tokens']})"
                )
            print("=====================\n")

            # 将响应添加到对话历史
            if self.conversation:
                self.conversation.add_message(self.name, response)

            return response
        except Exception as e:
            logger.error(f"LLM 调用失败: {e}")
            raise
    
    def augment_prompt(self, query: str, mode: str = "generate") -> str:
        """
        使用知识库增强提示词
        """
        return self.pipeline._augment_prompt(query, mode)


class RequirementsAnalystAgent(BaseAgent):
    """
    需求分析师Agent
    职责：解析自然语言需求 → 原子命题、组件映射
    """
    
    def __init__(self, pipeline):
        super().__init__("analyst", pipeline)
    
    def parse_requirements(self, user_requirements: str) -> Dict[str, Any]:
        """
        解析用户需求为原子命题
        """
        print(f"[{self.name}] 正在解析需求: {user_requirements[:100]}...")
        
        if not user_requirements.strip():
            error_msg = "用户需求为空"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}
        
        prompt = self.augment_prompt(
            f"请从以下自然语言需求中提取候选原子命题（atomic propositions）。\n"
            f"每个命题必须是一个可判断真假的形式化表达式，例如 'temp_in > 80'、'alarm_out = true' 或 'system_stop = true'。\n"
            f"请严格参考AGREE_code_knowledge_dataset.txt文件中提供的示例样本的形式化表达式表述方式。\n"
            f"边界要求：\n"
            f"- 只做需求语义拆解，不生成AGREE代码，不补充需求中没有表达的功能。\n"
            f"- 若自然语言没有给出确切端口名，可使用语义清晰的候选变量名，但不要伪造复杂组件路径。\n"
            f"- 每行只输出一个原子命题；不要输出解释、编号、Markdown、JSON或代码块。\n"
            f"- 原子命题应尽量保持最小粒度，避免把多个条件用 and/or 合成一行。\n\n"
            f"需求：\n{user_requirements}",
            mode="generate"
        )
        
        system_prompt = (
            "你是一个形式化需求分析专家，职责是把自然语言需求拆成最小候选原子命题。"
            "你的输出将被后续AGREE生成器使用，因此必须保守、精确、可判真值。"
            "只输出原子命题表达式，每行一个；不要输出解释、Markdown、JSON、代码块或完整AGREE规范。"
            "如果需求含糊，只抽取明确表达的条件，不要自行扩展系统行为。"
        )
        
        try:
            result = self.call_llm(system_prompt, prompt, temperature=0.2, max_tokens=10000)
            self.pipeline.state['atomic_propositions'] = result
            print(f"[{self.name}] 原子命题提取完成")
            print(f"\n提取的原子命题内容：\n{result}\n")
            return {"success": True, "result": result}
        except Exception as e:
            error_msg = f"解析失败: {str(e)}"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}


class AGREEGeneratorAgent(BaseAgent):
    """
    AGREE生成器Agent
    职责：编写AGREE规范代码（Annex）
    """
    
    def __init__(self, pipeline):
        super().__init__("generator", pipeline)

    def _strip_reasoning_text(self, text: str) -> str:
        if not text:
            return ""
        cleaned = text.strip()
        cleaned = re.sub(r"<think>.*?</think>", "", cleaned, flags=re.DOTALL | re.IGNORECASE)
        cleaned = re.sub(r"<thinking>.*?</thinking>", "", cleaned, flags=re.DOTALL | re.IGNORECASE)
        return cleaned.strip()

    def _iter_code_blocks(self, text: str) -> List[str]:
        if not text:
            return []
        return [
            match.group(1).strip()
            for match in re.finditer(r"```(?:aadl|agree|text)?\s*(.*?)\s*```", text, re.DOTALL | re.IGNORECASE)
            if match.group(1).strip()
        ]

    def _find_annex_blocks(self, text: str) -> List[str]:
        """
        Extract AGREE annex blocks without depending on a trailing semicolon.
        Models often return `**}` instead of `**};`; both are usable once normalized.
        """
        if not text:
            return []

        blocks: List[str] = []
        pattern = re.compile(r"annex\s+agree\s*\{\*\*", re.IGNORECASE)
        for match in pattern.finditer(text):
            start = match.start()
            end_match = re.search(r"\*\*}\s*;?", text[match.end():], re.DOTALL)
            if not end_match:
                continue
            end = match.end() + end_match.end()
            block = text[start:end].strip()
            block = self._normalize_annex_block(block)
            if block:
                blocks.append(block)

        unique_blocks: List[str] = []
        seen = set()
        for block in blocks:
            key = re.sub(r"\s+", " ", block).lower()
            if key not in seen:
                seen.add(key)
                unique_blocks.append(block)
        return unique_blocks

    def _normalize_annex_block(self, text: str) -> str:
        if not text:
            return ""
        block = text.strip()
        block = re.sub(r"^```(?:aadl|agree|text)?\s*", "", block, flags=re.IGNORECASE)
        block = re.sub(r"\s*```$", "", block)
        block = block.strip()
        if not re.search(r"annex\s+agree\s*\{\*\*", block, re.IGNORECASE):
            return ""
        if re.search(r"\*\*}\s*$", block) and not re.search(r"\*\*}\s*;\s*$", block):
            block += ";"
        return block

    def _extract_section_text(self, text: str, start_patterns: List[str], stop_patterns: List[str]) -> str:
        starts = []
        for pattern in start_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                starts.append(match)
        if not starts:
            return ""

        start_match = min(starts, key=lambda item: item.start())
        section_start = start_match.end()
        section_end = len(text)
        for pattern in stop_patterns:
            stop_match = re.search(pattern, text[section_start:], re.IGNORECASE)
            if stop_match:
                section_end = min(section_end, section_start + stop_match.start())
        return text[section_start:section_end].strip()

    def _first_annex_from_text(self, text: str) -> str:
        blocks = self._find_annex_blocks(text)
        if blocks:
            return blocks[0]
        for code_block in self._iter_code_blocks(text):
            blocks = self._find_annex_blocks(code_block)
            if blocks:
                return blocks[0]
        return ""

    def _extract_agree_sections(self, result: str) -> tuple[str, str]:
        cleaned = self._strip_reasoning_text(result)
        if not cleaned:
            return "", ""

        system_headers = [
            r"#+\s*系统级\s*AGREE\s*规范\s*#+",
            r"#+\s*系统级\s*AGREE\s*#+",
            r"#+\s*System(?:-|\s*)level\s*AGREE(?:\s*specification)?\s*#+",
            r"#+\s*System\s*AGREE(?:\s*specification)?\s*#+",
        ]
        implementation_headers = [
            r"#+\s*系统实现级\s*AGREE\s*规范\s*#+",
            r"#+\s*实现级\s*AGREE\s*规范\s*#+",
            r"#+\s*Implementation(?:-|\s*)level\s*AGREE(?:\s*specification)?\s*#+",
            r"#+\s*Implementation\s*AGREE(?:\s*specification)?\s*#+",
        ]

        system_text = self._extract_section_text(cleaned, system_headers, implementation_headers)
        implementation_text = self._extract_section_text(cleaned, implementation_headers, [])
        system_agree = self._first_annex_from_text(system_text)
        implementation_agree = self._first_annex_from_text(implementation_text)

        if system_agree or implementation_agree:
            return system_agree, implementation_agree

        # Fallback: inspect the complete response and every code block. This avoids
        # losing the second annex when the model wraps each section in a fence.
        annex_blocks = self._find_annex_blocks(cleaned)
        for code_block in self._iter_code_blocks(cleaned):
            annex_blocks.extend(self._find_annex_blocks(code_block))

        unique_blocks: List[str] = []
        seen = set()
        for block in annex_blocks:
            key = re.sub(r"\s+", " ", block).lower()
            if key not in seen:
                seen.add(key)
                unique_blocks.append(block)

        if len(unique_blocks) >= 2:
            return unique_blocks[0], unique_blocks[1]
        if len(unique_blocks) == 1:
            return "", unique_blocks[0]
        return "", ""
    
    def generate_spec(self, target_component: Optional[str] = None) -> Dict[str, Any]:
        """
        生成AGREE形式化规范
        """
        if target_component is None:
            target_component = self.pipeline._infer_target_component()
            if not target_component:
                error_msg = "无法推断目标组件"
                logger.error(error_msg)
                return {"success": False, "error": error_msg}
        
        # 移除可能的.impl后缀，确保我们处理的是系统名称
        system_name = target_component.replace('.impl', '')
        implementation_name = f"{system_name}.impl"
        
        print(f"[{self.name}] 正在为系统 '{system_name}' 及其实现 '{implementation_name}' 生成AGREE规范")
        
        props = self.pipeline.state.get('atomic_propositions', '无原子命题')
        
        # 从状态中获取所有模型
        all_models = self.pipeline.state.get('all_models', {})
        
        # 从状态中获取用户需求
        user_requirements = self.pipeline.state.get('user_requirements', '')
        
        # 构建模型上下文
        model_context = ""
        if all_models:
            # 添加主模型
            model_context += "### 主AADL模型：\n"
            model_context += all_models.get('main', '')
            model_context += "\n\n"
            
            # 添加引用包模型
            references = all_models.get('references', [])
            if references:
                model_context += "### 引用包模型：\n"
                for ref in references:
                    model_context += f"#### {ref.get('path', 'unknown')}：\n"
                    model_context += ref.get('content', '')
                    model_context += "\n\n"
        
        # 构建提示词，要求同时生成系统级和系统实现级的AGREE规范
        prompt_content = f"请为AADL系统 '{system_name}' 及其实现 '{implementation_name}' 生成完整的AGREE附件（annex agree {{** ... **}}），需满足以下要求： \n"
        prompt_content += f" \n"
        prompt_content += f"## 一、需求描述 \n"
        prompt_content += f"{user_requirements} \n"
        prompt_content += f" \n"
        prompt_content += f"## 二、原子命题 \n"
        prompt_content += f"{props} \n"
        prompt_content += f" \n"
        prompt_content += f"## 三、生成要求 \n"
        prompt_content += f"1. 作用域：只为目标组件定义 '{system_name}' 和目标组件实现 '{implementation_name}' 生成AGREE附件，不要为其他组件生成规范。 \n"
        prompt_content += f"2. 可见性：只能引用目标组件 features 中存在的端口、目标组件 annex 中声明的 eq/const，以及模型上下文中真实存在并可通过包名访问的函数/类型。 \n"
        prompt_content += f"3. 系统级AGREE规范：只放 assume / guarantee / eq / const / lemma 中适合组件类型层级的内容；不要引用 implementation 才可见的 subcomponents / connections / ports。 \n"
        prompt_content += f"4. 实现级AGREE规范：仅在确有合法左值时写 assign；assign 左值只能是当前组件自身输出端口或当前 annex 中声明的 eq 变量，绝不能是子组件端口、输入端口或不存在的变量。 \n"
        prompt_content += f"5. 最小化：优先生成能够表达需求的最小规范，不要重复生成同义 guarantee，不要为了凑完整性而发明状态变量或端口。 \n"
        prompt_content += f"6. 错误避免：关注Attention.txt中的常见问题，尤其避免 assume/guarantee 放错层级、重复 assign、类型不一致、未定义引用、使用 constraint/constant 伪关键字。 \n"
        prompt_content += f" \n"
        prompt_content += f"## 四、验证标准 \n"
        prompt_content += f"生成的AGREE附件需满足以下验证标准： \n"
        prompt_content += f"- 直接嵌入AADL对应系统和实现部分后可正常验证 \n"
        prompt_content += f"- 无'变量未关联'/'类型未识别'/'约束无操作逻辑'等警告 \n"
        prompt_content += f"- 可成功触发目标场景的验证 \n"
        prompt_content += f"- 若目标 system 定义没有 features，则系统级 annex 不得引用仅在 system implementation 中可见的 subcomponents / connections / ports \n"
        prompt_content += f"- 不要使用 constraint / constant 这类非 AGREE Annex 关键字块；优先使用 assume / guarantee / eq / const / lemma / assign \n"
        prompt_content += f" \n"
        prompt_content += f"## 五、模型上下文 \n"
        prompt_content += f"请参考以下AADL模型（包括主模型和引用包模型），确保生成的AGREE代码仅引用模型中实际存在的函数和组件：\n"
        prompt_content += f"{model_context}"
        prompt_content += f" \n"
        prompt_content += f"## 六、输出格式 \n"
        prompt_content += f"请按照以下格式输出：\n"
        prompt_content += f"### 系统级AGREE规范 ###\n"
        prompt_content += f"[系统级AGREE附件代码]\n"
        prompt_content += f"\n### 系统实现级AGREE规范 ###\n"
        prompt_content += f"[系统实现级AGREE附件代码]\n"
        
        prompt = self.augment_prompt(prompt_content, mode="generate")
        
        system_prompt = """你是一个AGREE Annex生成专家。你的职责是基于需求和AADL上下文，为指定目标组件生成最小、可插入、可验证的AGREE附件。

硬性规则：
- 只输出两个AGREE附件段，不输出解释、Markdown之外的说明、完整AADL模型或JSON。
- 必须保留完整的 annex agree {** ... **}; 结构，{** 和 **} 符号不可修改或删除。
- 只为用户指定的目标组件类型和目标组件实现生成规范；不要给其他组件生成任何内容。
- 只引用AADL模型中真实存在且在当前层级可见的端口、类型、函数和包名；不确定时不要引用。
- 系统级annex不得引用implementation中的subcomponents、connections或subcomponent.port。
- implementation级annex只有在存在合法左值时才写assign；assign左值只能是当前组件自身输出端口或当前annex中声明的eq变量，绝不能是输入端口、子组件端口或不存在的变量。
- 不要使用 constraint / constant 这类非AGREE Annex关键字块；常量使用 const。
- 不要生成重复同义约束，不要发明端口、函数、包、子组件或需求中没有的行为。

输出格式必须严格为：
### 系统级AGREE规范 ###
annex agree {**
...
**};

### 系统实现级AGREE规范 ###
annex agree {**
...
**};"""
        
        try:
            result = self.call_llm(system_prompt, prompt, temperature=0.2, max_tokens=14000)
            
            # 解析输出结果，分离系统级和系统实现级的AGREE规范
            system_agree, implementation_agree = self._extract_agree_sections(result)
            self.pipeline.state['agree_generator_raw_output'] = result
            
            # 保存生成的AGREE规范到状态中
            if system_agree:
                self.pipeline.state['agree_code_system'] = system_agree
                print(f"[{self.name}] 系统级AGREE规范生成完成")
                print(f"\n生成的系统级AGREE规范内容：\n{system_agree}\n")
            
            if implementation_agree:
                self.pipeline.state['agree_code_implementation'] = implementation_agree
                self.pipeline.state['agree_code'] = implementation_agree  # 保持向后兼容
                print(f"[{self.name}] 系统实现级AGREE规范生成完成")
                print(f"\n生成的系统实现级AGREE规范内容：\n{implementation_agree}\n")
            
            # 如果只生成了一个，也返回成功
            if system_agree or implementation_agree:
                return {"success": True, "result": result, "system_agree": system_agree, "implementation_agree": implementation_agree}
            else:
                self.pipeline.state['agree_generator_parse_failure_output'] = result
                return {"success": False, "error": "未能生成有效的AGREE规范", "raw_output": result}
        except Exception as e:
            error_msg = f"生成失败: {str(e)}"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}


class AADLModelAnalystAgent(BaseAgent):
    """
    AADL模型分析Agent
    职责：解析AADL模型结构，提取组件、连接和属性信息
    """
    
    def __init__(self, pipeline):
        super().__init__("model_analyst", pipeline)

    def _extract_first_json_object(self, text: str) -> str:
        """
        从模型返回的混合文本中提取第一个完整 JSON 对象。
        支持：
        1. ```json ... ```
        2. ``` ... ```
        3. 前后夹杂解释文字的 { ... }
        """
        if not text:
            return ""

        stripped = text.strip()

        fenced_json = re.search(r"```json\s*(.*?)\s*```", stripped, re.DOTALL | re.IGNORECASE)
        if fenced_json:
            return fenced_json.group(1).strip()

        fenced_any = re.search(r"```\s*(.*?)\s*```", stripped, re.DOTALL)
        if fenced_any:
            candidate = fenced_any.group(1).strip()
            if candidate.startswith("{"):
                return candidate

        start = stripped.find("{")
        if start == -1:
            return stripped

        in_string = False
        escape_next = False
        depth = 0
        for index in range(start, len(stripped)):
            char = stripped[index]
            if escape_next:
                escape_next = False
                continue
            if char == "\\":
                escape_next = True
                continue
            if char == '"':
                in_string = not in_string
                continue
            if in_string:
                continue
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return stripped[start:index + 1]

        return stripped[start:].strip()

    def _close_truncated_json_prefix(self, text: str) -> str:
        """
        针对被截断的 JSON，尽量保留最后一个完整对象/数组，并补齐缺失的闭合符。
        """
        if not text:
            return text

        candidate = text.strip()
        if not candidate.startswith("{"):
            return candidate

        in_string = False
        escape_next = False
        stack = []
        last_complete_end = -1

        for index, char in enumerate(candidate):
            if escape_next:
                escape_next = False
                continue
            if char == "\\":
                escape_next = True
                continue
            if char == '"':
                in_string = not in_string
                continue
            if in_string:
                continue

            if char in "{[":
                stack.append(char)
            elif char == "}" and stack and stack[-1] == "{":
                stack.pop()
                last_complete_end = index
            elif char == "]" and stack and stack[-1] == "[":
                stack.pop()
                last_complete_end = index

        if last_complete_end != -1:
            candidate = candidate[:last_complete_end + 1].rstrip()
            candidate = re.sub(r',\s*$', '', candidate)

        in_string = False
        escape_next = False
        stack = []
        for char in candidate:
            if escape_next:
                escape_next = False
                continue
            if char == "\\":
                escape_next = True
                continue
            if char == '"':
                in_string = not in_string
                continue
            if in_string:
                continue
            if char in "{[":
                stack.append(char)
            elif char == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack and stack[-1] == "[":
                stack.pop()

        while stack:
            opener = stack.pop()
            candidate += "}" if opener == "{" else "]"

        return candidate
    
    def analyze_model_structure(self, aadl_model: str) -> Dict[str, Any]:
        """
        分析AADL模型结构，提取组件、连接和属性信息
        """
        print(f"[{self.name}] 正在分析AADL模型结构...")
        
        # 保存原始模型到状态
        self.pipeline.state['raw_aadl_snippet'] = aadl_model.strip()
        self.pipeline.state['aadl_analysis'] = {}
        
        query = f"""
请分析以下 AADL 模型代码，提取结构化信息，并以严格 JSON 格式输出。

1. 组件接口（Components & Features）：
- 组件名称（component name）
- 类型必须规范化为 AADL 类别，如 system、system_implementation、thread、thread_implementation、process、process_implementation、device、data、subprogram 等
- 端口（features）：包括名称、方向（in/out/in out）、端口类别（data port/event data port等）、数据类型

2. 连接关系（Connections）：
- 连接名称
- 源端口（source）
- 目标端口（target）

3. 属性声明（Properties）：
- 属性名（property name）必须使用键名 "name"
- 值（value）必须使用键名 "value"

请确保输出为标准 JSON 对象，包含且仅包含三个顶层字段：
- "components": 列表，每个元素必须包含 "name"、"type"、"features" 字段；features 为空时使用 []
- "connections": 列表，每个元素必须包含 "name"、"source"、"target" 字段；无连接时使用 []
- "properties": 列表，每个元素必须包含 "name" 和 "value" 字段；无属性时使用 []

特别注意：对于属性声明，请准确提取属性名称，如 Data_Representation、Byte_Size、End_To_End_Delay_Constraint、Criticality、Virtual_Processor_Binding 等。

仅输出 JSON，不要额外解释，不要使用Markdown代码块，不要根据知识库示例补充模型中不存在的组件。

AADL 模型代码：
{aadl_model}
"""
        
        # 使用pipeline的增强提示词功能
        augmented_prompt = self.augment_prompt(query, mode="generate")
        
        system_prompt = """你是一个 AADL 静态结构分析专家。你的任务是忠实解析用户提供的AADL源码，并输出机器可解析的JSON结构。

规则：
- 只输出合法JSON对象，不输出解释、Markdown或代码块。
- 只能提取源码中真实出现的组件、features、connections、properties，不要从参考知识中补充或改写模型。
- 保留组件名、端口名、包名、大小写和 .impl 后缀。
- 如果某一类信息不存在，输出空数组。
- 对属性声明，请特别注意准确识别属性名称，例如：
- Data_Representation
- Byte_Size
- End_To_End_Delay_Constraint
- Criticality
- Virtual_Processor_Binding

JSON顶层字段必须且只能是 "components"、"connections"、"properties"。"""
        
        try:
            # 使用Agent的call_llm方法
            response = self.call_llm(
                system_prompt,
                augmented_prompt,
                temperature=0.1,
                max_tokens=10000,
                use_conversation_history=False
            )

            response = self._extract_first_json_object(response)
             
            # 打印原始响应以便调试
            # print("[调试] LLM原始响应:", response[:500] + "..." if len(response) > 500 else response)
             
            # 初始化result变量和fixed_response变量
            result = None
            fixed_response = response.strip()

            if not fixed_response:
                raise ValueError("模型返回为空，无法解析 JSON")
             
            try:
                # 尝试直接解析
                result = json.loads(fixed_response)
            except json.JSONDecodeError as e:
                # print(f"[调试] 初始解析失败: {str(e)}")
                # 尝试修复常见的JSON格式问题
                
                # 1. 移除末尾可能多余的逗号
                fixed_response = re.sub(r',\s*}', '}', fixed_response)
                fixed_response = re.sub(r',\s*]', ']', fixed_response)
                
                # 2. 添加缺少的逗号（处理"Expecting ',' delimiter"错误）
                # 查找缺少逗号的模式，如 "key": "value"  "key2": "value2"
                # 在非字符串状态下，查找 } 或 ] 后面缺少逗号的情况
                in_string = False
                escape_next = False
                needs_comma = []
                
                for i, char in enumerate(fixed_response):
                    if escape_next:
                        escape_next = False
                    elif char == '\\':
                        escape_next = True
                    elif char == '"' and not escape_next:
                        in_string = not in_string
                    elif not in_string:
                        # 检查是否需要添加逗号
                        # 模式："value"  "key":
                        if i > 0 and char == '"' and fixed_response[i-1].isspace():
                            # 向前查找最近的非空格字符
                            j = i - 1
                            while j >= 0 and fixed_response[j].isspace():
                                j -= 1
                            if j >= 0 and fixed_response[j] == '"':
                                # 找到模式："value"  "key":，需要在中间添加逗号
                                needs_comma.append(i)
                
                # 从后向前添加逗号，避免索引偏移
                for i in reversed(needs_comma):
                    fixed_response = fixed_response[:i] + ',' + fixed_response[i:]
                
                if needs_comma:
                    pass
                    # print(f"[调试] 已添加 {len(needs_comma)} 个缺少的逗号")
                
                # 3. 处理未终止的字符串和转义字符
                in_string = False
                escape_next = False
                clean_response = []
                for char in fixed_response:
                    if escape_next:
                        clean_response.append(char)
                        escape_next = False
                    elif char == '\\':
                        clean_response.append(char)
                        escape_next = True
                    elif char == '"' and not escape_next:
                        in_string = not in_string
                        clean_response.append(char)
                    else:
                        clean_response.append(char)
                
                fixed_response = ''.join(clean_response)
                
                # 3. 检查并修复未终止的字符串
                in_string = False
                escape_next = False
                for i, char in enumerate(fixed_response):
                    if escape_next:
                        escape_next = False
                    elif char == '\\':
                        escape_next = True
                    elif char == '"' and not escape_next:
                        in_string = not in_string
                
                # 如果字符串未终止，添加一个引号
                if in_string:
                    fixed_response += '"'
                    # print("[调试] 已修复未终止的字符串")
                
                # 4. 尝试截取到可能有效的部分（考虑字符串中的大括号）
                if fixed_response.startswith('{'):
                    open_braces = 0
                    close_braces = 0
                    valid_end = len(fixed_response)
                    in_string = False
                    escape_next = False
                    
                    for i, char in enumerate(fixed_response):
                        if escape_next:
                            escape_next = False
                        elif char == '\\':
                            escape_next = True
                        elif char == '"' and not escape_next:
                            in_string = not in_string
                        elif not in_string:
                            if char == '{':
                                open_braces += 1
                            elif char == '}':
                                close_braces += 1
                                if open_braces == close_braces:
                                    valid_end = i + 1
                                    break
                    
                    if valid_end < len(fixed_response):
                        fixed_response = fixed_response[:valid_end]
                        # print("[调试] 已截取到有效JSON部分")

                # 5. 针对尾部截断的 JSON，截到最后一个完整对象并自动补齐缺失括号
                fixed_response = self._close_truncated_json_prefix(fixed_response)

                # print("[调试] 修复后的JSON:", fixed_response[:500] + "..." if len(fixed_response) > 500 else fixed_response)
                
                # 只有在初始解析失败时才尝试修复后的解析
                try:
                    result = json.loads(fixed_response)
                except json.JSONDecodeError as e2:
                    # print(f"[调试] 修复后仍然解析失败: {str(e2)}")
                    raise
            
            expected_keys = {"components", "connections", "properties"}
            if not expected_keys.issubset(result.keys()):
                raise ValueError(f"缺少必要字段，应包含: {expected_keys}")
            
            # 保存解析结果到状态
            self.pipeline.state['aadl_analysis'].update(result)
            self.pipeline.state['components_list'] = [comp.get("name", "未命名组件") for comp in result["components"]]
            
            print(f"[{self.name}] 模型结构分析完成，解析出 {len(result['components'])} 个组件，")
            print(f"[{self.name}] {len(result['connections'])} 条连接，{len(result['properties'])} 个属性")
            
            print("解析结果（结构化摘要）：")
            components = [c.get('name', '未命名组件') for c in result['components']]
            connections = [f"{c.get('source', '未知源')} -> {c.get('target', '未知目标')}" for c in result['connections']]
            properties = [f"{p.get('name', '未知属性')} => {p.get('value', '未知值')}" for p in result['properties']]
            print(f"  组件: {components}")
            print(f"  连接: {connections}")
            print(f"  属性: {properties}\n")
            
            return {"success": True, "result": result}
            
        except Exception as e:
            error_msg = f"模型分析失败: {str(e)}"
            logger.error(error_msg)
            print(f"[{self.name}] 分析失败：" + error_msg + "\n")
            return {"success": False, "error": error_msg}


class AADLMergeAgent(BaseAgent):
    """
    AADL融合Agent
    职责：将AGREE规范代码合并到AADL模型中
    """
    def __init__(self, pipeline):
        super().__init__("merger", pipeline)

    def _strip_reasoning_text(self, text: str) -> str:
        if not text:
            return ""
        cleaned = text.strip()
        cleaned = re.sub(r"<think>.*?</think>", "", cleaned, flags=re.DOTALL | re.IGNORECASE)
        cleaned = re.sub(r"<thinking>.*?</thinking>", "", cleaned, flags=re.DOTALL | re.IGNORECASE)
        return cleaned.strip()

    def _extract_aadl_model(self, response: str) -> str:
        cleaned = self._strip_reasoning_text(response)
        if not cleaned:
            return ""

        code_blocks = [
            match.group(1).strip()
            for match in re.finditer(r"```(?:aadl|text)?\s*(.*?)\s*```", cleaned, re.DOTALL | re.IGNORECASE)
            if match.group(1).strip()
        ]
        if code_blocks:
            aadl_like_blocks = [block for block in code_blocks if re.search(r"\bpackage\s+\w+", block, re.IGNORECASE)]
            candidates = aadl_like_blocks or code_blocks
            return max(candidates, key=len).strip()

        # Some models prepend comments or labels before the package. Keep the
        # complete AADL model and discard only text before the first package.
        package_match = re.search(r"\bpackage\s+\w+", cleaned, re.IGNORECASE)
        if package_match:
            return cleaned[package_match.start():].strip()
        return cleaned

    def _is_plausible_full_aadl(self, code: str, original_aadl: str) -> tuple[bool, str]:
        stripped = (code or "").strip()
        if not stripped:
            return False, "模型未返回AADL内容"
        if stripped.startswith("{") or stripped.startswith("["):
            return False, "模型返回了JSON/结构化分析结果，而不是完整AADL模型"
        if not re.search(r"\bpackage\s+\w+", stripped, re.IGNORECASE):
            return False, "融合结果中未发现AADL package声明"
        if not re.search(r"\bend\s+\w+\s*;", stripped, re.IGNORECASE):
            return False, "融合结果中未发现AADL package结束声明"

        original_len = len((original_aadl or "").strip())
        if original_len > 1000 and len(stripped) < original_len * 0.5:
            return False, f"融合结果过短，疑似只返回了片段 ({len(stripped)} / {original_len})"
        return True, ""
    
    def merge_spec_into_model(self, target_component: Optional[str] = None) -> Dict[str, Any]:
        """
        合并AGREE规范到AADL模型
        
        Args:
            target_component: 目标组件名称，如果提供则直接使用
            
        Returns:
            Dict: 包含成功状态和结果的字典
        """
        if target_component is None:
            # 调用修改后的_infer_target_component方法
            target_component = self.pipeline._infer_target_component(target_component)
            if not target_component:
                error_msg = "无法推断目标组件"
                logger.error(error_msg)
                return {"success": False, "error": error_msg}
        else:
            # 打印使用指定目标组件的信息
            logger.info(f"使用指定的目标组件: {target_component}")
        
        original_aadl = self.pipeline.state.get('raw_aadl_snippet', '')
        system_agree = self.pipeline.state.get('agree_code_system', '')
        implementation_agree = self.pipeline.state.get('agree_code_implementation', '')
        
        # 保持向后兼容
        if not system_agree and not implementation_agree:
            generated_agree = self.pipeline.state.get('agree_code', '')
            if not generated_agree:
                error_msg = "缺少原始AADL或生成的AGREE代码"
                logger.error(error_msg)
                return {"success": False, "error": error_msg}
            # 如果只有一个AGREE代码，使用它作为实现级代码
            implementation_agree = generated_agree
        
        if not original_aadl:
            error_msg = "缺少原始AADL模型"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}
            
        # 从目标组件名中提取基本组件名（去掉.impl后缀）
        base_component = target_component.replace('.impl', '')
            
        # 构建AGREE代码部分
        agree_code_section = ""
        if system_agree:
            agree_code_section += f"系统级AGREE规范（应插入到组件定义中）:\n{system_agree}\n\n"
        if implementation_agree:
            agree_code_section += f"实现级AGREE规范（应插入到组件实现中）:\n{implementation_agree}\n"
            
        query = (
            f"请将给定AGREE附件插入目标AADL模型的指定组件中。你的任务是结构化编辑，不是重新设计模型或生成新规约。\n\n"
            f"目标组件定义: {base_component}\n"
            f"目标组件实现: {target_component}\n"
            f"待插入AGREE代码:\n{agree_code_section}\n"
            f"原始AADL模型:\n{original_aadl}\n\n"
            f"【核心要求】\n"
            f"1. 输出**完整、未截断的AADL模型**，包含原始模型中的所有组件、定义、实现及结束语句，不遗漏任何内容\n"
            f"2. **只在指定的组件和其实现中插入AGREE代码**，绝对不要在其他组件中添加或修改任何AGREE代码\n"
            f"3. 根据代码类型将AGREE附件分别插入到指定的组件定义和组件实现中\n"
            f"4. 不得新增、删除、重命名、复制任何AADL组件、端口、连接、with子句或类型定义；除目标annex外，原模型文本应尽量保持不变\n"
            f"5. 不得自行补写新的assign、eq、guarantee或assume；只能插入“待插入AGREE代码”中已经给出的内容\n\n"
            f"【语法格式要求】\n"
            f"1. 保留原始模型所有内容，不增删组件定义、结束语句及分号\n"
            f"2. AGREE附件需与组件内其他元素保持一致缩进\n"
            f"3. 禁止重复添加 annex agree 块，若原始模型已有则替换\n"
            f"4. 严格保留 'annex agree {{** ... **}}' 结构，{{**和**}}为核心语法符号，绝不能删除/修改\n"
            f"5. 参考 AGREE_code_knowledge_dataset.txt 示例及 AGREE_knowledge_dataset_ch.pdf 语法规范\n\n"
            f"【正确结构示例】\n"
            f"system GCAS_singleton\n"
            f"  features\n"
            f"    altitude: in data port real;\n"
            f"    timeToRecovery: out data port real;\n"
            f"  \n"
            f"  annex agree {{**\n"
            f"    eq t: real = 0.0 -> pre(t) + 0.1;\n"
            f"    eq height: real;\n"
            f"  \n"
            f"    const minHeightAllowed: real = 200.0;\n"
            f"  \n"
            f"    guarantee \"safe after some time\": t >= timeToRecovery => (height > minHeightAllowed) and (height > pre(height));\n"
            f"  **}};\n"
            f"end GCAS_singleton;\n"
            f"\n"
            f"system implementation GCAS_singleton.impl\n"
            f"  annex agree {{**\n"
            f"    assign height = gcas_nodes.kinematicLinearization(t);\n"
            f"    assign timeToRecovery = 3.7;\n"
            f"  **}};\n"
            f"end GCAS_singleton.impl;\n"
            f"\n"
            f"【核心提示】\n"
            f"AGREE附件需要根据内容类型分别放置：\n"
            f"- 组件定义({base_component})中：eq变量定义、const常量定义、guarantee约束语句、assume约束语句\n"
            f"- 组件实现({target_component})中：assign赋值语句、lemma语句\n"
            f"- 如果待插入代码中某一级为空，则不要为该层级创造新的annex\n\n"
            f"【正确输出标准】\n"
            f"输出结果必须是可直接运行的完整AADL模型，包含从第一个组件定义到最后一个'end'语句的所有内容。\n"
            f"必须确保AGREE附件内容正确分布在组件定义和组件实现中，遵循上述结构规范。\n"
            f"除了插入或替换目标组件的annex agree块，不允许做其他语义改写。"
        )
        augmented_prompt = self.augment_prompt(query, mode="validate")
        system_prompt = (
            "你是一个AADL源码编辑器。你的唯一任务是把给定AGREE附件插入指定组件，"
            "并返回完整AADL源码。不要生成新规约，不要重构模型，不要复制组件，不要解释。"
        )
        
        try:
            merged_output = self.call_llm(
                system_prompt,
                augmented_prompt,
                temperature=0.1,
                max_tokens=10000,
                use_conversation_history=False,
            )
            self.pipeline.state["merge_raw_output"] = merged_output
            merged_aadl = self._extract_aadl_model(merged_output)
            is_valid_model, invalid_reason = self._is_plausible_full_aadl(merged_aadl, original_aadl)
            if not is_valid_model:
                self.pipeline.state["merge_rejected_reason"] = invalid_reason
                return {
                    "success": False,
                    "error": f"融合结果不是有效的完整AADL模型: {invalid_reason}",
                    "raw_output": merged_output,
                }
            
            self.pipeline.state['merged_aadl'] = merged_aadl
            print(f"[{self.name}] AGREE附件已成功集成到AADL模型")
            print(f"\n合并后的AADL模型内容：\n{merged_aadl[:1000]}...\n")
            print("(输出内容已截断，完整内容请查看文件)\n")
            return {"success": True, "result": merged_aadl}
        except Exception as e:
            error_msg = f"合并失败: {str(e)}"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}


class AADLValidatorAgent(BaseAgent):
    """
    AADL验证Agent
    职责：语法检查 + 修复（可调用AADL Inspector和AGREE验证器）
    """
    def __init__(self, pipeline):
        super().__init__("validator", pipeline)

    def validate_and_fix(self, error_level_info: Dict = None) -> Dict[str, Any]:
        """
        验证并修复AGREE代码语法，支持错误层级判断

        Args:
            error_level_info: 错误层级信息字典

        Returns:
            Dict: 包含成功状态、修复后的代码和验证报告的字典
        """
        print(f"[{self.name}] 正在验证并修复代码...")

        # 获取合并后的AADL代码
        merged_aadl = self.pipeline.state.get('merged_aadl', '')
        if not merged_aadl:
            error_msg = "未找到合并后的AADL代码，请先运行融合步骤"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}

        # 确定需要修复的错误类型
        aadl_errors = []
        agree_errors = []
        if error_level_info:
            aadl_errors = error_level_info.get("aadl_errors", [])
            agree_errors = error_level_info.get("agree_errors", [])

        # 根据错误类型构建错误摘要
        all_errors = []
        if aadl_errors:
            all_errors.extend(aadl_errors)
        if agree_errors:
            all_errors.extend(agree_errors)

        error_summary = "\n".join(all_errors) if all_errors else ""

        # 如果没有错误，直接返回
        if not all_errors:
            print("\n[提示] 未检测到需要修复的错误")
            return {
                "success": True,
                "result": merged_aadl,
                "validation_report": "未检测到错误",
                "skipped": True,
                "repair_count": 0,
                "final_dual_result": None
            }

        # 进行验证修复
        result = self._validate_and_fix(aadl_errors=error_summary,
                                        has_aadl_errors=len(aadl_errors) > 0,
                                        has_agree_errors=len(agree_errors) > 0,
                                        error_level_info=error_level_info)

        # 循环修复直到通过检查（最多8次迭代）
        iteration = 1
        final_dual_result = None
        max_iterations = 8

        while iteration <= max_iterations:
            print(f"\n[{self.name}] ===== 修复迭代 {iteration}/{max_iterations} =====")

            # 运行双重验证
            dual_result = self.pipeline.run_dual_validation(self.pipeline.state)
            result.update(dual_result)
            final_dual_result = dual_result

            error_info = dual_result.get("error_level_info", {})
            has_aadl_err = error_info.get("has_aadl_errors", False)
            has_agree_err = error_info.get("has_agree_errors", False)

            # 检查是否通过
            if not has_aadl_err and not has_agree_err:
                print(f"\n[{self.name}] 迭代 {iteration}/{max_iterations}：所有错误已修复完成！")
                break

            # 检查是否达到最大迭代次数
            if iteration >= max_iterations:
                print(f"\n[{self.name}] 已达到最大迭代次数 {max_iterations}，停止修复")
                break

            # 继续修复
            print(f"\n[{self.name}] 迭代 {iteration}/{max_iterations}：发现错误，继续修复...")

            # 构建错误摘要
            all_errs = error_info.get("all_errors", [])
            error_summary = "\n".join(all_errs) if all_errs else ""

            self.pipeline.state["merged_aadl"] = result.get("result", "")
            repair_result = self._validate_and_fix(
                aadl_errors=error_summary,
                has_aadl_errors=has_aadl_err,
                has_agree_errors=has_agree_err,
                error_level_info=error_info
            )
            result.update(repair_result)
            if not repair_result.get("success", False):
                print(f"\n[{self.name}] 修复输出不可用，停止迭代: {repair_result.get('error', '未知错误')}")
                break
            iteration += 1

        # 返回修复次数和最终验证结果
        result["repair_count"] = iteration
        result["final_dual_result"] = final_dual_result
        return result

    def _strip_reasoning_text(self, text: str) -> str:
        if not text:
            return ""
        cleaned = text.strip()
        cleaned = re.sub(r"<think>.*?</think>", "", cleaned, flags=re.DOTALL | re.IGNORECASE)
        cleaned = re.sub(r"<thinking>.*?</thinking>", "", cleaned, flags=re.DOTALL | re.IGNORECASE)
        return cleaned.strip()

    def _extract_repaired_code(self, response: str) -> str:
        cleaned = self._strip_reasoning_text(response)
        if not cleaned:
            return ""

        code_blocks = [
            match.group(1).strip()
            for match in re.finditer(r"```(?:aadl|xml|json|text)?\s*(.*?)\s*```", cleaned, re.DOTALL | re.IGNORECASE)
            if match.group(1).strip()
        ]
        if code_blocks:
            aadl_like_blocks = [block for block in code_blocks if re.search(r"\bpackage\s+\w+", block, re.IGNORECASE)]
            candidates = aadl_like_blocks or code_blocks
            return max(candidates, key=len).strip()

        cleaned = re.sub(r"^```(?:aadl|xml|json|text)?\s*", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"\s*```$", "", cleaned)
        return cleaned.strip()

    def _is_plausible_full_aadl(self, code: str, previous_code: str) -> tuple[bool, str]:
        stripped = (code or "").strip()
        if not stripped:
            return False, "模型返回为空"
        if stripped in {"```", "``````"} or set(stripped) <= {"`", "\n", "\r", " ", "\t"}:
            return False, "模型只返回了代码块边界，没有返回AADL内容"
        if not re.search(r"\bpackage\s+\w+", stripped, re.IGNORECASE):
            return False, "修复结果中未发现AADL package声明"
        if not re.search(r"\bend\s+\w+\s*;", stripped, re.IGNORECASE):
            return False, "修复结果中未发现AADL package结束声明"

        previous_len = len(previous_code.strip())
        if previous_len > 1000 and len(stripped) < previous_len * 0.35:
            return False, f"修复结果过短，疑似只返回了片段 ({len(stripped)} / {previous_len})"
        return True, ""
    
    def _validate_and_fix(self, aadl_errors: str = "", has_aadl_errors: bool = False, has_agree_errors: bool = False, error_level_info: Dict = None) -> Dict[str, Any]:
        """
        验证并修复AGREE代码语法，支持错误层级判断

        Args:
            error_level_info: 包含原始验证输出的字典（需求2）
        """
        merged_aadl = self.pipeline.state.get('merged_aadl', '')
        if not merged_aadl:
            error_msg = "未找到合并后的AADL代码"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}

        # 根据错误类型构建不同的系统提示词
        if has_agree_errors and not has_aadl_errors:
            # 只有 AGREE 错误
            system_prompt = """
你是一位专业的AGREE代码验证和修复专家，精通AGREE语法规范。

任务：仔细检查提供的AADL+AGREE代码，识别并修复所有AGREE层级的语法错误。

重要参考资料（请以正确案例为导向）：
1. Attention.txt - 包含常见错误案例和修改方法
2. AGREE_knowledge_dataset_ch.pdf文件 - 这是正确语法规则的主要来源
3. AGREE_code_knowledge_dataset.txt - 包含正确示例

修复步骤：
1. 首先分析AGREE验证器提供的错误信息，精确定位问题位置和类型
2. 以知识库中的正确示例为导向，查找对应的正确语法规范
3. 对每个错误进行精确修复，不要添加或删除原代码的功能
4. 修复后，通览整个代码确保语法一致性和完整性

要求：
1. 仅返回完整的、修复后的代码，不要额外解释
2. 保持原始代码的结构和功能不变
3. 严格遵循AGREE语法规范
4. 【最高优先级】绝对不能删除annex agree {{** **}}语法中的**符号
5. 确保修复后的代码能通过AGREE验证器的检查
6. 只修复验证器报告中指出的问题，不要重写无关组件，不要复制组件，不要删除依赖with子句
7. 输出必须是完整AADL源码，不能是片段、diff、JSON、Markdown解释或仅代码块边界
"""
        elif has_aadl_errors and not has_agree_errors:
            # 只有 AADL 错误
            system_prompt = """
你是一位专业的AADL代码验证和修复专家，精通AADL语法规范。

任务：仔细检查提供的AADL代码，识别并修复所有AADL层级的语法错误。

修复步骤：
1. 首先分析AADL Inspector提供的错误信息，精确定位问题位置和类型
2. 以知识库中的正确示例为导向，查找对应的正确语法规范
3. 对每个错误进行精确修复，不要添加或删除原代码的功能

要求：
1. 仅返回完整的、修复后的代码，不要额外解释
2. 保持原始代码的结构和功能不变
3. 严格遵循AADL语法规范
4. 确保修复后的代码能通过AADL Inspector的检查
5. 只修复AADL Inspector报告中指出的问题，不要改变AGREE规约语义，不要重写无关组件
6. 输出必须是完整AADL源码，不能是片段、diff、JSON、Markdown解释或仅代码块边界
"""
        else:
            # 两种错误都有或都没有
            system_prompt = """
你是一位专业的AGREE代码验证和修复专家，精通AADL和AGREE语法规范。

任务：仔细检查提供的AADL+AGREE代码，识别并修复所有语法错误。

重要参考资料（请以正确案例为导向）：
1. Attention.txt - 包含常见错误案例和修改方法
2. AGREE_knowledge_dataset_ch.pdf文件 - 这是正确语法规则的主要来源
3. AGREE_code_knowledge_dataset.txt - 包含正确示例

修复步骤：
1. 首先分析错误信息，精确定位问题位置和类型
2. 以知识库中的正确示例为导向，查找对应的正确语法规范
3. 对每个错误进行精确修复，不要添加或删除原代码的功能
4. 修复后，通览整个代码确保语法一致性和完整性

要求：
1. 仅返回完整的、修复后的代码，不要额外解释
2. 保持原始代码的结构和功能不变
3. 严格遵循AADL和AGREE语法规范
4. 【最高优先级】绝对不能删除annex agree {{** **}}语法中的**符号
5. 确保修复后的代码能通过验证
6. 只修复验证器报告中指出的问题，不要重写无关组件，不要复制组件，不要删除依赖with子句
7. 输出必须是完整AADL源码，不能是片段、diff、JSON、Markdown解释或仅代码块边界
"""

        # 构建基础查询，包含代码和错误信息
        query = f"""
请验证并修复以下AADL+AGREE代码的语法错误。

要验证的代码：
```
{merged_aadl}
```
"""

        # 优先使用带序号的格式化错误信息（如"错误 1: [行号 75] ..."）
        if error_level_info:
            inspection_formatted_errors = error_level_info.get("inspection_formatted_errors", [])
            agree_raw_output = error_level_info.get("agree_raw_output", "")
            inspection_raw_output = error_level_info.get("inspection_raw_output", "")

            if inspection_formatted_errors:
                # 使用带序号的格式化错误信息传给LLM
                query += "\n检测到的错误信息：\n"
                for err in inspection_formatted_errors:
                    query += f"  {err}\n"
                query += "\n重要：请以知识库中的正确案例为导向，针对上述每个错误进行精确修复。只修复这些错误，不要重写无关模型结构。\n"
            elif agree_raw_output or inspection_raw_output:
                # 降级使用原始完整输出
                query += "\n===== 验证器原始输出 =====\n"
                if inspection_raw_output:
                    query += "\n----- AADL Inspector 输出 -----\n"
                    query += inspection_raw_output
                if agree_raw_output:
                    query += "\n----- AGREE 验证器 输出 -----\n"
                    query += agree_raw_output
                query += "\n===== 原始输出结束 =====\n"
            elif aadl_errors:
                # 降级使用加工过的错误信息
                query += f"\n检测到的错误信息：\n{aadl_errors}\n\n"
                query += "重要：请以知识库中的正确案例为导向，针对上述每个错误进行精确修复。只修复这些错误，不要重写无关模型结构。\n"
        elif aadl_errors:
            # 没有 error_level_info 时使用加工过的错误信息
            query += f"\n检测到的错误信息：\n{aadl_errors}\n\n"
            query += "重要：请以知识库中的正确案例为导向，针对上述每个错误进行精确修复。只修复这些错误，不要重写无关模型结构。\n"

        query += "\n请返回完整的、修复后的AADL源码，不要额外解释，不要输出diff，不要输出JSON，不要只输出局部片段。"

        # 使用生成专用向量库增强提示词
        user_prompt = self.augment_prompt(query, mode="generate")

        try:
            # 需求1：修复迭代时不使用对话历史，只传递最新代码
            result = self.call_llm(system_prompt, user_prompt, temperature=0.2, max_tokens=10000, use_conversation_history=False)
            self.pipeline.state["last_repair_raw_output"] = result
            final_code = self._extract_repaired_code(result)
            is_valid_code, invalid_reason = self._is_plausible_full_aadl(final_code, merged_aadl)
            if not is_valid_code:
                self.pipeline.state["last_repair_rejected_reason"] = invalid_reason
                return {
                    "success": False,
                    "error": f"模型返回的修复代码不完整: {invalid_reason}",
                    "result": merged_aadl,
                    "validation_report": "修复输出被拒绝，保留上一版AADL代码",
                    "output_file": self.pipeline.state.get("final_model_path", "")
                }

            output_file_path = os.path.abspath(os.environ.get("AGREE_WORK_MODEL", "modified_model.aadl"))
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(final_code)
                # 需求3：确保文件写入完成并刷新到磁盘
                f.flush()
                os.fsync(f.fileno())

            self.pipeline.state["final_model_path"] = output_file_path
            self.pipeline.state["merged_aadl"] = final_code

            return {
                "success": True,
                "result": final_code,
                "validation_report": "AGREE代码已验证并修复" if aadl_errors else "未发现语法错误",
                "output_file": output_file_path
            }
        except Exception as e:
            error_msg = f"自动修复失败: {str(e)}"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}


