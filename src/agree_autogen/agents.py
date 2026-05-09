import json
import re
from typing import Any, Dict, List, Optional

from .runtime import logger, normalize_token_usage


class Conversation:
    """Shared conversation history for the cooperating agents."""

    def __init__(self):
        self.messages: List[Dict[str, str]] = []

    def add_message(self, role: str, content: str):
        if not role or not content:
            return
        self.messages.append({"role": role, "content": content})
        logger.info("[%s] message added to shared conversation", role)

    def format_for_llm(self, system_prompt: str, user_prompt: str) -> List[Dict[str, str]]:
        messages = [{"role": "system", "content": system_prompt}]
        role_mapping = {
            "analyst": "assistant",
            "generator": "assistant",
            "validator": "assistant",
            "system": "system",
            "user": "user",
        }
        for msg in self.messages:
            original_role = msg.get("role", "")
            llm_role = role_mapping.get(original_role, "assistant")
            content = msg.get("content", "")
            if original_role in {"analyst", "generator", "validator"}:
                content = f"[agent:{original_role.upper()}] {content}"
            messages.append({"role": llm_role, "content": content})
        messages.append({"role": "user", "content": user_prompt})
        return messages

    def __str__(self) -> str:
        result = []
        for msg in self.messages:
            content = msg.get("content", "")
            first_line = content.split("\n")[0]
            result.append(f"[{msg.get('role', 'unknown')}]: {first_line}")
        return "\n".join(result)

    def get_history(self) -> List[Dict[str, str]]:
        return self.messages


class BaseAgent:
    """Base class for all LLM-backed agents."""

    def __init__(self, name: str, pipeline):
        self.name = name
        self.pipeline = pipeline
        self.conversation: Optional[Conversation] = None

    def set_conversation(self, conversation: Conversation):
        self.conversation = conversation

    def call_llm(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 2000,
        use_conversation_history: bool = True,
    ) -> str:
        try:
            print("\n=== LLM request ===")
            print(f"Model: {self.pipeline.llm_model_name}")
            print(f"temperature: {temperature}")
            print(f"max_tokens: {max_tokens}")
            print(f"use_conversation_history: {bool(self.conversation) and use_conversation_history}")

            if self.conversation and use_conversation_history:
                messages = self.conversation.format_for_llm(system_prompt, user_prompt)
            else:
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ]

            completion = self.pipeline.client.chat.completions.create(
                model=self.pipeline.llm_model_name,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            response = (completion.choices[0].message.content or "").strip()
            if not response:
                raise ValueError("LLM returned an empty response")

            token_stats = normalize_token_usage(messages, response, completion.usage)
            self.pipeline.total_prompt_tokens += token_stats["prompt_tokens"]
            self.pipeline.total_completion_tokens += token_stats["completion_tokens"]
            self.pipeline.total_tokens += token_stats["total_tokens"]

            print("\n=== LLM response ===")
            print(response)
            print("\n=== Token usage ===")
            print(f"prompt_tokens: {token_stats['prompt_tokens']}")
            print(f"completion_tokens: {token_stats['completion_tokens']}")
            print(f"total_tokens: {token_stats['total_tokens']}")
            if token_stats["used_estimated_prompt"] or token_stats["used_estimated_completion"]:
                print(
                    "Token usage was estimated because provider usage was missing or invalid "
                    f"(provider_prompt={token_stats['provider_prompt_tokens']}, "
                    f"provider_completion={token_stats['provider_completion_tokens']})."
                )
            print("===================\n")

            if self.conversation:
                self.conversation.add_message(self.name, response)
            return response
        except Exception as exc:
            logger.error("LLM call failed: %s", exc)
            raise

    def augment_prompt(self, query: str, mode: str = "generate") -> str:
        return self.pipeline._augment_prompt(query, mode)


class RequirementsAnalystAgent(BaseAgent):
    """Extract conservative atomic propositions from natural-language requirements."""

    def __init__(self, pipeline):
        super().__init__("analyst", pipeline)

    def parse_requirements(self, user_requirements: str) -> Dict[str, Any]:
        print(f"[{self.name}] Parsing requirements...")
        if not user_requirements.strip():
            error_msg = "User requirements are empty"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}

        prompt = self.augment_prompt(
            "Extract candidate atomic propositions from the requirement below.\n"
            "Rules:\n"
            "- Output one proposition per line.\n"
            "- Each proposition must be a minimal truth-valued expression.\n"
            "- Do not generate AGREE code.\n"
            "- Do not invent ports, components, subcomponents, or functions.\n"
            "- If exact AADL names are unknown, use clear semantic placeholders.\n"
            "- Do not return Markdown, JSON, bullets, explanations, or code fences.\n\n"
            f"Requirement:\n{user_requirements}",
            mode="generate",
        )
        system_prompt = (
            "You are a formal requirements analyst. Your task is to decompose natural-language "
            "requirements into minimal candidate atomic propositions. Be conservative: only "
            "extract behavior that is explicitly stated."
        )

        try:
            result = self.call_llm(system_prompt, prompt, temperature=0.2, max_tokens=4000)
            self.pipeline.state["atomic_propositions"] = result
            print(f"[{self.name}] Atomic proposition extraction completed")
            return {"success": True, "result": result}
        except Exception as exc:
            error_msg = f"Requirement analysis failed: {exc}"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}


class AGREEGeneratorAgent(BaseAgent):
    """Generate AGREE annex fragments for the target component."""

    def __init__(self, pipeline):
        super().__init__("generator", pipeline)

    def _strip_reasoning_text(self, text: str) -> str:
        text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"```(?:aadl|agree|text|python)?", "```", text, flags=re.IGNORECASE)
        return text.strip()

    def _iter_code_blocks(self, text: str) -> List[str]:
        return [m.group(1).strip() for m in re.finditer(r"```[a-zA-Z0-9_-]*\s*(.*?)```", text, re.DOTALL)]

    def _find_annex_blocks(self, text: str) -> List[str]:
        blocks = []
        pattern = re.compile(r"annex\s+agree\s*\{\*\*(.*?)\*\*\}\s*;", re.IGNORECASE | re.DOTALL)
        for match in pattern.finditer(text):
            blocks.append(f"annex agree {{**\n{match.group(1).strip()}\n**}};")
        return blocks

    def _normalize_annex_block(self, text: str) -> str:
        text = text.strip()
        if re.search(r"annex\s+agree\s*\{\*\*", text, re.IGNORECASE):
            blocks = self._find_annex_blocks(text)
            if blocks:
                return blocks[0]
        if text.startswith("{**") and text.endswith("**};"):
            return "annex agree " + text
        if text.startswith("{**") and text.endswith("**}"):
            return "annex agree " + text + ";"
        return f"annex agree {{**\n{text}\n**}};"

    def _first_annex_from_text(self, text: str) -> str:
        clean = self._strip_reasoning_text(text)
        for block in self._iter_code_blocks(clean):
            annexes = self._find_annex_blocks(block)
            if annexes:
                return annexes[0]
        annexes = self._find_annex_blocks(clean)
        if annexes:
            return annexes[0]
        return ""

    def _extract_agree_sections(self, result: str) -> tuple[str, str]:
        clean = self._strip_reasoning_text(result)
        system_agree = ""
        implementation_agree = ""

        try:
            data = json.loads(clean)
            system_agree = str(data.get("system_type_annex", "") or "").strip()
            implementation_agree = str(data.get("implementation_annex", "") or "").strip()
        except Exception:
            pass

        if not system_agree and not implementation_agree:
            blocks = []
            for code in self._iter_code_blocks(clean) or [clean]:
                blocks.extend(self._find_annex_blocks(code))
            if len(blocks) == 1:
                implementation_agree = blocks[0]
            elif len(blocks) >= 2:
                system_agree = blocks[0]
                implementation_agree = blocks[1]

        if system_agree:
            system_agree = self._normalize_annex_block(system_agree)
        if implementation_agree:
            implementation_agree = self._normalize_annex_block(implementation_agree)
        return system_agree, implementation_agree

    def generate_spec(self, target_component: Optional[str] = None) -> Dict[str, Any]:
        if target_component is None:
            target_component = self.pipeline._infer_target_component()
            if not target_component:
                error_msg = "Unable to infer target component"
                logger.error(error_msg)
                return {"success": False, "error": error_msg}

        system_name = target_component.replace(".impl", "").replace(".Impl", "")
        implementation_name = target_component if "." in target_component else f"{system_name}.impl"
        requirements = self.pipeline.state.get("user_requirements", "")
        atomic_props = self.pipeline.state.get("atomic_propositions", "")
        aadl_analysis = self.pipeline.state.get("aadl_analysis", {})
        aadl_model = self.pipeline.state.get("raw_aadl_snippet", "")

        prompt = self.augment_prompt(
            "Generate AGREE annex code for the specified AADL component.\n\n"
            f"Target component type: {system_name}\n"
            f"Target implementation: {implementation_name}\n\n"
            "Natural-language requirement:\n"
            f"{requirements}\n\n"
            "Candidate atomic propositions:\n"
            f"{atomic_props}\n\n"
            "AADL model analysis JSON:\n"
            f"{json.dumps(aadl_analysis, ensure_ascii=True, indent=2)}\n\n"
            "Relevant AADL model:\n"
            f"```aadl\n{aadl_model}\n```\n\n"
            "Output contract:\n"
            "- Return JSON with keys system_type_annex and implementation_annex.\n"
            "- Each value must be either an empty string or a complete annex agree {** ... **}; block.\n"
            "- Put assume/guarantee/eq/const only in the system type annex.\n"
            "- Put assign/lemma/assert only in the implementation annex.\n"
            "- Do not reference subcomponent ports inside system type guarantees.\n"
            "- Do not invent ports, data types, functions, packages, or subcomponents.\n"
            "- If no safe implementation-level statement is needed, set implementation_annex to an empty string.\n"
            "- Return only JSON. No Markdown or explanations.",
            mode="generate",
        )
        system_prompt = (
            "You are an AGREE specification engineer. Generate syntactically valid AGREE annex "
            "fragments that are conservative with respect to the provided AADL model."
        )

        try:
            result = self.call_llm(system_prompt, prompt, temperature=0.2, max_tokens=10000)
            self.pipeline.state["agree_generator_raw_output"] = result
            system_agree, implementation_agree = self._extract_agree_sections(result)
            if system_agree or implementation_agree:
                self.pipeline.state["agree_code_system"] = system_agree
                self.pipeline.state["agree_code_implementation"] = implementation_agree
                self.pipeline.state["agree_code"] = implementation_agree or system_agree
                return {
                    "success": True,
                    "result": {
                        "system_type_annex": system_agree,
                        "implementation_annex": implementation_agree,
                    },
                }
            self.pipeline.state["agree_generator_parse_failure_output"] = result
            return {"success": False, "error": "No AGREE annex block could be extracted from generator output"}
        except Exception as exc:
            error_msg = f"AGREE generation failed: {exc}"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}


class AADLModelAnalystAgent(BaseAgent):
    """Analyze the AADL model and return a structured JSON summary."""

    def __init__(self, pipeline):
        super().__init__("model_analyst", pipeline)

    def _extract_first_json_object(self, text: str) -> str:
        start = text.find("{")
        if start < 0:
            raise ValueError("No JSON object start found")
        depth = 0
        in_string = False
        escape = False
        for idx in range(start, len(text)):
            char = text[idx]
            if in_string:
                if escape:
                    escape = False
                elif char == "\\":
                    escape = True
                elif char == '"':
                    in_string = False
            else:
                if char == '"':
                    in_string = True
                elif char == "{":
                    depth += 1
                elif char == "}":
                    depth -= 1
                    if depth == 0:
                        return text[start : idx + 1]
        raise ValueError("No complete JSON object found")

    def _close_truncated_json_prefix(self, text: str) -> str:
        cleaned = text.strip()
        stack = []
        in_string = False
        escape = False
        for char in cleaned:
            if in_string:
                if escape:
                    escape = False
                elif char == "\\":
                    escape = True
                elif char == '"':
                    in_string = False
            else:
                if char == '"':
                    in_string = True
                elif char in "{[":
                    stack.append("}" if char == "{" else "]")
                elif char in "}]":
                    if stack and stack[-1] == char:
                        stack.pop()
        if in_string:
            cleaned += '"'
        cleaned += "".join(reversed(stack))
        return cleaned

    def analyze_model_structure(self, aadl_model: str) -> Dict[str, Any]:
        print(f"[{self.name}] Analyzing AADL model structure...")
        self.pipeline.state["raw_aadl_snippet"] = aadl_model.strip()
        self.pipeline.state["aadl_analysis"] = {}

        prompt = self.augment_prompt(
            "Analyze the AADL model and return only JSON.\n\n"
            "Schema:\n"
            "{\n"
            '  "package": "package name",\n'
            '  "imports": ["package names from with clauses"],\n'
            '  "components": [\n'
            "    {\n"
            '      "name": "component type name",\n'
            '      "kind": "system|thread|process|device|data|other",\n'
            '      "features": [{"name": "port name", "direction": "in|out", "category": "data port|event port|other", "type": "qualified type"}],\n'
            '      "implementations": ["implementation names"]\n'
            "    }\n"
            "  ],\n"
            '  "connections": [{"name": "connection name", "source": "source endpoint", "destination": "destination endpoint"}],\n'
            '  "target_candidates": ["component implementation names that may accept AGREE annexes"]\n'
            "}\n\n"
            "Rules:\n"
            "- Use only information present in the AADL text.\n"
            "- Do not invent components, ports, or connections.\n"
            "- Return valid JSON only. No Markdown.\n\n"
            f"AADL model:\n```aadl\n{aadl_model}\n```",
            mode="generate",
        )
        system_prompt = "You are an AADL model analyst. Return precise JSON and no explanatory text."

        try:
            result = self.call_llm(system_prompt, prompt, temperature=0.1, max_tokens=10000, use_conversation_history=False)
            json_text = self._extract_first_json_object(result)
            try:
                parsed = json.loads(json_text)
            except json.JSONDecodeError:
                parsed = json.loads(self._close_truncated_json_prefix(json_text))
            if not isinstance(parsed, dict):
                raise ValueError("AADL analysis response is not a JSON object")
            parsed.setdefault("components", [])
            parsed.setdefault("connections", [])
            parsed.setdefault("imports", [])
            parsed.setdefault("target_candidates", [])
            self.pipeline.state["aadl_analysis"].update(parsed)
            self.pipeline.state["components_list"] = [comp.get("name", "unnamed_component") for comp in parsed["components"]]
            print(f"[{self.name}] AADL model analysis completed")
            return {"success": True, "result": parsed}
        except Exception as exc:
            error_msg = f"AADL model analysis failed: {exc}"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}


class AADLMergeAgent(BaseAgent):
    """Insert generated AGREE annex blocks into a complete AADL model."""

    def __init__(self, pipeline):
        super().__init__("merger", pipeline)

    def _strip_reasoning_text(self, text: str) -> str:
        return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE).strip()

    def _extract_aadl_model(self, response: str) -> str:
        clean = self._strip_reasoning_text(response)
        blocks = re.findall(r"```(?:aadl|text)?\s*(.*?)```", clean, flags=re.DOTALL | re.IGNORECASE)
        for block in blocks:
            if re.search(r"\bpackage\b", block, re.IGNORECASE) and re.search(r"\bend\s+\w+\s*;", block, re.IGNORECASE):
                return block.strip()
        return clean.strip()

    def _is_plausible_full_aadl(self, code: str, original_aadl: str) -> tuple[bool, str]:
        if not code.strip():
            return False, "empty model"
        if not re.search(r"\bpackage\b", code, re.IGNORECASE):
            return False, "missing package declaration"
        if len(code) < max(100, int(len(original_aadl) * 0.6)):
            return False, "model is unexpectedly short"
        return True, ""

    def merge_spec_into_model(self, target_component: Optional[str] = None) -> Dict[str, Any]:
        original_aadl = self.pipeline.state.get("raw_aadl_snippet", "")
        system_annex = self.pipeline.state.get("agree_code_system", "")
        implementation_annex = self.pipeline.state.get("agree_code_implementation", "")
        agree_code = self.pipeline.state.get("agree_code", "")
        if not original_aadl.strip():
            return {"success": False, "error": "Original AADL model is missing"}
        if not (system_annex or implementation_annex or agree_code):
            return {"success": False, "error": "Generated AGREE annex is missing"}

        prompt = (
            "Insert the generated AGREE annex block(s) into the full AADL model.\n\n"
            f"Target component: {target_component or self.pipeline._infer_target_component() or 'unknown'}\n\n"
            "System type annex:\n"
            f"{system_annex}\n\n"
            "Implementation annex:\n"
            f"{implementation_annex or agree_code}\n\n"
            "Original AADL model:\n"
            f"```aadl\n{original_aadl}\n```\n\n"
            "Rules:\n"
            "- Return the complete modified AADL model only.\n"
            "- Preserve package name, imports, features, subcomponents, and connections unless required by the annex insertion.\n"
            "- Do not invent new ports, subcomponents, packages, or data types.\n"
            "- Put system type annexes before the matching 'end <component>;'.\n"
            "- Put implementation annexes before the matching 'end <component.impl>;'.\n"
            "- Keep the exact annex agree {** ... **}; delimiters.\n"
            "- No explanations and no Markdown."
        )
        system_prompt = "You are an AADL source editor. Only perform the requested annex insertion."

        try:
            merged_output = self.call_llm(system_prompt, prompt, temperature=0.1, max_tokens=16000, use_conversation_history=False)
            self.pipeline.state["merge_raw_output"] = merged_output
            merged_aadl = self._extract_aadl_model(merged_output)
            valid, reason = self._is_plausible_full_aadl(merged_aadl, original_aadl)
            if not valid:
                self.pipeline.state["merge_rejected_reason"] = reason
                return {"success": False, "error": f"Merged AADL was rejected: {reason}"}
            self.pipeline.state["merged_aadl"] = merged_aadl
            return {"success": True, "result": merged_aadl}
        except Exception as exc:
            error_msg = f"AADL merge failed: {exc}"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}


class AADLValidatorAgent(BaseAgent):
    """Repair AADL/AGREE code according to validator diagnostics."""

    def __init__(self, pipeline):
        super().__init__("validator", pipeline)

    def validate_and_fix(self, error_level_info: Dict = None) -> Dict[str, Any]:
        return self._validate_and_fix(error_level_info=error_level_info or {})

    def _strip_reasoning_text(self, text: str) -> str:
        return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE).strip()

    def _extract_repaired_code(self, response: str) -> str:
        clean = self._strip_reasoning_text(response)
        blocks = re.findall(r"```(?:aadl|text)?\s*(.*?)```", clean, flags=re.DOTALL | re.IGNORECASE)
        for block in blocks:
            if re.search(r"\bpackage\b", block, re.IGNORECASE):
                return block.strip()
        return clean.strip()

    def _is_plausible_full_aadl(self, code: str, previous_code: str) -> tuple[bool, str]:
        if not code.strip():
            return False, "empty repaired model"
        if not re.search(r"\bpackage\b", code, re.IGNORECASE):
            return False, "missing package declaration"
        if len(code) < max(100, int(len(previous_code) * 0.5)):
            return False, "repaired model is unexpectedly short"
        return True, ""

    def _validate_and_fix(
        self,
        aadl_errors: str = "",
        has_aadl_errors: bool = False,
        has_agree_errors: bool = False,
        error_level_info: Dict = None,
    ) -> Dict[str, Any]:
        error_level_info = error_level_info or {}
        current_code = self.pipeline.state.get("merged_aadl", "")
        if not current_code.strip():
            return {"success": False, "error": "No merged AADL model is available for repair"}

        diagnostics = error_level_info.get("formatted_errors") or aadl_errors or json.dumps(error_level_info, ensure_ascii=True, indent=2)
        raw_output = error_level_info.get("raw_validator_output") or ""

        prompt = self.augment_prompt(
            "Repair the following AADL+AGREE model using only the reported diagnostics.\n\n"
            "Diagnostics:\n"
            f"{diagnostics}\n\n"
            "Raw validator output:\n"
            f"{raw_output}\n\n"
            "Current AADL+AGREE model:\n"
            f"```aadl\n{current_code}\n```\n\n"
            "Repair rules:\n"
            "- Return the complete repaired AADL model only.\n"
            "- Preserve original functionality and architecture.\n"
            "- Fix only issues indicated by the diagnostics.\n"
            "- Do not delete annex agree {** ... **}; delimiters.\n"
            "- Do not invent missing packages or data types unless the diagnostic explicitly requires a local declaration.\n"
            "- Do not include explanations, Markdown, or JSON.",
            mode="generate",
        )
        system_prompt = (
            "You are an AADL and AGREE repair engineer. Apply the smallest safe patch that "
            "addresses validator diagnostics."
        )

        try:
            result = self.call_llm(system_prompt, prompt, temperature=0.1, max_tokens=16000, use_conversation_history=False)
            self.pipeline.state["last_repair_raw_output"] = result
            repaired_code = self._extract_repaired_code(result)
            valid, reason = self._is_plausible_full_aadl(repaired_code, current_code)
            if not valid:
                self.pipeline.state["last_repair_rejected_reason"] = reason
                return {"success": False, "error": f"Repaired model was rejected: {reason}"}

            output_file_path = self.pipeline.state.get("final_model_path")
            if output_file_path:
                with open(output_file_path, "w", encoding="utf-8") as file:
                    file.write(repaired_code)
            self.pipeline.state["merged_aadl"] = repaired_code
            return {"success": True, "result": repaired_code}
        except Exception as exc:
            error_msg = f"Validation repair failed: {exc}"
            logger.error(error_msg)
            return {"success": False, "error": error_msg}
