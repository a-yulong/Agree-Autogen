"""LLM-backed agents for the refactored pipeline."""

from __future__ import annotations

import json
import http.client
import os
import re
import time
import traceback
import urllib.error
import urllib.request
from types import SimpleNamespace
from typing import Any, Dict

from ..runtime import normalize_token_usage
from .config import RAG_QUERIES, RuntimeConfig
from .output_recovery import recover_json_object, recover_section
from .output_recovery import extract_annex_blocks
from .prompting import (
    PromptLibrary,
    extract_section,
    normalize_agree_annex_delimiters,
    strip_code_fence,
)
from .rag_bundle import RagBundleBuilder
from .state import DISABLED, PipelineState


class LLMCallError(RuntimeError):
    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        response_text: str = "",
        headers: dict[str, str] | None = None,
    ):
        super().__init__(message)
        self.status_code = status_code
        self.response_text = response_text
        self.headers = headers or {}


def split_target_component_names(target_component: str | None, aadl_model: str) -> tuple[str, str]:
    """Return (component type, component implementation) using the target extracted from the requirement."""
    target = (target_component or "").strip()
    if target:
        if "." in target:
            component = target.split(".", 1)[0]
            if _implementation_exists(target, aadl_model):
                return component, target
            return component, _find_matching_implementation(component, aadl_model)
        implementation = _find_matching_implementation(target, aadl_model)
        return target, implementation
    component = _infer_first_component_type(aadl_model)
    implementation = _find_matching_implementation(component, aadl_model)
    return component, implementation


def _implementation_exists(name: str, aadl_model: str) -> bool:
    return bool(
        re.search(
            rf"^\s*(?:system|process|thread|device|abstract|subprogram)\s+implementation\s+{re.escape(name)}\b",
            aadl_model or "",
            flags=re.IGNORECASE | re.MULTILINE,
        )
    )


def _find_matching_implementation(component: str, aadl_model: str) -> str:
    pattern = re.compile(
        r"^\s*(?:system|process|thread|device|abstract|subprogram)\s+implementation\s+([A-Za-z_][A-Za-z0-9_.]*)\b",
        re.IGNORECASE | re.MULTILINE,
    )
    normalized_component = re.sub(r"[^A-Za-z0-9_]", "", component or "").lower()
    matches = []
    for match in pattern.finditer(aadl_model or ""):
        name = match.group(1)
        normalized_name = re.sub(r"[^A-Za-z0-9_]", "", name).lower()
        if normalized_name.startswith(normalized_component):
            matches.append(name)
    return max(matches, key=len) if matches else ""


def _infer_first_component_type(aadl_model: str) -> str:
    match = re.search(
        r"^\s*(?:system|process|thread|device|abstract|subprogram)\s+([A-Za-z_][A-Za-z0-9_]*)\b",
        aadl_model or "",
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if not match:
        raise ValueError("Unable to infer component type.")
    return match.group(1)


class AgentRuntime:
    """Shared LLM client, prompt library, RAG builder, and token accounting."""

    def __init__(self, config: RuntimeConfig):
        if not config.model_api_key:
            raise ValueError("AGREE_MODEL_API_KEY is not configured.")
        self.config = config
        self.prompts = PromptLibrary()
        self.rag = RagBundleBuilder(config.knowledge_base)
        self.debug_prompts = os.environ.get("AGREE_DEBUG_PROMPTS", "").lower() in {"1", "true", "yes", "on"}
        self.debug_inputs_only = os.environ.get("AGREE_DEBUG_LLM_INPUTS_ONLY", "").lower() in {"1", "true", "yes", "on"}
        self.debug_inputs_verbose = os.environ.get("AGREE_DEBUG_LLM_INPUTS_VERBOSE", "").lower() in {"1", "true", "yes", "on"}
        self.debug_save_outputs = os.environ.get("AGREE_DEBUG_SAVE_LLM_OUTPUTS", "").lower() in {"1", "true", "yes", "on"}
        self.call_counter = 0

    def call(
        self,
        state: PipelineState,
        system_prompt: str,
        user_prompt: str,
        temperature: float | None = None,
        stage_name: str = "llm_call",
        max_tokens: int | None = None,
    ) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        self.call_counter += 1
        if self.debug_prompts or self.debug_inputs_only or self.debug_save_outputs:
            self._debug_llm_request(state, stage_name, system_prompt, user_prompt, temperature)
        request_kwargs = {
            "model": self.config.model_name,
            "messages": messages,
            "temperature": self.config.temperature if temperature is None else temperature,
        }
        effective_max_tokens = max_tokens if max_tokens is not None else self.config.max_tokens
        max_completion_tokens = os.environ.get("AGREE_MAX_COMPLETION_TOKENS", "").strip()
        if max_completion_tokens:
            request_kwargs["max_completion_tokens"] = int(max_completion_tokens)
        elif effective_max_tokens is not None:
            request_kwargs["max_tokens"] = effective_max_tokens
        max_retries = int(os.environ.get("AGREE_LLM_MAX_RETRIES", "2"))
        last_error: Exception | None = None
        payload = None
        for attempt in range(1, max_retries + 2):
            try:
                payload = self._direct_chat_completion(request_kwargs)
                break
            except Exception as exc:
                last_error = exc
                self._save_llm_failure(state, stage_name, attempt, exc)
                if attempt > max_retries:
                    raise RuntimeError(
                        f"LLM call failed at stage '{stage_name}' after {attempt} attempt(s): {exc}"
                    ) from exc
                time.sleep(min(2 * attempt, 6))
        if payload is None:
            raise RuntimeError(f"LLM call failed at stage '{stage_name}': {last_error}")
        try:
            choice = payload["choices"][0]
            message = choice.get("message", {}) or {}
            content = message.get("content")
            if isinstance(content, list):
                response = "\n".join(
                    str(part.get("text") or part.get("content") or "")
                    for part in content
                    if isinstance(part, dict)
                ).strip()
            else:
                response = str(content or "").strip()
        except Exception as exc:
            raise LLMCallError(
                f"LLM response JSON did not contain choices[0].message.content: {exc}",
                response_text=json.dumps(payload, ensure_ascii=False)[:4000],
            ) from exc
        if not response:
            self._save_empty_llm_payload(state, stage_name, payload)
            finish_reason = choice.get("finish_reason")
            message_keys = sorted(message.keys()) if isinstance(message, dict) else []
            usage = payload.get("usage") or {}
            raise LLMCallError(
                "LLM returned an empty response "
                f"(finish_reason={finish_reason}, message_keys={message_keys}, usage={usage}).",
                response_text=json.dumps(payload, ensure_ascii=False)[:8000],
            )
        usage_payload = payload.get("usage") or {}
        usage = normalize_token_usage(messages, response, SimpleNamespace(**usage_payload))
        state.token_stats.add(usage)
        if self.debug_save_outputs or self.debug_prompts:
            self._save_llm_response(state, stage_name, response)
        if self.debug_prompts and not self.debug_inputs_only:
            print("\n" + "=" * 80, flush=True)
            print("LLM RESPONSE", flush=True)
            print("=" * 80, flush=True)
            print(response, flush=True)
            print("=" * 80 + "\n", flush=True)
        return response

    def _direct_chat_completion(self, request_kwargs: dict[str, Any]) -> dict[str, Any]:
        base_url = self.config.model_base_url.rstrip("/")
        wire_api = os.environ.get("AGREE_MODEL_WIRE_API", "chat_completions").strip().lower().replace("-", "_")
        if wire_api == "responses":
            return self._direct_responses_completion(request_kwargs)
        url = f"{base_url}/chat/completions"
        body = json.dumps(request_kwargs, ensure_ascii=False).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.config.model_api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "AGREE-AutoGen/2.0",
        }
        referer = os.environ.get("OPENROUTER_HTTP_REFERER") or os.environ.get("HTTP_REFERER")
        title = os.environ.get("OPENROUTER_TITLE") or "AGREE-AutoGen"
        if "openrouter.ai" in base_url:
            if referer:
                headers["HTTP-Referer"] = referer
            headers["X-OpenRouter-Title"] = title
        timeout = float(os.environ.get("AGREE_LLM_TIMEOUT_SECONDS", "240"))
        request = urllib.request.Request(url, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status_code = response.getcode()
                response_headers = dict(response.headers.items())
                response_body = self._read_response_with_deadline(response, timeout, status_code, response_headers)
                response_text = response_body.decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            response_text = exc.read().decode("utf-8", errors="replace")
            raise LLMCallError(
                f"HTTP {exc.code} from LLM provider.",
                status_code=exc.code,
                response_text=response_text,
                headers=dict(exc.headers.items()) if exc.headers else {},
            ) from exc
        except urllib.error.URLError as exc:
            raise LLMCallError(f"Network error from LLM provider: {exc}") from exc

        if status_code < 200 or status_code >= 300:
            raise LLMCallError(
                f"HTTP {status_code} from LLM provider.",
                status_code=status_code,
                response_text=response_text,
                headers=response_headers,
            )
        try:
            payload = json.loads(response_text)
        except json.JSONDecodeError as exc:
            raise LLMCallError(
                f"LLM provider returned non-JSON response at line {exc.lineno}, column {exc.colno}: {exc.msg}",
                status_code=status_code,
                response_text=response_text,
                headers=response_headers,
            ) from exc
        if not isinstance(payload, dict):
            raise LLMCallError(
                "LLM provider returned JSON that is not an object.",
                status_code=status_code,
                response_text=response_text,
                headers=response_headers,
            )
        return payload

    def _direct_responses_completion(self, request_kwargs: dict[str, Any]) -> dict[str, Any]:
        base_url = self.config.model_base_url.rstrip("/")
        url = f"{base_url}/responses"
        input_parts: list[str] = []
        for message in request_kwargs.get("messages", []):
            role = message.get("role", "user")
            content = message.get("content", "")
            input_parts.append(f"[{role.upper()}]\n{content}")
        response_kwargs: dict[str, Any] = {
            "model": request_kwargs.get("model"),
            "input": "\n\n".join(input_parts),
        }
        if request_kwargs.get("temperature") is not None:
            response_kwargs["temperature"] = request_kwargs["temperature"]
        if request_kwargs.get("max_completion_tokens") is not None:
            response_kwargs["max_output_tokens"] = request_kwargs["max_completion_tokens"]
        elif request_kwargs.get("max_tokens") is not None:
            response_kwargs["max_output_tokens"] = request_kwargs["max_tokens"]
        body = json.dumps(response_kwargs, ensure_ascii=False).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.config.model_api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "AGREE-AutoGen/2.0",
        }
        timeout = float(os.environ.get("AGREE_LLM_TIMEOUT_SECONDS", "240"))
        request = urllib.request.Request(url, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status_code = response.getcode()
                response_headers = dict(response.headers.items())
                response_body = self._read_response_with_deadline(response, timeout, status_code, response_headers)
                response_text = response_body.decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            response_text = exc.read().decode("utf-8", errors="replace")
            raise LLMCallError(
                f"HTTP {exc.code} from LLM provider.",
                status_code=exc.code,
                response_text=response_text,
                headers=dict(exc.headers.items()) if exc.headers else {},
            ) from exc
        except urllib.error.URLError as exc:
            raise LLMCallError(f"Network error from LLM provider: {exc}") from exc

        if status_code < 200 or status_code >= 300:
            raise LLMCallError(
                f"HTTP {status_code} from LLM provider.",
                status_code=status_code,
                response_text=response_text,
                headers=response_headers,
            )
        try:
            payload = json.loads(response_text)
        except json.JSONDecodeError as exc:
            raise LLMCallError(
                f"LLM provider returned non-JSON response at line {exc.lineno}, column {exc.colno}: {exc.msg}",
                status_code=status_code,
                response_text=response_text,
                headers=response_headers,
            ) from exc
        if not isinstance(payload, dict):
            raise LLMCallError(
                "LLM provider returned JSON that is not an object.",
                status_code=status_code,
                response_text=response_text,
                headers=response_headers,
            )
        text = self._extract_responses_text(payload)
        if not text:
            raise LLMCallError("LLM returned an empty response.", response_text=response_text[:4000])
        usage = payload.get("usage") or {}
        return {
            "choices": [{"message": {"content": text}}],
            "usage": {
                "prompt_tokens": usage.get("input_tokens", usage.get("prompt_tokens", 0)),
                "completion_tokens": usage.get("output_tokens", usage.get("completion_tokens", 0)),
                "total_tokens": usage.get("total_tokens", 0),
            },
            "_raw_responses_payload": payload,
        }

    @staticmethod
    def _extract_responses_text(payload: dict[str, Any]) -> str:
        if isinstance(payload.get("output_text"), str):
            return payload["output_text"].strip()
        chunks: list[str] = []
        for item in payload.get("output") or []:
            if not isinstance(item, dict):
                continue
            for content in item.get("content") or []:
                if isinstance(content, dict) and isinstance(content.get("text"), str):
                    chunks.append(content["text"])
        return "\n".join(chunks).strip()

    def _read_response_with_deadline(self, response: Any, timeout: float, status_code: int, response_headers: dict[str, str]) -> bytes:
        """Read provider responses with an absolute deadline.

        Some OpenRouter upstreams occasionally keep a chunked HTTP 200 response
        alive while sending only whitespace. A plain response.read() can hang for
        far longer than the intended request timeout in that situation because
        each whitespace chunk refreshes the socket read. Reading in chunks lets
        us enforce a whole-response deadline and keep the batch supervisor moving.
        """
        read_timeout = float(os.environ.get("AGREE_LLM_SOCKET_READ_TIMEOUT_SECONDS", "20"))
        absolute_timeout = float(os.environ.get("AGREE_LLM_ABSOLUTE_TIMEOUT_SECONDS", str(max(timeout, 300.0))))
        try:
            sock = getattr(getattr(response, "fp", None), "raw", None)
            sock = getattr(sock, "_sock", None)
            if sock is not None:
                sock.settimeout(read_timeout)
        except Exception:
            pass
        deadline = time.monotonic() + absolute_timeout
        chunks: list[bytes] = []
        while True:
            if time.monotonic() > deadline:
                partial = b"".join(chunks)
                raise LLMCallError(
                    f"LLM provider response exceeded absolute read deadline ({absolute_timeout:.0f}s).",
                    status_code=status_code,
                    response_text=partial.decode("utf-8", errors="replace")[:8000],
                    headers=response_headers,
                )
            try:
                chunk = response.read(65536)
            except http.client.IncompleteRead as exc:
                if exc.partial:
                    chunks.append(exc.partial)
                    break
                partial = b"".join(chunks)
                if partial:
                    break
                raise LLMCallError(
                    "LLM provider returned an incomplete HTTP response with no recoverable body.",
                    status_code=status_code,
                    response_text="",
                    headers=response_headers,
                ) from exc
            except (TimeoutError, OSError) as exc:
                partial = b"".join(chunks)
                raise LLMCallError(
                    f"Timed out while reading LLM provider response chunk: {exc}",
                    status_code=status_code,
                    response_text=partial.decode("utf-8", errors="replace")[:8000],
                    headers=response_headers,
                ) from exc
            if not chunk:
                break
            chunks.append(chunk)
        body = b"".join(chunks)
        if not body.strip():
            raise LLMCallError(
                "LLM provider returned a whitespace-only response body.",
                status_code=status_code,
                response_text=body.decode("utf-8", errors="replace")[:8000],
                headers=response_headers,
            )
        return body

    def rag_context(
        self,
        state: PipelineState,
        agent_name: str,
        enabled: bool,
        diagnostic_context: str = "",
        retrieval_requirement: str | None = None,
    ) -> str:
        queries = RAG_QUERIES[agent_name]
        if os.environ.get("AGREE_RAG_ENHANCED", "1").lower() in {"1", "true", "yes", "on"}:
            bundle = self.rag.build_enhanced(
                queries=queries,
                enabled=enabled,
                requirement=retrieval_requirement or state.raw_requirement,
                aadl_context=state.raw_aadl,
                target_component=state.target_component,
                agent_name=agent_name,
                model_analysis=state.model_analysis,
                diagnostic_context=diagnostic_context,
            )
            context = bundle["context"]
            state.rag_bundles[agent_name] = bundle["metadata"]
            self._save_rag_debug(state, agent_name, bundle.get("debug", {}))
        else:
            context = self.rag.build(queries, enabled)
            state.rag_bundles[agent_name] = self.rag.selected_metadata(queries, enabled)
        context = self._digest_rag_context(
            state,
            agent_name,
            context,
            enabled,
            diagnostic_context=diagnostic_context,
            retrieval_requirement=retrieval_requirement,
        )
        if self.debug_prompts and not self.debug_inputs_only:
            print("\n" + "=" * 80, flush=True)
            print(f"RAG DIGEST FOR {agent_name}", flush=True)
            print("=" * 80, flush=True)
            print(context if context else "RAG disabled or empty.", flush=True)
            print("=" * 80 + "\n", flush=True)
        return context

    def _digest_rag_context(
        self,
        state: PipelineState,
        agent_name: str,
        raw_context: str,
        enabled: bool,
        *,
        diagnostic_context: str = "",
        retrieval_requirement: str | None = None,
    ) -> str:
        if not enabled or not raw_context or raw_context == "RAG_DISABLED":
            return raw_context
        if os.environ.get("AGREE_RAG_DIGEST", "1").lower() not in {"1", "true", "yes", "on"}:
            return raw_context
        available_symbols = self._compile_available_symbols(state, None)
        prompt = self.prompts.render(
            "rag_digest",
            agent_name=agent_name,
            agent_task=self._agent_task_summary(agent_name),
            requirement_text=retrieval_requirement or state.raw_requirement,
            target_component=state.target_component or "NONE",
            available_symbols=available_symbols,
            diagnostic_context=diagnostic_context or "No validator diagnostics are active.",
            raw_rag_context=raw_context,
        )
        response = self.call(
            state,
            (
                "Digest retrieved RAG cards into concise, agent-specific guidance. "
                "Return exactly one JSON object and do not solve the case."
            ),
            prompt,
            temperature=0.0,
            stage_name=f"rag_digest_{agent_name}",
            max_tokens=900,
        )
        recovered = recover_json_object(
            response,
            f"rag_digest_{agent_name}",
            defaults={
                "rag_rules": [],
                "generic_rules": [],
                "syntax_or_pattern_reminders": [],
                "anti_patterns": [],
                "irrelevant_topics": [],
            },
        )
        self.record_recovery(state, f"rag_digest_{agent_name}", recovered.actions)
        payload = recovered.value if isinstance(recovered.value, dict) else {}
        digest = self._format_rag_digest(agent_name, payload)
        debug_dir = state.report_dir(self.config.result_root) / "rag_debug"
        debug_dir.mkdir(parents=True, exist_ok=True)
        safe_agent = re.sub(r"[^A-Za-z0-9_.-]+", "_", agent_name).strip("_") or "agent"
        (debug_dir / f"{safe_agent}_rag_digest.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
            errors="replace",
        )
        (debug_dir / f"{safe_agent}_rag_digest.txt").write_text(digest, encoding="utf-8", errors="replace")
        return digest

    def _agent_task_summary(self, agent_name: str) -> str:
        tasks = {
            "model_analyst": "Extract factual AADL structure: components, implementations, features, ports, connections, and visible identifiers.",
            "requirement_analyst": "Summarize the natural-language requirement into compact semantic items grounded in visible model names.",
            "agree_generator": "Generate syntactically valid AGREE annex blocks from the raw requirement, semantic items, model facts, and visible symbols.",
            "model_fusion": "Insert generated AGREE annex blocks into the intended target component or implementation while preserving AADL architecture.",
            "validation_repair": "Turn validator diagnostics into precise repairs and execute them without changing unrelated architecture.",
        }
        return tasks.get(agent_name, "Use retrieved knowledge only as concise task-specific guidance.")

    def strategy_guidance_enabled(self) -> bool:
        return os.environ.get("AGREE_AGENT_STRATEGY_GUIDANCE", "1").lower() in {"1", "true", "yes", "on"}

    def _format_rag_digest(self, agent_name: str, payload: dict[str, Any]) -> str:
        sections = [f"<RAG_DIGEST agent=\"{agent_name}\">"]
        if agent_name == "agree_generator":
            labels = [
                ("rag_rules", "RAG rules"),
                ("generic_rules", "Generic rules"),
                ("syntax_or_pattern_reminders", "Syntax or pattern reminders"),
                ("anti_patterns", "Anti-patterns"),
            ]
            wrote_any = False
            for key, title in labels:
                values = payload.get(key, [])
                if isinstance(values, str):
                    values = [values]
                if not isinstance(values, list):
                    values = []
                cleaned = [re.sub(r"\s+", " ", str(item)).strip() for item in values if str(item).strip()]
                if not cleaned:
                    continue
                wrote_any = True
                sections.append(f"{title}:")
                sections.extend(f"- {item[:360]}" for item in cleaned[:20])
            if not wrote_any:
                sections.append("RAG rules:")
                sections.append("- Use only visible target-interface symbols.")
                sections.append("- Do not encode AADL properties, units, or type names.")
                sections.append("- Use annex agree {** ... **}; syntax.")
            sections.append("</RAG_DIGEST>")
            return "\n".join(sections)
        labels = [
            ("generic_rules", "Generic rules"),
            ("syntax_or_pattern_reminders", "Syntax or pattern reminders"),
            ("anti_patterns", "Anti-patterns"),
            ("irrelevant_topics", "Irrelevant retrieved material"),
        ]
        for key, title in labels:
            values = payload.get(key, [])
            if isinstance(values, str):
                values = [values]
            if not isinstance(values, list):
                values = []
            sections.append(f"{title}:")
            cleaned = [re.sub(r"\s+", " ", str(item)).strip() for item in values if str(item).strip()]
            if cleaned:
                sections.extend(f"- {item[:420]}" for item in cleaned[:8])
            else:
                sections.append("- None.")
        sections.append("</RAG_DIGEST>")
        return "\n".join(sections)

    def compiled_agent_context(
        self,
        state: PipelineState,
        agent_name: str,
        enabled: bool,
        *,
        visible_identifiers: list[str] | None = None,
        include_reference_context: bool = True,
        diagnostic_context: str = "",
        retrieval_requirement: str | None = None,
    ) -> dict[str, str]:
        if agent_name in {"model_analyst", "requirement_analyst"}:
            raw_context = ""
        else:
            raw_context = self.rag_context(
                state,
                agent_name,
                enabled,
                diagnostic_context=diagnostic_context,
                retrieval_requirement=retrieval_requirement,
            )
        bundle = state.rag_bundles.get(agent_name, {}) if isinstance(state.rag_bundles, dict) else {}
        rag_debug_dir = state.report_dir(self.config.result_root) / "rag_debug"
        syntax = self._load_agent_rag_cards(rag_debug_dir, agent_name, "Ksyn")
        patterns = self._load_agent_rag_cards(rag_debug_dir, agent_name, "Kexp")
        defensive = self._load_agent_rag_cards(rag_debug_dir, agent_name, "Kdef")

        if agent_name in {"model_analyst", "requirement_analyst"}:
            raw_context = ""
            syntax = []
            patterns = []
            defensive = []

        card_guidance_enabled = os.environ.get("AGREE_AGENT_CARD_GUIDANCE", "1").lower() in {"1", "true", "yes", "on"}
        compiled = {
            "retrieved_knowledge": raw_context,
            "must_follow_rules": self._compile_must_follow(agent_name, defensive) if card_guidance_enabled else "",
            "syntax_reference": self._compile_syntax_reference(agent_name, syntax) if card_guidance_enabled else "",
            "pattern_reference": self._compile_pattern_reference(agent_name, patterns) if card_guidance_enabled else "",
            "available_symbols": self._compile_available_symbols(state, visible_identifiers),
            "reference_context": self.reference_context(state) if include_reference_context else "",
            "target_model_context": "" if agent_name == "agree_generator" else self.target_model_context(state, visible_identifiers),
        }
        return compiled

    def target_model_context(self, state: PipelineState, visible_identifiers: list[str] | None = None, max_chars: int = 9000) -> str:
        """Return a compact AADL slice centered on the target component."""
        max_chars = int(os.environ.get("AGREE_TARGET_CONTEXT_MAX_CHARS", str(max_chars)))
        context_mode = os.environ.get("AGREE_TARGET_CONTEXT_MODE", "focused").lower()
        if context_mode in {"full", "raw", "all"}:
            text = state.raw_aadl or ""
            if len(text) > max_chars:
                text = text[:max_chars] + "\n-- [full model context truncated]"
            return text
        component, implementation = split_target_component_names(state.target_component, state.raw_aadl)
        names = [name for name in [component, implementation] if name]
        blocks: list[str] = []
        for name in names:
            block = self._component_block(state.raw_aadl, name)
            if block:
                blocks.append(f"-- TARGET DECLARATION: {name}\n{block}")
        related = self._related_model_lines(state.raw_aadl, names, visible_identifiers or [])
        if related:
            blocks.append("-- RELATED MODEL LINES\n" + "\n".join(related[:80]))
        if isinstance(state.model_analysis, dict):
            focused = self._focused_model_analysis(state, names)
            if focused:
                blocks.append("-- FOCUSED MODEL ANALYSIS\n" + json.dumps(focused, ensure_ascii=False, indent=2))
        text = "\n\n".join(blocks).strip()
        if not text:
            text = state.raw_aadl[:max_chars]
        if len(text) > max_chars:
            text = text[:max_chars] + "\n-- [target model context truncated]"
        return text

    def _component_block(self, aadl_model: str, name: str) -> str:
        declaration = r"(?:system|process|thread|device|abstract|subprogram|processor|data|bus)(?:\s+implementation)?"
        match = re.search(
            rf"(?ims)^\s*{declaration}\s+{re.escape(name)}\b.*?^\s*end\s+{re.escape(name)}\s*;",
            aadl_model or "",
        )
        return match.group(0).strip() if match else ""

    def _related_model_lines(self, aadl_model: str, target_names: list[str], visible_identifiers: list[str]) -> list[str]:
        names = [name for name in target_names + list(visible_identifiers) if name]
        if not names:
            return []
        related: list[str] = []
        for line in (aadl_model or "").splitlines():
            clean = line.strip()
            if not clean:
                continue
            if any(re.search(rf"(?<![A-Za-z0-9_]){re.escape(name)}(?![A-Za-z0-9_])", clean) for name in names):
                related.append(clean)
        return list(dict.fromkeys(related))

    def _focused_model_analysis(self, state: PipelineState, target_names: list[str]) -> dict[str, Any]:
        analysis = state.model_analysis if isinstance(state.model_analysis, dict) else {}
        names = {name for name in target_names if name}
        focused: dict[str, Any] = {}
        component_types = []
        for item in analysis.get("component_types", []) or []:
            if not isinstance(item, dict):
                continue
            name = str(item.get("name") or "")
            if name in names:
                component_types.append(item)
        if component_types:
            focused["component_types"] = component_types
        component_implementations = []
        for item in analysis.get("component_implementations", []) or []:
            if not isinstance(item, dict):
                continue
            name = str(item.get("name") or "")
            type_name = str(item.get("type_name") or name.split(".", 1)[0])
            if name in names or type_name in names:
                component_implementations.append(item)
        if component_implementations:
            focused["component_implementations"] = component_implementations
        subcomponents = []
        for item in analysis.get("subcomponents", []) or []:
            if not isinstance(item, dict):
                continue
            if str(item.get("owner") or "") in names:
                subcomponents.append(item)
        if subcomponents:
            focused["subcomponents"] = subcomponents
        features = []
        for item in analysis.get("features", []) or []:
            if not isinstance(item, dict):
                continue
            if str(item.get("owner") or "") in names:
                features.append(item)
        if features:
            focused["features"] = features
        connections = []
        for item in analysis.get("connections", []) or []:
            if not isinstance(item, dict):
                continue
            haystack = " ".join(str(item.get(key, "")) for key in ("owner", "name", "source", "destination"))
            if any(name and name in haystack for name in names):
                connections.append(item)
        if connections:
            focused["connections"] = connections[:40]
        properties = []
        for item in analysis.get("properties", []) or []:
            if not isinstance(item, dict):
                continue
            if str(item.get("owner") or "") in names:
                properties.append(item)
        if properties:
            focused["properties"] = properties[:40]
        return focused

    def direct_reference_context(self, state: PipelineState, max_total_chars: int = 7000) -> str:
        """Return only referenced declarations that are directly named by the target slice."""
        target_text = self.target_model_context(state, max_chars=14000)
        declaration_names, property_names = self._direct_reference_sets(target_text)
        if not declaration_names and not property_names:
            return "No directly referenced declarations were detected."
        blocks: list[str] = []
        total = 0
        seen: set[str] = set()
        same_file = self._extract_direct_reference_blocks(state.raw_aadl, declaration_names, property_names)
        if same_file:
            block = f"-- BEGIN DIRECT DECLARATIONS FROM CURRENT AADL MODEL\n{same_file}\n-- END DIRECT DECLARATIONS FROM CURRENT AADL MODEL"
            blocks.append(block)
            seen.add(self._dedupe_key(block))
            total += len(block)
        for ref in state.references:
            content = str(ref.get("content", "") or "")
            path = str(ref.get("path", "reference.aadl") or "reference.aadl")
            path, content = self._prefer_reference_content(path, content)
            external_declaration_names = {
                name for name in declaration_names if "::" in name or "." in name
            }
            extracted = self._extract_direct_reference_blocks(content, external_declaration_names, property_names)
            if not extracted:
                continue
            block = f"-- BEGIN DIRECT REFERENCED AADL: {path}\n{extracted}\n-- END DIRECT REFERENCED AADL: {path}"
            key = self._dedupe_key(block)
            if key in seen:
                continue
            seen.add(key)
            if total + len(block) > max_total_chars:
                remaining = max_total_chars - total
                if remaining > 500:
                    block = block[:remaining] + "\n-- [direct referenced declarations truncated]"
                    blocks.append(block)
                break
            blocks.append(block)
            total += len(block)
        return "\n\n".join(blocks) if blocks else "No directly referenced declarations were found in referenced packages."

    def _direct_reference_sets(self, target_text: str) -> tuple[set[str], set[str]]:
        declaration_names: set[str] = set()
        property_names: set[str] = set()
        for qualified in re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)+)\b", target_text or ""):
            if re.search(r"\s*=>", (target_text or "")[target_text.find(qualified) : target_text.find(qualified) + len(qualified) + 5]):
                property_names.add(qualified)
                property_names.add(qualified.split("::")[-1])
            else:
                declaration_names.add(qualified)
                declaration_names.add(qualified.split("::")[-1])
        for match in re.finditer(
            r"(?im)^\s*[A-Za-z_][A-Za-z0-9_]*\s*:\s*(system|process|thread|device|abstract|processor|data|bus)\s+([A-Za-z_][A-Za-z0-9_.:]*)",
            target_text or "",
        ):
            classifier = match.group(2).rstrip(";")
            declaration_names.add(classifier)
            declaration_names.add(classifier.split("::")[-1].split(".")[0])
        for parent in re.findall(r"(?im)^\s*(?:system|process|thread|device|abstract|processor|data|bus)\s+[A-Za-z_][A-Za-z0-9_]*\s+extends\s+([A-Za-z_][A-Za-z0-9_:]*)", target_text or ""):
            declaration_names.add(parent)
            declaration_names.add(parent.split("::")[-1])
        for prop in re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)+)\s*=>", target_text or ""):
            property_names.add(prop)
            property_names.add(prop.split("::")[-1])
        return {name for name in declaration_names if name}, {name for name in property_names if name}

    def _extract_direct_reference_blocks(self, content: str, declaration_names: set[str], property_names: set[str]) -> str:
        blocks: list[str] = []
        package_name = self._primary_package_name(content)
        for name in sorted(declaration_names, key=len, reverse=True):
            local = name.split("::")[-1].split(".")[0]
            for candidate in {name, local}:
                block = self._declaration_block_by_name(content, candidate)
                if block:
                    label = self._qualified_declaration_label(block, package_name)
                    blocks.append(f"-- DIRECT DECLARATION: {label}\n{block}" if label else block)
        for name in sorted(property_names, key=len, reverse=True):
            local = name.split("::")[-1]
            for candidate in {name, local}:
                prop_block = self._property_definition_context(content, candidate)
                if prop_block:
                    blocks.append(prop_block)
        unique: list[str] = []
        seen: set[str] = set()
        for block in blocks:
            key = self._dedupe_key(block)
            if key in seen:
                continue
            seen.add(key)
            unique.append(block)
        return "\n\n".join(unique)

    def _primary_package_name(self, content: str) -> str:
        match = re.search(r"(?im)^\s*package\s+([A-Za-z_][A-Za-z0-9_:]*)\b", content or "")
        return match.group(1) if match else ""

    def _qualified_declaration_label(self, block: str, package_name: str) -> str:
        match = re.search(
            r"(?im)^\s*(?:system|process|thread|device|abstract|subprogram|processor|data|bus)(?:\s+implementation)?\s+([A-Za-z_][A-Za-z0-9_.:]*)\b",
            block or "",
        )
        if not match:
            return ""
        name = match.group(1)
        if "::" in name or not package_name:
            return name
        return f"{package_name}::{name}"

    def _dedupe_key(self, text: str) -> str:
        return re.sub(r"\s+", " ", text or "").strip().lower()

    def _declaration_block_by_name(self, content: str, name: str) -> str:
        if not name:
            return ""
        declaration = r"(?:system|process|thread|device|abstract|subprogram|processor|data|bus)(?:\s+implementation)?"
        match = re.search(
            rf"(?ims)^\s*{declaration}\s+{re.escape(name)}\b.*?^\s*end\s+{re.escape(name)}\s*;",
            content or "",
        )
        if match:
            return match.group(0).strip()
        return ""

    def _property_definition_context(self, content: str, name: str) -> str:
        if not name:
            return ""
        lines = (content or "").splitlines()
        for index, line in enumerate(lines):
            if re.search(rf"(?i)\b{re.escape(name)}\b", line) and (
                "=>" not in line or re.search(r"(?i)\b(property|inherit|applies|units|type)\b", line)
            ):
                start = max(0, index - 2)
                end = min(len(lines), index + 5)
                return "\n".join(lines[start:end]).strip()
        return ""

    def reference_context(self, state: PipelineState, max_chars_per_file: int = 6000, max_total_chars: int = 24000) -> str:
        """Return case-specific non-predeclared AADL references for LLM grounding."""
        blocks: list[str] = []
        total = 0
        skipped = {
            "base_types",
            "data_model",
            "communication_properties",
            "deployment",
            "deployment_properties",
            "memory_properties",
            "modeling_properties",
            "programming_properties",
            "thread_properties",
            "timing_properties",
        }
        for ref in state.references:
            content = str(ref.get("content", "") or "")
            path = str(ref.get("path", "reference.aadl") or "reference.aadl")
            path, content = self._prefer_reference_content(path, content)
            declared = self._declared_units(content)
            if declared and all(unit.split("::", 1)[0].lower() in skipped for unit in declared):
                continue
            snippet = content[:max_chars_per_file]
            if len(content) > max_chars_per_file:
                snippet += "\n-- [truncated reference context]"
            block = f"-- BEGIN REFERENCED AADL: {path}\n{snippet}\n-- END REFERENCED AADL: {path}"
            if total + len(block) > max_total_chars:
                break
            blocks.append(block)
            total += len(block)
        return "\n\n".join(blocks) if blocks else "No non-predeclared referenced AADL packages were provided."

    def _declared_units(self, content: str) -> list[str]:
        units: list[str] = []
        for pattern in (
            r"(?im)^\s*package\s+([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*)\b",
            r"(?im)^\s*property\s+set\s+([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*)\b",
        ):
            units.extend(match.group(1) for match in re.finditer(pattern, content or ""))
        return units

    def _prefer_reference_content(self, path: str, content: str) -> tuple[str, str]:
        declared = self._declared_units(content)
        if not declared:
            return path, content
        current_data = len(re.findall(r"(?im)^\s*data\s+[A-Za-z_][A-Za-z0-9_]*\b", content or ""))
        current_lines = len((content or "").splitlines())
        for unit in declared:
            candidate = self._find_library_reference(unit)
            if candidate is None:
                continue
            candidate_content = candidate.read_text(encoding="utf-8", errors="replace")
            candidate_data = len(re.findall(r"(?im)^\s*data\s+[A-Za-z_][A-Za-z0-9_]*\b", candidate_content))
            candidate_lines = len(candidate_content.splitlines())
            if candidate_data > current_data + 5 or candidate_lines > current_lines * 2:
                return str(candidate), candidate_content
        return path, content

    def _find_library_reference(self, unit: str) -> Path | None:
        key = (unit or "").strip().replace(".", "::").lower()
        static_root = (self.config.agree_validator_root / "static-libs").resolve()
        for root in self.config.aadl_library_dirs or []:
            if not root.exists() or not root.is_dir():
                continue
            resolved_root = root.resolve()
            try:
                resolved_root.relative_to(static_root)
                continue
            except ValueError:
                pass
            for file in root.rglob("*.aadl"):
                content = file.read_text(encoding="utf-8", errors="replace")
                if key in {item.lower() for item in self._declared_units(content)}:
                    return file
        return None

    def _save_rag_debug(self, state: PipelineState, agent_name: str, debug: Dict[str, Any]) -> None:
        if not debug:
            return
        debug_dir = state.report_dir(self.config.result_root) / "rag_debug"
        debug_dir.mkdir(parents=True, exist_ok=True)
        safe_agent = re.sub(r"[^A-Za-z0-9_.-]+", "_", agent_name).strip("_") or "agent"
        json_targets = {
            "retrieval_config": debug.get("retrieval_config"),
            "retrieval_features": debug.get("retrieval_features"),
            "retrieval_queries": debug.get("retrieval_queries"),
            "retrieved_candidates_raw": debug.get("retrieved_candidates_raw"),
            "reranked_candidates": debug.get("reranked_candidates"),
        }
        for name, payload in json_targets.items():
            if payload is None:
                continue
            path = debug_dir / f"{safe_agent}_{name}.json"
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8", errors="replace")
            if agent_name == "agree_generator":
                generic = debug_dir / f"{name}.json"
                generic.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8", errors="replace")
        cards = debug.get("compressed_rag_cards")
        if cards:
            path = debug_dir / f"{safe_agent}_compressed_rag_cards.txt"
            path.write_text(str(cards), encoding="utf-8", errors="replace")
            if agent_name == "agree_generator":
                (debug_dir / "compressed_rag_cards.txt").write_text(str(cards), encoding="utf-8", errors="replace")

    def _load_agent_rag_cards(self, debug_dir: Path, agent_name: str, category: str) -> list[str]:
        path = debug_dir / f"{agent_name}_compressed_rag_cards.txt"
        if not path.exists():
            return []
        text = path.read_text(encoding="utf-8", errors="replace")
        block = extract_section(text, f"{category.upper()}_CARDS")
        if not block:
            return []
        chunks = [chunk.strip() for chunk in re.split(r"\n\s*\n(?=\[K(?:SYN|EXP|DEF)-\d+\])", block) if chunk.strip()]
        return chunks

    def _compile_must_follow(self, agent_name: str, defensive_cards: list[str]) -> str:
        base_rules = {
            "model_analyst": [
                "Return JSON only in the requested schema.",
                "Do not interpret the requirement or generate AGREE content.",
                "Do not invent components, ports, subcomponents, or implementations.",
            ],
            "requirement_analyst": [
                "Return JSON only in the compact semantic item schema.",
                "Do not output AGREE expressions.",
                "Preserve explicit bounds, relations, route names, and visible identifiers.",
                "Do not decide that the final annex should be empty.",
            ],
            "agree_generator": [
                "Return only AGREE annex block(s).",
                "Use Requirement Analyst items as semantic guidance, not as a generation gate.",
                "Prefer valid partial contracts over empty annexes when executable meaning is available.",
                "Use only exact visible target-interface symbols as operands.",
            ],
            "model_fusion": [
                "Preserve all unrelated AADL structure exactly.",
                "Insert annexes only into the resolved target type or target implementation.",
                "Do not rename, reorder, or redesign the architecture.",
            ],
            "validation_repair": [
                "Fix only constructs implicated by diagnostics.",
                "Preserve the generated contract intent while repairing syntax and scope.",
                "Return repaired code only, preserving unrelated model text.",
            ],
        }
        lines = [f"- {rule}" for rule in base_rules.get(agent_name, [])] if self.strategy_guidance_enabled() else []
        if agent_name == "model_analyst":
            return "\n".join(lines)
        for card in defensive_cards[:3]:
            summary = self._card_summary(card)
            if summary:
                lines.append(f"- {summary}")
        return "\n".join(lines)

    def _compile_syntax_reference(self, agent_name: str, syntax_cards: list[str]) -> str:
        if agent_name == "model_analyst":
            return ""
        limit = 2 if agent_name in {"model_analyst", "requirement_analyst"} else 3
        lines = []
        for card in syntax_cards[:limit]:
            summary = self._card_summary(card)
            if summary:
                lines.append(f"- {summary}")
        return "\n".join(lines)

    def _compile_pattern_reference(self, agent_name: str, pattern_cards: list[str]) -> str:
        if agent_name not in {"requirement_analyst", "agree_generator", "validation_repair"}:
            return ""
        limit = 2 if agent_name == "requirement_analyst" else 3
        lines = []
        for card in pattern_cards[:limit]:
            summary = self._card_summary(card)
            if summary:
                lines.append(f"- {summary}")
        return "\n".join(lines)

    def _compile_available_symbols(self, state: PipelineState, visible_identifiers: list[str] | None) -> str:
        identifiers = list(dict.fromkeys((visible_identifiers or [])[:40]))
        if not identifiers and isinstance(state.model_analysis, dict):
            for item in state.model_analysis.get("components", []) or []:
                if isinstance(item, dict):
                    for feature in item.get("features", []) or []:
                        if isinstance(feature, dict) and isinstance(feature.get("name"), str):
                            identifiers.append(feature["name"])
        if not identifiers:
            return "No explicit identifier whitelist available."
        return "\n".join(f"- {identifier}" for identifier in identifiers[:40])

    def _card_summary(self, card_text: str) -> str:
        lines = [line.strip() for line in card_text.splitlines() if line.strip()]
        if not lines:
            return ""
        content_lines = [line for line in lines if not line.startswith("[K") and not line.startswith("Source:") and not line.startswith("Topic:")]
        summary = " ".join(content_lines[:3]).strip()
        summary = re.sub(r"\s+", " ", summary)
        return summary[:360]

    def _debug_llm_request(
        self,
        state: PipelineState,
        stage_name: str,
        system_prompt: str,
        user_prompt: str,
        temperature: float | None,
    ) -> None:
        safe_stage = re.sub(r"[^A-Za-z0-9_.-]+", "_", stage_name).strip("_") or "llm_call"
        request_text = (
            f"case={state.case_id}\n"
            f"setting={state.setting}\n"
            f"model={self.config.model_name}\n"
            f"temperature={self.config.temperature if temperature is None else temperature}\n"
            "\n"
            "[SYSTEM PROMPT]\n"
            f"{system_prompt}\n"
            "\n"
            "[USER PROMPT]\n"
            f"{user_prompt}\n"
        )
        debug_dir = state.report_dir(self.config.result_root) / "llm_inputs"
        debug_dir.mkdir(parents=True, exist_ok=True)
        prompt_path = debug_dir / f"{self.call_counter:02d}_{safe_stage}.txt"
        prompt_path.write_text(request_text, encoding="utf-8", errors="replace")

        print("\n" + "=" * 80, flush=True)
        print("LLM REQUEST", flush=True)
        print(f"stage={stage_name}", flush=True)
        print(f"case={state.case_id} setting={state.setting} model={self.config.model_name}", flush=True)
        print(f"saved_input={prompt_path}", flush=True)
        print("=" * 80, flush=True)
        if self.debug_prompts or self.debug_inputs_verbose:
            print("[SYSTEM PROMPT]", flush=True)
            print(system_prompt, flush=True)
            print("\n[USER PROMPT]", flush=True)
            print(user_prompt, flush=True)
            print("=" * 80 + "\n", flush=True)
        else:
            print("Full submitted LLM input was written to the file above.", flush=True)
        print("=" * 80 + "\n", flush=True)

    def _save_llm_response(self, state: PipelineState, stage_name: str, response: str) -> None:
        safe_stage = re.sub(r"[^A-Za-z0-9_.-]+", "_", stage_name).strip("_") or "llm_call"
        output_dir = state.report_dir(self.config.result_root) / "llm_outputs"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{self.call_counter:02d}_{safe_stage}.txt"
        output_path.write_text(response, encoding="utf-8", errors="replace")
        if self.debug_inputs_only:
            print(f"saved_output={output_path}", flush=True)

    def _save_llm_failure(self, state: PipelineState, stage_name: str, attempt: int, exc: Exception) -> None:
        safe_stage = re.sub(r"[^A-Za-z0-9_.-]+", "_", stage_name).strip("_") or "llm_call"
        failure_dir = state.report_dir(self.config.result_root) / "llm_failures"
        failure_dir.mkdir(parents=True, exist_ok=True)
        failure_path = failure_dir / f"{self.call_counter:02d}_{safe_stage}_attempt_{attempt}.txt"
        status_code = getattr(exc, "status_code", None)
        response_text = getattr(exc, "response_text", "")
        headers = getattr(exc, "headers", {})
        payload = (
            f"stage={stage_name}\n"
            f"attempt={attempt}\n"
            f"exception_type={type(exc).__name__}\n"
            f"exception={exc}\n\n"
            f"status_code={status_code}\n"
            f"headers={json.dumps(headers, ensure_ascii=False, indent=2)}\n\n"
            "[RAW_RESPONSE_PREVIEW]\n"
            f"{response_text[:8000]}\n\n"
            "[TRACEBACK]\n"
            f"{traceback.format_exc()}\n"
        )
        failure_path.write_text(payload, encoding="utf-8", errors="replace")

    def _save_empty_llm_payload(self, state: PipelineState, stage_name: str, payload: dict[str, Any]) -> None:
        safe_stage = re.sub(r"[^A-Za-z0-9_.-]+", "_", stage_name).strip("_") or "llm_call"
        payload_dir = state.report_dir(self.config.result_root) / "llm_payloads"
        payload_dir.mkdir(parents=True, exist_ok=True)
        payload_path = payload_dir / f"{self.call_counter:02d}_{safe_stage}_empty.json"
        payload_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
            errors="replace",
        )

    def record_recovery(self, state: PipelineState, stage_name: str, actions: list[dict[str, Any]]) -> None:
        if not actions:
            return
        state.recovery_actions.extend(actions)
        recovery_dir = state.report_dir(self.config.result_root) / "recovery"
        recovery_dir.mkdir(parents=True, exist_ok=True)
        safe_stage = re.sub(r"[^A-Za-z0-9_.-]+", "_", stage_name).strip("_") or "stage"
        path = recovery_dir / f"{safe_stage}_recovery.json"
        path.write_text(json.dumps(actions, ensure_ascii=False, indent=2), encoding="utf-8", errors="replace")


class ModelAnalystAgent:
    def __init__(self, runtime: AgentRuntime):
        self.runtime = runtime

    def run(self, state: PipelineState, rag_enabled: bool) -> Dict[str, Any]:
        compiled = self.runtime.compiled_agent_context(state, "model_analyst", rag_enabled)
        focused_aadl = self.runtime.target_model_context(state, max_chars=12000)
        prompt = self.runtime.prompts.render(
            "model_analyst",
            aadl_model=focused_aadl,
            must_follow_rules=compiled["must_follow_rules"],
            syntax_reference=compiled["syntax_reference"],
            available_symbols=compiled["available_symbols"],
            rag_context=compiled["retrieved_knowledge"],
        )
        response = self.runtime.call(
            state,
            (
                "Extract factual AADL architecture only. Return JSON with component types, "
                "implementations, subcomponents, features, connections, and properties. "
                "Preserve exact qualified names. Do not interpret requirements or generate AGREE."
            ),
            prompt,
            temperature=0.1,
            stage_name="model_analyst",
        )
        recovered = recover_json_object(
            response,
            "model_analyst",
            defaults={
                "component_types": [],
                "component_implementations": [],
                "subcomponents": [],
                "features": [],
                "connections": [],
                "properties": [],
            },
        )
        self.runtime.record_recovery(state, "model_analyst", recovered.actions)
        return recovered.value


class RequirementAnalystAgent:
    def __init__(self, runtime: AgentRuntime):
        self.runtime = runtime

    def run(self, state: PipelineState, rag_enabled: bool) -> Dict[str, Any]:
        identifier_whitelist = self._target_visible_identifiers(state)
        compiled = self.runtime.compiled_agent_context(
            state,
            "requirement_analyst",
            False,
            visible_identifiers=identifier_whitelist,
            include_reference_context=False,
        )
        prompt = self.runtime.prompts.render(
            "requirement_analyst",
            requirement_text=state.raw_requirement,
            must_follow_rules=compiled["must_follow_rules"],
            available_symbols=compiled["available_symbols"],
            target_interface_context=self._target_interface_context(state),
            model_refs_context=self._model_refs_context(state),
        )
        response = self.runtime.call(
            state,
            (
                "Summarize the requirement into compact JSON items for the AGREE Generator. "
                "Return JSON only with id, kind, status, and text. Do not output AGREE expressions."
            ),
            prompt,
            temperature=0.0,
            stage_name="requirement_analyst",
            max_tokens=1200,
        )
        report_dir = state.report_dir(self.runtime.config.result_root)
        report_dir.mkdir(parents=True, exist_ok=True)
        target_interface_context = self._target_interface_context(state)
        (report_dir / "requirement_analyst_target_interface.txt").write_text(
            target_interface_context,
            encoding="utf-8",
            errors="replace",
        )
        (report_dir / "requirement_analyst_original_output.txt").write_text(
            response,
            encoding="utf-8",
            errors="replace",
        )
        recovered = recover_json_object(
            response,
            "requirement_analyst",
            defaults={"items": []},
        )
        self.runtime.record_recovery(state, "requirement_analyst", recovered.actions)
        analysis = self._normalize_requirement_items(recovered.value if isinstance(recovered.value, dict) else {}, state)
        (report_dir / "requirement_analyst_classified_items.json").write_text(
            json.dumps(analysis, ensure_ascii=False, indent=2),
            encoding="utf-8",
            errors="replace",
        )
        (report_dir / "requirement_analyst_raw_atomic_propositions.txt").write_text(
            self._suggested_expression_text(analysis),
            encoding="utf-8",
            errors="replace",
        )
        return analysis

    def _target_interface_context(self, state: PipelineState) -> str:
        target_type, _ = split_target_component_names(state.target_component, state.raw_aadl)
        profiles = ModelFusionAgent(self.runtime)._target_feature_profiles(state, target_type or state.target_component)
        if not profiles:
            identifiers = self._target_visible_identifiers(state)
            if not identifiers:
                return "\n".join(
                    [
                        "Exact expression symbols: (none)",
                        "No feature-level AGREE expression symbols are available for this target.",
                    ]
                )
            return "\n".join(
                [
                    "Exact expression symbols: (none)",
                    "No feature-level AGREE expression symbols are available for this target.",
                    "The structural names below are model elements, not AGREE expression values:",
                    *[f"- {identifier}" for identifier in identifiers[:40]],
                ]
            )
        field_map = ModelFusionAgent(self.runtime)._data_field_map(state)
        expression_symbols: list[str] = []
        rows: list[str] = ["name | direction | kind | scalar | aadl_type"]
        for name, profile in profiles.items():
            expression_symbols.append(name)
            rows.append(
                " | ".join(
                    [
                        name,
                        str(profile.get("direction") or "unknown"),
                        str(profile.get("kind") or "unknown"),
                        str(profile.get("scalar") or "unknown"),
                        str(profile.get("data_type") or ""),
                    ]
                )
            )
            for field in field_map.get(str(profile.get("data_type") or "").lower(), [])[:8]:
                field_symbol = f"{name}.{field.get('name')}"
                expression_symbols.append(field_symbol)
                rows.append(
                    " | ".join(
                        [
                            field_symbol,
                            str(profile.get("direction") or "unknown"),
                            "data_field",
                            str(field.get("scalar") or "unknown"),
                            str(field.get("data_type") or ""),
                        ]
                    )
                )
        unique_symbols = list(dict.fromkeys(expression_symbols))
        lines = [
            "Exact expression symbols: " + ", ".join(unique_symbols[:40]),
            "Use only these exact names as expression operands; do not prefix them with component, implementation, package, property, or metadata names.",
            "",
            *rows,
        ]
        return "\n".join(lines[:43])

    def _model_refs_context(self, state: PipelineState) -> str:
        if not isinstance(state.model_analysis, dict):
            return "No model analysis refs available."
        lines: list[str] = []
        for item in state.model_analysis.get("subcomponents", []) or []:
            if not isinstance(item, dict):
                continue
            owner = str(item.get("owner") or "")
            name = str(item.get("name") or "")
            classifier = str(item.get("classifier") or "")
            if owner and name:
                lines.append(f"subcomponent: {owner}.{name} classifier={classifier}")
        for item in state.model_analysis.get("connections", []) or []:
            if not isinstance(item, dict):
                continue
            owner = str(item.get("owner") or "")
            name = str(item.get("name") or "")
            source = str(item.get("source") or "")
            destination = str(item.get("destination") or "")
            if owner and name:
                lines.append(f"connection: {owner}.{name} source={source} destination={destination}")
        for item in state.model_analysis.get("properties", []) or []:
            if not isinstance(item, dict):
                continue
            owner = str(item.get("owner") or "")
            name = str(item.get("name") or "")
            value = str(item.get("value") or "")
            if owner and name:
                lines.append(f"property: {owner} {name}={value}")
        return "\n".join(lines[:60]) if lines else "No model analysis refs available."

    def _normalize_requirement_items(self, payload: dict[str, Any], state: PipelineState) -> Dict[str, Any]:
        raw_items = payload.get("items")
        if not isinstance(raw_items, list):
            raw_items = []
        whitelist = self._identifier_whitelist(state)
        normalized: list[dict[str, Any]] = []
        valid_categories = {
            "aadl_property",
            "interface_fact",
            "behavior_relation",
            "dependency_claim",
            "data_constraint",
            "timing_constraint",
            "signal_flow",
            "input_assumption",
            "output_guarantee",
            "deployment_binding",
            "other",
            "unsupported",
        }
        for index, item in enumerate(raw_items, 1):
            if not isinstance(item, dict):
                continue
            category = str(item.get("kind") or item.get("category") or "unsupported").strip()
            if category not in valid_categories:
                category = "other"
            intent = str(item.get("intent") or item.get("polarity") or "").strip().lower()
            if intent not in {"assume", "guarantee", "describe"}:
                if category == "input_assumption":
                    intent = "assume"
                elif category in {"behavior_relation", "data_constraint", "output_guarantee", "dependency_claim"}:
                    intent = "guarantee"
                else:
                    intent = "describe"
            visible_symbols = [
                str(symbol).strip()
                for symbol in item.get("symbols", item.get("visible_symbols", [])) or []
                if isinstance(symbol, str) and str(symbol).strip()
            ]
            related = [
                str(symbol).strip()
                for symbol in item.get("model_refs", item.get("related_model_elements", [])) or []
                if isinstance(symbol, str) and str(symbol).strip()
            ]
            evidence = [
                str(symbol).strip()
                for symbol in item.get("evidence", item.get("anchored_identifiers", visible_symbols + related)) or []
                if isinstance(symbol, str) and str(symbol).strip()
            ]
            text = str(item.get("text") or item.get("fragment") or item.get("requirement_fragment") or "").strip()
            normalized.append(
                {
                    "id": str(item.get("id") or f"R{index}"),
                    "text": text,
                    "fragment": text,
                    "kind": category,
                    "intent": intent,
                    "evidence": evidence[:12],
                    "symbols": visible_symbols[:12],
                    "model_refs": related[:12],
                    "note": "",
                    # Compatibility fields for downstream prompts while they are being revised agent by agent.
                    "requirement_fragment": text,
                    "category": category,
                    "related_model_elements": related[:12],
                    "visible_symbols": visible_symbols[:12],
                    "suggested_agree_expression": "",
                    "reason": "",
                    "anchored_identifiers": evidence[:12],
                    "directly_generatable": False,
                }
            )
        self.runtime.record_recovery(
            state,
            "requirement_analyst",
            [
                {
                    "stage": "requirement_analyst",
                    "action": "requirement_items_normalized",
                    "detail": f"Normalized {len(normalized)} classified requirement item(s).",
                    "confidence": "high" if normalized else "low",
                }
            ],
        )
        return {
            "analysis_style": "classified_requirement_items",
            "items": normalized,
            "rag_cards_used": {"Ksyn": [], "Kexp": [], "Kdef": []},
            "suggested_agree_expressions": [],
        }

    def _default_requirement_status(self, category: str) -> str:
        if category == "aadl_property":
            return "property_only"
        if category in {"interface_fact", "timing_constraint"}:
            return "structural_only"
        if category == "unsupported":
            return "unsupported"
        return "describe"

    def _short_note(self, text: str) -> str:
        words = re.split(r"\s+", (text or "").strip())
        return " ".join(words[:12])

    def _suggested_expression_text(self, analysis: dict[str, Any]) -> str:
        items = analysis.get("items", []) if isinstance(analysis, dict) else []
        lines = []
        for item in items:
            if isinstance(item, dict) and item.get("directly_generatable"):
                expression = str(item.get("suggested_agree_expression") or "").strip()
                if expression:
                    lines.append(expression)
        return "\n".join(lines)

    def _extract_requirement_propositions(self, response: str, state: PipelineState) -> tuple[list[str], list[dict[str, Any]]]:
        propositions = self._parse_atomic_lines(response)
        return propositions, [
            {
                "stage": "requirement_analyst",
                "action": "atomic_line_parse_used",
                "detail": "Parsed Requirement Analyst output as plain atomic proposition lines.",
                "confidence": "high" if propositions else "low",
            }
        ]

    def _parse_atomic_lines(
        self,
        text: str,
    ) -> list[str]:
        cleaned = strip_code_fence(text or "")
        cleaned = re.sub(r"(?is)<think>.*?</think>", "", cleaned)
        cleaned = (
            cleaned.replace("≥", ">=")
            .replace("≤", "<=")
            .replace("≠", "<>")
            .replace("¬", "not ")
            .replace("∧", " and ")
            .replace("∨", " or ")
        )
        lines: list[str] = []
        for raw_line in cleaned.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            line = re.sub(r"^\s*(?:[-*•]|\d+[\.)])\s*", "", line).strip()
            line = line.strip("`")
            if not line:
                continue
            lower = line.lower()
            if lower in {"atomic propositions:", "atomic proposition list:", "propositions:"}:
                continue
            if lower.startswith(("here are", "the atomic", "output:", "note:")):
                continue
            if re.search(r"\b(analysis_style|atomic_propositions|raw_atomic_propositions|requirement_units)\b", lower):
                continue
            if line.startswith("{") or line.startswith("["):
                continue
            if re.match(r"(?i)^\s*(assume|guarantee|lemma|eq|const|assign|annex)\b", line):
                continue
            lines.append(line.rstrip(";"))
        return list(dict.fromkeys(lines))

    def _identifier_whitelist(self, state: PipelineState) -> list[str]:
        identifiers: list[str] = []
        if not isinstance(state.model_analysis, dict):
            return self._raw_aadl_identifiers(state.raw_aadl)
        whitelist = state.model_analysis.get("identifier_whitelist", {})
        if isinstance(whitelist, dict):
            for value in whitelist.values():
                if isinstance(value, list):
                    identifiers.extend(item for item in value if isinstance(item, str))
        for key in ("component_types", "component_implementations", "data_types", "subcomponents", "connections"):
            for item in state.model_analysis.get(key, []) or []:
                if isinstance(item, str):
                    identifiers.append(item)
                elif isinstance(item, dict) and isinstance(item.get("name"), str):
                    identifiers.append(item["name"])
        for item in state.model_analysis.get("features", []) or []:
            if isinstance(item, dict) and isinstance(item.get("name"), str):
                identifiers.append(item["name"])
        for item in state.model_analysis.get("components", []) or []:
            if isinstance(item, str):
                identifiers.append(item)
            elif isinstance(item, dict):
                if isinstance(item.get("name"), str):
                    identifiers.append(item["name"])
                for feature in item.get("features", []) or []:
                    if isinstance(feature, str):
                        identifiers.append(feature)
                    elif isinstance(feature, dict) and isinstance(feature.get("name"), str):
                        identifiers.append(feature["name"])
        for item in state.model_analysis.get("ports", []) or []:
            if isinstance(item, str):
                identifiers.append(item)
            elif isinstance(item, dict) and isinstance(item.get("name"), str):
                identifiers.append(item["name"])
        identifiers.extend(self._raw_aadl_identifiers(state.raw_aadl))
        return list(dict.fromkeys(identifiers))

    def _target_visible_identifiers(self, state: PipelineState) -> list[str]:
        if not isinstance(state.model_analysis, dict):
            return self._raw_aadl_identifiers(state.raw_aadl)
        try:
            target_type, _ = split_target_component_names(state.target_component, state.raw_aadl)
        except Exception:
            target_type = state.target_component or ""
        target_type_lower = (target_type or "").lower()
        identifiers: list[str] = []
        for feature in state.model_analysis.get("features", []) or []:
            if not isinstance(feature, dict):
                continue
            owner = str(feature.get("owner") or "").lower()
            if owner == target_type_lower and isinstance(feature.get("name"), str):
                identifiers.append(feature["name"])
        if identifiers:
            return list(dict.fromkeys(identifiers))
        for component in state.model_analysis.get("components", []) or []:
            if not isinstance(component, dict):
                continue
            name = component.get("name")
            if not isinstance(name, str) or name.lower() != target_type_lower:
                continue
            for feature in component.get("features", []) or []:
                if isinstance(feature, str):
                    identifiers.append(feature)
                elif isinstance(feature, dict) and isinstance(feature.get("name"), str):
                    identifiers.append(feature["name"])
            break
        if identifiers:
            return list(dict.fromkeys(identifiers))
        return self._identifier_whitelist(state)

    def _anchored_identifiers(self, proposition: str, identifiers: list[str]) -> list[str]:
        anchors = []
        for identifier in identifiers:
            if re.search(rf"(?<![A-Za-z0-9_]){re.escape(identifier)}(?![A-Za-z0-9_])", proposition):
                anchors.append(identifier)
        return anchors

    def _raw_aadl_identifiers(self, aadl_model: str) -> list[str]:
        identifiers: list[str] = []
        patterns = [
            r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(?:in|out)\s+(?:event\s+data|event|data)\s+port\b",
            r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(?:system|process|thread|device|data)\b",
            r"^\s*(?:system|process|thread|device|data)\s+(?:implementation\s+)?([A-Za-z_][A-Za-z0-9_.]*)\b",
            r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*connection\b",
        ]
        for line in (aadl_model or "").splitlines():
            for pattern in patterns:
                match = re.search(pattern, line, flags=re.IGNORECASE)
                if match:
                    identifiers.append(match.group(1))
                    break
        return list(dict.fromkeys(identifiers))


class AgreeGeneratorAgent:
    def __init__(self, runtime: AgentRuntime):
        self.runtime = runtime

    def run(self, state: PipelineState, rag_enabled: bool) -> str:
        system_name, implementation_name = split_target_component_names(state.target_component, state.raw_aadl)
        visible_identifiers = RequirementAnalystAgent(self.runtime)._target_visible_identifiers(state)
        feature_profiles = ModelFusionAgent(self.runtime)._target_feature_profiles(state, system_name)
        requirement_analysis = self._format_requirement_analysis(
            state.requirement_analysis,
            visible_identifiers,
            feature_profiles,
            state.raw_requirement,
        )
        retrieval_requirement = "\n\n".join(
            item
            for item in [
                "Classified requirement items for AGREE generation:",
                requirement_analysis,
            ]
            if item
        )
        compiled = self.runtime.compiled_agent_context(
            state,
            "agree_generator",
            rag_enabled,
            visible_identifiers=visible_identifiers,
            include_reference_context=False,
            retrieval_requirement=retrieval_requirement,
        )
        prompt = self.runtime.prompts.render(
            "agree_generator",
            requirement_text=state.raw_requirement,
            target_model_context=compiled["target_model_context"],
            reference_context=compiled["reference_context"],
            model_analysis_or_disabled="",
            requirement_analysis_or_disabled=requirement_analysis,
            target_component=state.target_component,
            system_name=system_name,
            implementation_name=implementation_name or "NONE",
            must_follow_rules=compiled["must_follow_rules"],
            syntax_reference=compiled["syntax_reference"],
            pattern_reference=compiled["pattern_reference"],
            available_symbols=compiled["available_symbols"],
            target_interface_context=RequirementAnalystAgent(self.runtime)._target_interface_context(state),
            rag_context=compiled["retrieved_knowledge"],
        )
        debug_dir = state.report_dir(self.runtime.config.result_root) / "rag_debug"
        debug_dir.mkdir(parents=True, exist_ok=True)
        (debug_dir / "llm_input_with_rag_cards.txt").write_text(prompt, encoding="utf-8", errors="replace")
        response = self.runtime.call(
            state,
            (
                "Generate only valid AGREE annex block(s). Do not output a complete AADL model, "
                "Markdown, JSON, headings, or explanations. Use Requirement Analyst items as semantic guidance, "
                "but do not treat them as a gate that can force an empty annex. Every assume or guarantee must "
                "include a quoted label and colon."
            ),
            prompt,
            temperature=0.1,
            stage_name="agree_generator",
        )
        return response

    def _format_requirement_analysis(
        self,
        requirement_analysis: Any,
        visible_identifiers: list[str] | None = None,
        feature_profiles: dict[str, dict[str, str]] | None = None,
        raw_requirement: str = "",
    ) -> str:
        if isinstance(requirement_analysis, dict):
            items = requirement_analysis.get("items")
            if isinstance(items, list):
                compact_items = []
                for item in items:
                    if not isinstance(item, dict):
                        continue
                    compact_items.append(
                        {
                            "id": item.get("id", ""),
                            "text": item.get("text", item.get("fragment", item.get("requirement_fragment", ""))),
                            "kind": item.get("kind", item.get("category", "")),
                            "intent": item.get("intent", "describe"),
                            "evidence": item.get("evidence", item.get("anchored_identifiers", [])),
                        }
                    )
                if compact_items:
                    return json.dumps({"items": compact_items}, ensure_ascii=False, indent=2)
            expressions = requirement_analysis.get("suggested_agree_expressions")
            if isinstance(expressions, list) and expressions:
                return json.dumps({"suggested_agree_expressions": expressions}, ensure_ascii=False, indent=2)
            raw = requirement_analysis.get("raw_atomic_propositions")
            if isinstance(raw, str) and raw.strip():
                return json.dumps({"requirement_expression_candidates": self._lightly_format_requirement_expression_text(raw).splitlines()}, ensure_ascii=False, indent=2)
        if isinstance(requirement_analysis, str):
            return self._lightly_format_requirement_expression_text(requirement_analysis)
        return ""

    def _lightly_format_requirement_expression_text(self, text: str) -> str:
        lines: list[str] = []
        for raw_line in strip_code_fence(text or "").splitlines():
            line = re.sub(r"^\s*(?:[-*•]|\d+[\.)])\s*", "", raw_line.strip()).strip("`").strip()
            if not line:
                continue
            lower = line.lower()
            if re.search(r"\b(analysis_style|atomic_propositions|raw_atomic_propositions|requirement_units)\b", lower):
                continue
            if line.startswith("{") or line.startswith("["):
                continue
            if re.match(r"(?i)^\s*(assume|guarantee|lemma|eq|const|annex)\b", line):
                continue
            if "..." in line or "…" in line:
                continue
            lines.append(line.rstrip(";"))
        return "\n".join(dict.fromkeys(lines))

    def _format_model_analysis(self, model_analysis: Any) -> str:
        if model_analysis == DISABLED:
            return DISABLED
        try:
            return json.dumps(model_analysis, ensure_ascii=False, indent=2)
        except TypeError:
            return str(model_analysis)

class ModelFusionAgent:
    def __init__(self, runtime: AgentRuntime):
        self.runtime = runtime

    def run(self, state: PipelineState, rag_enabled: bool) -> str:
        compiled = self.runtime.compiled_agent_context(state, "model_fusion", rag_enabled, include_reference_context=False)
        if self.runtime.strategy_guidance_enabled():
            target_location_plan = self._plan_target_location(state)
            fusion_plan = self._plan_fusion(state, compiled, target_location_plan)
        else:
            fusion_plan = self._fallback_fusion_plan(state)
        base_component, implementation_name = self._targets_from_fusion_plan(state, fusion_plan)
        deterministic = self._apply_fusion_plan(state.raw_aadl, state.agree_generation_output, fusion_plan)
        if deterministic:
            state.artifacts["model_fusion_raw_response"] = deterministic
            return deterministic
        prompt = self.runtime.prompts.render(
            "model_fusion",
            aadl_model=state.raw_aadl,
            reference_context="",
            agree_generator_output=state.agree_generation_output,
            fusion_plan=json.dumps(fusion_plan, ensure_ascii=False, indent=2),
            base_component=base_component,
            target_component=implementation_name or "NONE",
            must_follow_rules=compiled["must_follow_rules"],
            syntax_reference=compiled["syntax_reference"],
            pattern_reference=compiled["pattern_reference"],
            available_symbols=compiled["available_symbols"],
            rag_context=compiled["retrieved_knowledge"],
        )
        response = self.runtime.call(
            state,
            "Return only the complete modified AADL model. Insert or replace AGREE annex blocks locally in the target component and preserve all unrelated AADL code.",
            prompt,
            temperature=0.1,
            stage_name="model_fusion",
        )
        state.artifacts["model_fusion_raw_response"] = response
        fused = normalize_agree_annex_delimiters(strip_code_fence(response))
        if not self._is_plausible_full_aadl(fused, state.raw_aadl):
            raise ValueError("Model Fusion did not return a plausible complete AADL model.")
        return fused

    def _fallback_fusion_plan(self, state: PipelineState) -> dict[str, Any]:
        type_name, implementation_name = split_target_component_names(state.target_component, state.raw_aadl)
        annex = self._clean_annex(state.agree_generation_output)
        is_implementation_binding = bool(re.search(r"(?im)^\s*(assign|assert)\b", annex))
        owner = implementation_name if is_implementation_binding and implementation_name else type_name
        owner_kind = "component_implementation" if is_implementation_binding and implementation_name else "component_type"
        plan = {
            "target_component_type": type_name or "",
            "target_component_implementation": implementation_name or "NONE",
            "generated_content_kind": "implementation_binding" if is_implementation_binding else "type_contract",
            "insertions": [],
            "preserve_unrelated_code": True,
        }
        if owner:
            plan["insertions"].append(
                {
                    "owner": owner,
                    "owner_kind": owner_kind,
                    "operation": "insert_or_replace",
                    "annex_block_id": "AGREE_BLOCK_1",
                }
            )
        return plan

    def _apply_fusion_plan(self, aadl_model: str, agree_text: str, fusion_plan: dict[str, Any]) -> str:
        annex = self._clean_annex(agree_text)
        if not annex:
            return ""
        insertions = fusion_plan.get("insertions") if isinstance(fusion_plan, dict) else []
        if not isinstance(insertions, list) or not insertions:
            return ""
        output = aadl_model
        applied = False
        for insertion in insertions:
            if not isinstance(insertion, dict):
                continue
            owner = str(insertion.get("owner") or "").strip()
            if not owner:
                continue
            output = self._replace_or_insert_annex(output, owner, annex)
            applied = True
        return output if applied else ""

    def _plan_target_location(self, state: PipelineState) -> dict[str, Any]:
        prompt = self.runtime.prompts.render(
            "model_fusion_target",
            requirement_text=state.raw_requirement,
            previous_target_component=state.target_component or "NONE",
            component_candidates=self._component_candidate_list(state.raw_aadl),
        )
        response = self.runtime.call(
            state,
            (
                "Infer the intended AADL target location from the requirement and candidate list only. "
                "Return exactly one JSON object."
            ),
            prompt,
            temperature=0.0,
            stage_name="model_fusion_target",
        )
        recovered = recover_json_object(
            response,
            "model_fusion_target",
            defaults={
                "mentioned_component_type": "",
                "mentioned_component_implementation": "NONE",
                "evidence": "",
                "confidence": "low",
            },
        )
        self.runtime.record_recovery(state, "model_fusion_target", recovered.actions)
        plan = recovered.value if isinstance(recovered.value, dict) else {}
        plan.setdefault("mentioned_component_type", plan.get("target_component_type", ""))
        plan.setdefault("mentioned_component_implementation", plan.get("target_component_implementation", "NONE"))
        plan.setdefault("evidence", plan.get("requirement_evidence", ""))
        plan.setdefault("confidence", "low")
        report_dir = state.report_dir(self.runtime.config.result_root)
        report_dir.mkdir(parents=True, exist_ok=True)
        (report_dir / "model_fusion_target.json").write_text(
            json.dumps(plan, ensure_ascii=False, indent=2),
            encoding="utf-8",
            errors="replace",
        )
        state.artifacts["model_fusion_target"] = json.dumps(plan, ensure_ascii=False, indent=2)
        return plan

    def _plan_fusion(self, state: PipelineState, compiled: dict[str, str], target_location_plan: dict[str, Any]) -> dict[str, Any]:
        generated_scope_hint = self._generated_agree_scope_hint(state.agree_generation_output)
        prompt = self.runtime.prompts.render(
            "model_fusion_plan",
            target_location_plan=json.dumps(target_location_plan, ensure_ascii=False, indent=2),
            component_candidates=self._component_candidate_list(state.raw_aadl),
            agree_generator_output=state.agree_generation_output,
            generated_scope_hint=generated_scope_hint,
            rag_context=compiled["retrieved_knowledge"],
        )
        response = self.runtime.call(
            state,
            (
                "Produce Model Fusion execution guidance. Return exactly one JSON object. "
                "Use the target-location output as the primary target evidence."
            ),
            prompt,
            temperature=0.0,
            stage_name="model_fusion_plan",
        )
        recovered = recover_json_object(
            response,
            "model_fusion_plan",
            defaults={
                "target_component_type": "",
                "target_component_implementation": "NONE",
                "generated_content_kind": "unknown",
                "insertions": [],
                "preserve_unrelated_code": True,
            },
        )
        self.runtime.record_recovery(state, "model_fusion_plan", recovered.actions)
        plan = recovered.value if isinstance(recovered.value, dict) else {}
        plan.setdefault("target_component_type", "")
        plan.setdefault("target_component_implementation", "NONE")
        plan.setdefault("generated_content_kind", "unknown")
        plan.setdefault("insertions", [])
        plan.setdefault("preserve_unrelated_code", True)
        if generated_scope_hint.startswith("type_level_only"):
            target_type = self._resolve_candidate_name(
                str(plan.get("target_component_type") or target_location_plan.get("mentioned_component_type") or ""),
                self._component_candidate_names(state.raw_aadl),
            )
            if not target_type:
                target_type, _ = split_target_component_names(state.target_component, state.raw_aadl)
            plan["generated_content_kind"] = "type_contract"
            plan["target_component_type"] = target_type
            plan["insertions"] = [
                {
                    "owner": target_type,
                    "owner_kind": "component_type",
                    "operation": "insert_or_replace",
                    "annex_block_id": "AGREE_BLOCK_1",
                }
            ] if target_type else []
        elif generated_scope_hint.startswith("implementation_level_content"):
            impl = self._resolve_candidate_name(
                str(plan.get("target_component_implementation") or target_location_plan.get("mentioned_component_implementation") or ""),
                self._component_candidate_names(state.raw_aadl),
            )
            plan["generated_content_kind"] = "implementation_binding"
            plan["target_component_implementation"] = impl or "NONE"
            plan["insertions"] = [
                {
                    "owner": impl,
                    "owner_kind": "component_implementation",
                    "operation": "insert_or_replace",
                    "annex_block_id": "AGREE_BLOCK_1",
                }
            ] if impl else []
        report_dir = state.report_dir(self.runtime.config.result_root)
        report_dir.mkdir(parents=True, exist_ok=True)
        (report_dir / "model_fusion_plan.json").write_text(
            json.dumps(plan, ensure_ascii=False, indent=2),
            encoding="utf-8",
            errors="replace",
        )
        state.artifacts["model_fusion_plan"] = json.dumps(plan, ensure_ascii=False, indent=2)
        return plan

    def _generated_agree_scope_hint(self, agree_text: str) -> str:
        text = (agree_text or "").lower()
        has_impl_construct = bool(re.search(r"\b(assign|assert)\b", text))
        has_type_contract = bool(re.search(r"\b(assume|guarantee|eq|const)\b", text))
        if has_type_contract and not has_impl_construct:
            return "type_level_only: generated AGREE contains only assume/guarantee/eq/const contract content."
        if has_impl_construct and has_type_contract:
            return "mixed_type_and_implementation: generated AGREE contains both contract content and implementation constructs."
        if has_impl_construct:
            return "implementation_level_content: generated AGREE contains assign/assert implementation constructs."
        return "unknown: generated AGREE scope cannot be inferred from keywords."

    def _targets_from_fusion_plan(self, state: PipelineState, fusion_plan: dict[str, Any]) -> tuple[str, str]:
        candidates = self._component_candidate_names(state.raw_aadl)
        insertions = fusion_plan.get("insertions") if isinstance(fusion_plan, dict) else []
        type_candidate = str(fusion_plan.get("target_component_type") or "").strip()
        implementation_candidate = str(fusion_plan.get("target_component_implementation") or "").strip()
        if isinstance(insertions, list):
            for insertion in insertions:
                if not isinstance(insertion, dict):
                    continue
                owner = str(insertion.get("owner") or "").strip()
                kind = str(insertion.get("owner_kind") or "").strip()
                if kind == "component_type" and owner:
                    type_candidate = owner
                elif kind == "component_implementation" and owner:
                    implementation_candidate = owner
        if implementation_candidate.upper() == "NONE":
            implementation_candidate = ""
        base_component, implementation_name = split_target_component_names(state.target_component, state.raw_aadl)
        resolved_type = self._resolve_candidate_name(type_candidate, candidates) or base_component
        resolved_impl = self._resolve_candidate_name(implementation_candidate, candidates) or ""
        if not resolved_impl and resolved_type:
            _, resolved_impl = split_target_component_names(resolved_type, state.raw_aadl)
        return resolved_type, resolved_impl

    def _component_candidate_list(self, aadl_model: str) -> str:
        rows = []
        for item in self._component_candidates(aadl_model):
            suffix = " implementation" if item["is_implementation"] else " type"
            rows.append(f"- {item['name']} ({item['kind']}{suffix})")
        return "\n".join(rows) if rows else "No component candidates were found."

    def _component_candidate_names(self, aadl_model: str) -> list[str]:
        return [item["name"] for item in self._component_candidates(aadl_model)]

    def _component_candidates(self, aadl_model: str) -> list[dict[str, Any]]:
        pattern = re.compile(
            r"(?im)^\s*(system|process|thread|device|abstract|subprogram)\s+(implementation\s+)?([A-Za-z_][A-Za-z0-9_.]*)\b"
        )
        candidates = []
        seen = set()
        for match in pattern.finditer(aadl_model or ""):
            name = match.group(3)
            key = name.lower()
            if key in seen:
                continue
            seen.add(key)
            candidates.append(
                {
                    "kind": match.group(1),
                    "is_implementation": bool(match.group(2)),
                    "name": name,
                }
            )
        return candidates

    def _resolve_candidate_name(self, name: str, candidates: list[str]) -> str:
        if not name:
            return ""
        normalized = name.strip().lower()
        for candidate in candidates:
            if candidate.lower() == normalized:
                return candidate
        tail = normalized.split(".")[0]
        matches = [candidate for candidate in candidates if candidate.lower() == tail]
        if len(matches) == 1:
            return matches[0]
        return ""

    def _is_plausible_full_aadl(self, code: str, original_aadl: str) -> bool:
        if not code or len(code) < max(100, int(len(original_aadl) * 0.6)):
            return False
        lowered = code.lower()
        return "package " in lowered and "public" in lowered and "end " in lowered and "annex agree" in lowered

    def _clean_annex(self, text: str) -> str:
        import re

        text = normalize_agree_annex_delimiters(text)
        match = re.search(r"(annex\s+agree\s*\{\*\*.*?\*\*\}\s*;)", text or "", flags=re.IGNORECASE | re.DOTALL)
        if match:
            annex = match.group(1).strip()
            body = re.sub(r"^annex\s+agree\s*\{\*\*|\*\*\}\s*;$", "", annex, flags=re.IGNORECASE | re.DOTALL).strip()
            if not re.search(r"(?im)^\s*(assume|guarantee|eq|const|assign|assert)\b", body):
                return ""
            return annex
        clauses = (text or "").strip()
        if not clauses:
            return ""
        if re.search(r"(?im)^\s*(assume|guarantee|eq|const|assign|assert)\b", clauses):
            return "annex agree {**\n" + clauses + "\n**};"
        return clauses

    def _sanitize_annex_for_target(self, state: PipelineState, annex: str, target_name: str) -> tuple[str, list[dict[str, Any]]]:
        return self._clean_annex(annex), []

    def _split_agree_statements(self, body: str) -> list[str]:
        statements: list[str] = []
        current: list[str] = []
        in_string = False
        escape = False
        for char in body or "":
            current.append(char)
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
                elif char == ";":
                    statement = "".join(current).strip()
                    if statement:
                        statements.append(statement)
                    current = []
        tail = "".join(current).strip()
        if tail and re.search(r"(?im)^\s*(assume|guarantee|eq|const|assign|assert)\b", tail):
            statements.append(tail if tail.endswith(";") else tail + ";")
        return statements

    def _target_feature_profiles(self, state: PipelineState, target_name: str) -> dict[str, dict[str, str]]:
        block = self._component_block(state.raw_aadl, target_name)
        if not block:
            return {}
        data_scalars = self._data_scalar_map(state)
        profiles: dict[str, dict[str, str]] = {}
        self._collect_feature_profiles(block, data_scalars, profiles)
        if not profiles and "." in (target_name or ""):
            fallback = self._component_block(state.raw_aadl, target_name.split(".", 1)[0])
            if fallback:
                self._collect_feature_profiles(fallback, data_scalars, profiles)
        return profiles

    def _collect_feature_profiles(self, block: str, data_scalars: dict[str, str], profiles: dict[str, dict[str, str]]) -> None:
        feature_pattern = re.compile(
            r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(in|out|requires|provides)\s+([^;]+?)\s*;",
            re.IGNORECASE | re.MULTILINE,
        )
        for match in feature_pattern.finditer(block):
            name = match.group(1)
            direction = match.group(2).lower()
            spec = re.sub(r"--.*$", "", match.group(3).strip(), flags=re.MULTILINE)
            spec_lower = spec.lower()
            if "access" in spec_lower and "port" not in spec_lower and "parameter" not in spec_lower:
                profiles[name] = {"direction": direction, "kind": "access", "scalar": "opaque"}
                continue
            if "event port" in spec_lower and "data port" not in spec_lower:
                profiles[name] = {"direction": direction, "kind": "event", "scalar": "event"}
                continue
            data_type = ""
            type_match = re.search(
                r"\b(?:data\s+port|event\s+data\s+port|parameter)\s+([A-Za-z_][A-Za-z0-9_]*(?:(?:::|\.)[A-Za-z_][A-Za-z0-9_]*)*)",
                spec,
                flags=re.IGNORECASE,
            )
            if type_match:
                data_type = type_match.group(1)
            builtin_scalars = {
                "float": "real",
                "real": "real",
                "double": "real",
                "integer": "int",
                "int": "int",
                "boolean": "bool",
                "bool": "bool",
            }
            data_type_key = data_type.lower()
            scalar = (
                data_scalars.get(data_type_key)
                or data_scalars.get(data_type.split("::")[-1].lower())
                or builtin_scalars.get(data_type_key)
                or builtin_scalars.get(data_type.split("::")[-1].lower())
                or "opaque"
            )
            profiles[name] = {"direction": direction, "kind": "data", "scalar": scalar, "data_type": data_type}

    def _component_block(self, aadl_model: str, name: str) -> str:
        declaration = r"(?:system|process|thread|device|abstract|subprogram)(?:\s+implementation)?"
        match = re.search(
            rf"(?ims)^\s*{declaration}\s+{re.escape(name)}\b.*?^\s*end\s+{re.escape(name)}\s*;",
            aadl_model or "",
        )
        return match.group(0) if match else ""

    def _data_field_map(self, state: PipelineState) -> dict[str, list[dict[str, str]]]:
        texts = [state.raw_aadl or ""]
        for ref in state.references or []:
            if isinstance(ref, dict):
                texts.append(str(ref.get("content", "") or ""))
        data_scalars = self._data_scalar_map(state)
        fields_by_type: dict[str, list[dict[str, str]]] = {}
        impl_pattern = re.compile(
            r"(?ims)^\s*data\s+implementation\s+([A-Za-z_][A-Za-z0-9_]*(?:(?:::|\.)[A-Za-z_][A-Za-z0-9_]*)*)\b(.*?)^\s*end\s+\1\s*;",
            flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
        )
        field_pattern = re.compile(
            r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*data\s+([A-Za-z_][A-Za-z0-9_]*(?:(?:::|\.)[A-Za-z_][A-Za-z0-9_]*)*)\s*;",
            flags=re.IGNORECASE | re.MULTILINE,
        )
        for text in texts:
            package_match = re.search(r"(?im)^\s*package\s+([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*)\b", text or "")
            package = package_match.group(1) if package_match else ""
            for match in impl_pattern.finditer(text or ""):
                impl_name = match.group(1)
                body = match.group(2) or ""
                fields = []
                for field_match in field_pattern.finditer(body):
                    field_type = field_match.group(2)
                    builtin_scalars = {
                        "float": "real",
                        "real": "real",
                        "double": "real",
                        "integer": "int",
                        "int": "int",
                        "boolean": "bool",
                        "bool": "bool",
                    }
                    field_type_key = field_type.lower()
                    field_type_tail = re.split(r"::|\.", field_type)[-1].lower()
                    scalar = (
                        data_scalars.get(field_type_key)
                        or data_scalars.get(field_type_tail)
                        or builtin_scalars.get(field_type_key)
                        or builtin_scalars.get(field_type_tail)
                        or "opaque"
                    )
                    fields.append({"name": field_match.group(1), "data_type": field_type, "scalar": scalar})
                if not fields:
                    continue
                keys = {impl_name.lower(), impl_name.split("::")[-1].lower()}
                if package and "::" not in impl_name:
                    keys.add(f"{package}::{impl_name}".lower())
                for key in keys:
                    fields_by_type[key] = fields
        return fields_by_type

    def _data_scalar_map(self, state: PipelineState) -> dict[str, str]:
        texts = [state.raw_aadl or ""]
        for ref in state.references or []:
            if isinstance(ref, dict):
                texts.append(str(ref.get("content", "") or ""))
        mapping: dict[str, str] = {}
        inheritance: dict[str, str] = {}
        for text in texts:
            package_match = re.search(r"(?im)^\s*package\s+([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*)\b", text or "")
            package = package_match.group(1) if package_match else ""
            for extends_match in re.finditer(
                r"(?ims)^\s*data\s+([A-Za-z_][A-Za-z0-9_]*(?:(?:::|\.)[A-Za-z_][A-Za-z0-9_]*)*)\s+extends\s+([A-Za-z_][A-Za-z0-9_]*(?:(?:::|\.)[A-Za-z_][A-Za-z0-9_]*)*)\b",
                text or "",
            ):
                child = extends_match.group(1)
                parent = extends_match.group(2)
                parent_key = parent.lower() if "::" in parent or not package else f"{package}::{parent}".lower()
                child_keys = [child.lower(), child.split("::")[-1].lower()]
                if package and "::" not in child:
                    child_keys.append(f"{package}::{child}".lower())
                for child_key in child_keys:
                    inheritance[child_key] = parent_key
            for match in re.finditer(
                r"(?ims)^\s*data\s+([A-Za-z_][A-Za-z0-9_]*(?:(?:::|\.)[A-Za-z_][A-Za-z0-9_]*)*)\b(.*?)(?:^\s*end\s+\1\s*;)",
                text or "",
            ):
                name = match.group(1)
                body = match.group(2)
                rep_match = re.search(
                    r"Data_Model::(?:Data_Representation|Representation)\s*=>\s*(?:\(\s*)?[\"']?([A-Za-z_][A-Za-z0-9_\s]*)[\"']?",
                    body,
                    flags=re.IGNORECASE,
                )
                rep = re.sub(r"\s+", " ", rep_match.group(1).strip().lower()) if rep_match else ""
                if not rep:
                    source_match = re.search(r"Type_Source_Name\s*=>\s*[\"']([^\"']+)[\"']", body, flags=re.IGNORECASE)
                    source_name = source_match.group(1).lower() if source_match else ""
                    if any(token in source_name for token in ("float", "double")):
                        rep = "float"
                    elif any(token in source_name for token in ("bool", "boolean")):
                        rep = "boolean"
                    elif any(token in source_name for token in ("int", "long", "short")):
                        rep = "integer"
                scalar = {
                    "boolean": "bool",
                    "bool": "bool",
                    "float": "real",
                    "real": "real",
                    "fixed": "real",
                    "double": "real",
                    "integer": "int",
                    "int": "int",
                    "unsigned int": "int",
                    "signed int": "int",
                    "short": "int",
                    "unsigned short": "int",
                    "long": "int",
                    "unsigned long": "int",
                }.get(rep, "opaque")
                mapping[name.lower()] = scalar
                if package:
                    mapping[f"{package}::{name}".lower()] = scalar
        changed = True
        while changed:
            changed = False
            for child, parent in inheritance.items():
                if mapping.get(child) != "opaque":
                    continue
                parent_scalar = mapping.get(parent) or mapping.get(parent.split("::")[-1])
                if parent_scalar and parent_scalar != "opaque":
                    mapping[child] = parent_scalar
                    changed = True
        return mapping

    def _compact_statement(self, statement: str) -> str:
        return re.sub(r"\s+", " ", (statement or "").strip())[:500]

    def _indent_statement(self, statement: str) -> str:
        lines = [line.rstrip() for line in (statement or "").strip().splitlines()]
        return "\n".join("  " + line.strip() if line.strip() else line for line in lines)

    def _infer_component_type(self, aadl_model: str) -> str:
        match = __import__("re").search(r"^\s*system\s+([A-Za-z_][A-Za-z0-9_]*)", aadl_model, flags=__import__("re").MULTILINE)
        if not match:
            raise ValueError("Unable to infer component type for deterministic fusion.")
        return match.group(1)

    def _insert_before_end(self, aadl_model: str, name: str, annex: str) -> str:
        import re

        pattern = re.compile(rf"(^\s*end\s+{re.escape(name)}\s*;\s*$)", re.IGNORECASE | re.MULTILINE)
        match = pattern.search(aadl_model)
        if not match:
            raise ValueError(f"Unable to find insertion point before 'end {name};'.")
        indent = re.match(r"\s*", match.group(1)).group(0)
        block = "\n".join(indent + line if line.strip() else line for line in annex.splitlines())
        return aadl_model[: match.start()] + block + "\n" + aadl_model[match.start() :]

    def _replace_or_insert_annex(self, aadl_model: str, name: str, annex: str) -> str:
        import re

        declaration = r"(?:system|process|thread|device|abstract|subprogram)(?:\s+implementation)?"
        pattern = re.compile(
            rf"(^\s*{declaration}\s+{re.escape(name)}\b.*?)(^\s*end\s+{re.escape(name)}\s*;\s*$)",
            re.IGNORECASE | re.MULTILINE | re.DOTALL,
        )
        match = pattern.search(aadl_model)
        if not match:
            return self._insert_before_end(aadl_model, name, annex)
        body = match.group(1)
        end_line = match.group(2)
        body = re.sub(
            r"\n?\s*annex\s+agree\s*\{\*\*.*?\*\*\}\s*;\s*",
            "\n",
            body,
            flags=re.IGNORECASE | re.DOTALL,
        ).rstrip()
        indent = re.match(r"\s*", end_line).group(0)
        block = "\n".join(indent + line if line.strip() else line for line in annex.splitlines())
        replacement = body + "\n" + block + "\n" + end_line
        return aadl_model[: match.start()] + replacement + aadl_model[match.end() :]

    def _visible_outputs(self, state: PipelineState) -> list[str]:
        ports: list[str] = []
        if isinstance(state.model_analysis, dict):
            whitelist = state.model_analysis.get("identifier_whitelist", {})
            if isinstance(whitelist, dict):
                ports.extend(port for port in whitelist.get("ports", []) if isinstance(port, str))
            for item in state.model_analysis.get("ports", []) or []:
                if isinstance(item, dict):
                    name = item.get("name")
                    direction = str(item.get("direction", "")).lower()
                    if isinstance(name, str) and ("out" in direction or not direction):
                        ports.append(name)
                elif isinstance(item, str):
                    ports.append(item)
        requirement = state.raw_requirement.lower()
        ports = list(dict.fromkeys(ports))
        outputs = [port for port in ports if isinstance(port, str) and port.lower() in requirement]
        if outputs:
            return outputs
        return [port for port in ports if isinstance(port, str)]


class ValidationRepairAgent:
    def __init__(self, runtime: AgentRuntime):
        self.runtime = runtime

    def run(self, state: PipelineState, aadl_diagnostics: Any, agree_diagnostics: Any, rag_enabled: bool) -> Dict[str, str]:
        visible_identifiers = RequirementAnalystAgent(self.runtime)._target_visible_identifiers(state)
        current_artifact = state.final_aadl or state.fused_aadl
        target_type, _ = split_target_component_names(state.target_component, current_artifact)
        target_interface_context = RequirementAnalystAgent(self.runtime)._target_interface_context(state)
        requirement_analysis = AgreeGeneratorAgent(self.runtime)._format_requirement_analysis(state.requirement_analysis)
        current_annex_context = self._current_annex_context(current_artifact)
        diagnostic_line_context = self._diagnostic_line_context(current_artifact, aadl_diagnostics, agree_diagnostics)
        target_model_context = self.runtime.target_model_context(state, visible_identifiers, max_chars=5000)
        diagnostic_context = "\n".join(
            [
                "AADL Inspector diagnostics:",
                json.dumps(aadl_diagnostics, ensure_ascii=False, indent=2),
                "AGREE validator diagnostics:",
                json.dumps(agree_diagnostics, ensure_ascii=False, indent=2),
            ]
        )
        compiled = self.runtime.compiled_agent_context(
            state,
            "validation_repair",
            rag_enabled,
            visible_identifiers=visible_identifiers,
            diagnostic_context=diagnostic_context,
        )
        round_number = len(state.repair_history) + 1
        self._save_repair_focus(
            state,
            round_number,
            current_annex_context=current_annex_context,
            diagnostic_line_context=diagnostic_line_context,
            target_interface_context=target_interface_context,
            requirement_analysis=requirement_analysis,
            target_model_context=target_model_context,
        )
        if self.runtime.strategy_guidance_enabled():
            repair_plan = self._plan_repair(
                state,
                aadl_diagnostics,
                agree_diagnostics,
                compiled,
                round_number,
                target_interface_context=target_interface_context,
                requirement_analysis=requirement_analysis,
                current_annex_context=current_annex_context,
                diagnostic_line_context=diagnostic_line_context,
                target_model_context=target_model_context,
            )
        else:
            repair_plan = {
                "problems": [],
                "repair_mode": "edit_annex",
                "executor_steps": [
                    "Use the validator diagnostics and focused annex context to make the smallest legal repair."
                ],
            }
        prompt = self.runtime.prompts.render(
            "validation_repair_execute",
            reference_context="",
            aadl_diagnostics=json.dumps(aadl_diagnostics, ensure_ascii=False, indent=2),
            agree_diagnostics=json.dumps(agree_diagnostics, ensure_ascii=False, indent=2),
            repair_plan=json.dumps(repair_plan, ensure_ascii=False, indent=2),
            available_symbols=compiled["available_symbols"],
            target_component=state.target_component,
            requirement_text=state.raw_requirement,
            requirement_analysis=requirement_analysis,
            target_interface_context=target_interface_context,
            current_annex_context=current_annex_context,
            current_aadl_artifact=self._complete_model_context_for_repair(current_artifact, repair_plan),
            diagnostic_line_context=diagnostic_line_context,
            target_model_context=target_model_context,
        )
        response = self.runtime.call(
            state,
            (
                "Execute the repair plan. Return repaired AGREE annex block(s) only unless the plan "
                "explicitly asks for a complete AADL artifact. Do not return the same invalid annex "
                "unchanged. Keep the output syntactically valid for the AGREE validator."
            ),
            prompt,
            temperature=0.1,
            stage_name=f"validation_repair_execute_round_{round_number}",
        )
        repaired_result = recover_section(response, "REPAIRED_AADL", "validation_repair")
        repaired = repaired_result.value or response
        if repaired_result.actions:
            self.runtime.record_recovery(state, "validation_repair", repaired_result.actions)
        if repaired.strip().lower().startswith("diagnostic_blocker"):
            raise ValueError(repaired.strip())
        if not repaired:
            raise ValueError("Repair response did not contain <REPAIRED_AADL>.")
        repaired_code = self._coerce_repair_to_complete_artifact(state, current_artifact, repaired, repair_plan)
        if "public package " in repaired_code.lower():
            raise ValueError("Repair attempted to create a nested package; rejected by structural binding guard.")
        return {
            "raw_response": response,
            "diagnosis": self._plan_summary(repair_plan),
            "repair_plan": json.dumps(repair_plan, ensure_ascii=False, indent=2),
            "repaired_aadl": repaired_code,
        }

    def _plan_repair(
        self,
        state: PipelineState,
        aadl_diagnostics: Any,
        agree_diagnostics: Any,
        compiled: dict[str, str],
        round_number: int,
        *,
        target_interface_context: str,
        requirement_analysis: str,
        current_annex_context: str,
        diagnostic_line_context: str,
        target_model_context: str,
    ) -> dict[str, Any]:
        prompt = self.runtime.prompts.render(
            "validation_repair_plan",
            aadl_diagnostics=json.dumps(aadl_diagnostics, ensure_ascii=False, indent=2),
            agree_diagnostics=json.dumps(agree_diagnostics, ensure_ascii=False, indent=2),
            syntax_reference=compiled["syntax_reference"],
            pattern_reference=compiled["pattern_reference"],
            available_symbols=compiled["available_symbols"],
            target_component=state.target_component,
            requirement_text=state.raw_requirement,
            requirement_analysis=requirement_analysis,
            target_interface_context=target_interface_context,
            current_annex_context=current_annex_context,
            diagnostic_line_context=diagnostic_line_context,
            target_model_context=target_model_context,
        )
        response = self.runtime.call(
            state,
            (
                "Analyze validator diagnostics against the focused AGREE annex context. Produce a strict "
                "JSON repair plan only. Do not output repaired code."
            ),
            prompt,
            temperature=0.0,
            stage_name=f"validation_repair_plan_round_{round_number}",
        )
        recovered = recover_json_object(
            response,
            "validation_repair_plan",
            defaults={
                "problems": [],
                "repair_mode": "edit_annex",
                "executor_steps": [],
            },
        )
        self.runtime.record_recovery(state, "validation_repair_plan", recovered.actions)
        plan = recovered.value if isinstance(recovered.value, dict) else {}
        plan.setdefault("problems", [])
        plan.setdefault("repair_mode", "edit_annex")
        plan.setdefault("executor_steps", [])
        report_dir = state.report_dir(self.runtime.config.result_root)
        report_dir.mkdir(parents=True, exist_ok=True)
        (report_dir / f"repair_plan_round_{round_number}.json").write_text(
            json.dumps(plan, ensure_ascii=False, indent=2),
            encoding="utf-8",
            errors="replace",
        )
        return plan

    def _plan_summary(self, repair_plan: dict[str, Any]) -> str:
        problems = repair_plan.get("problems") if isinstance(repair_plan, dict) else []
        if not isinstance(problems, list) or not problems:
            return json.dumps(repair_plan, ensure_ascii=False)[:1000]
        summaries = []
        for problem in problems[:5]:
            if isinstance(problem, dict):
                summaries.append(f"{problem.get('diagnostic', '')}: {problem.get('cause', '')} -> {problem.get('minimal_edit', '')}")
        return "\n".join(item for item in summaries if item).strip()

    def _save_repair_focus(
        self,
        state: PipelineState,
        round_number: int,
        *,
        current_annex_context: str,
        diagnostic_line_context: str,
        target_interface_context: str,
        requirement_analysis: str,
        target_model_context: str,
    ) -> None:
        report_dir = state.report_dir(self.runtime.config.result_root)
        report_dir.mkdir(parents=True, exist_ok=True)
        text = "\n\n".join(
            [
                f"round={round_number}",
                "[TARGET INTERFACE]\n" + target_interface_context,
                "[REQUIREMENT ANALYSIS]\n" + requirement_analysis,
                "[CURRENT ANNEX CONTEXT]\n" + current_annex_context,
                "[DIAGNOSTIC LINE CONTEXT]\n" + diagnostic_line_context,
                "[TARGET MODEL CONTEXT]\n" + target_model_context,
            ]
        )
        (report_dir / f"repair_focus_round_{round_number}.txt").write_text(text, encoding="utf-8", errors="replace")

    def _complete_model_context_for_repair(self, current_artifact: str, repair_plan: dict[str, Any]) -> str:
        if self._repair_plan_requires_complete_model(repair_plan):
            return current_artifact
        return "Full model omitted because the repair plan is annex-local."

    def _current_annex_context(self, artifact: str) -> str:
        blocks: list[str] = []
        for match in re.finditer(r"annex\s+agree\s*\{\*\*.*?\*\*\}\s*;", artifact or "", flags=re.IGNORECASE | re.DOTALL):
            start_line = artifact.count("\n", 0, match.start()) + 1
            end_line = artifact.count("\n", 0, match.end()) + 1
            owner = self._owner_before_offset(artifact, match.start())
            header = f"-- owner: {owner or 'unknown'} | lines {start_line}-{end_line}"
            blocks.append(header + "\n" + match.group(0).strip())
        return "\n\n".join(blocks) if blocks else "No AGREE annex block is present."

    def _diagnostic_line_context(self, artifact: str, aadl_diagnostics: Any, agree_diagnostics: Any, radius: int = 4) -> str:
        line_numbers: list[int] = []
        for item in self._flatten_diagnostics(aadl_diagnostics) + self._flatten_diagnostics(agree_diagnostics):
            for match in re.finditer(r"\bline\s+(\d+)\b", item, flags=re.IGNORECASE):
                line_numbers.append(int(match.group(1)))
        if not line_numbers:
            return "No validator line numbers were available."
        lines = artifact.splitlines()
        sections: list[str] = []
        for line_number in list(dict.fromkeys(line_numbers))[:12]:
            start = max(1, line_number - radius)
            end = min(len(lines), line_number + radius)
            rendered = []
            for current in range(start, end + 1):
                marker = ">>" if current == line_number else "  "
                rendered.append(f"{marker} {current}: {lines[current - 1]}")
            sections.append("\n".join(rendered))
        return "\n\n".join(sections)

    def _flatten_diagnostics(self, diagnostics: Any) -> list[str]:
        if diagnostics is None:
            return []
        if isinstance(diagnostics, str):
            return [diagnostics]
        if isinstance(diagnostics, dict):
            return [json.dumps(diagnostics, ensure_ascii=False)]
        if isinstance(diagnostics, list):
            flattened: list[str] = []
            for item in diagnostics:
                flattened.extend(self._flatten_diagnostics(item))
            return flattened
        return [str(diagnostics)]

    def _owner_before_offset(self, artifact: str, offset: int) -> str:
        declaration = re.compile(
            r"^\s*(system|process|thread|device|abstract|subprogram)(\s+implementation)?\s+([A-Za-z_][A-Za-z0-9_.]*)\b",
            flags=re.IGNORECASE | re.MULTILINE,
        )
        owner = ""
        for match in declaration.finditer(artifact or "", 0, max(0, offset)):
            owner = match.group(3)
        return owner

    def _same_annex_returned(self, current_artifact: str, repaired: str) -> bool:
        current_annexes = extract_annex_blocks(current_artifact)
        repaired_annexes = extract_annex_blocks(normalize_agree_annex_delimiters(strip_code_fence(repaired)))
        if not current_annexes or not repaired_annexes:
            return False
        normalized_current = {re.sub(r"\s+", " ", annex).strip().lower() for annex in current_annexes}
        normalized_repaired = {re.sub(r"\s+", " ", annex).strip().lower() for annex in repaired_annexes}
        return bool(normalized_repaired) and normalized_repaired.issubset(normalized_current)

    def _coerce_repair_to_complete_artifact(
        self,
        state: PipelineState,
        current_artifact: str,
        repaired: str,
        repair_plan: dict[str, Any] | None = None,
    ) -> str:
        candidate = normalize_agree_annex_delimiters(strip_code_fence(repaired))
        if self._repair_plan_requires_complete_model(repair_plan) and self._is_plausible_complete_aadl(candidate, current_artifact):
            self.runtime.record_recovery(
                state,
                "validation_repair",
                [
                    {
                        "stage": "validation_repair",
                        "action": "complete_aadl_repair_used",
                        "detail": "Repair plan requested complete-model repair; accepted the returned AADL artifact for validation.",
                        "confidence": "medium",
                    }
                ],
            )
            return candidate
        annexes = extract_annex_blocks(candidate)
        if annexes:
            merged = self._replace_repaired_annexes(current_artifact, annexes, state, repair_plan)
            self.runtime.record_recovery(
                state,
                "validation_repair",
                [
                    {
                        "stage": "validation_repair",
                        "action": "repair_annexes_merged_locally",
                        "detail": "Repair returned AGREE annex block(s); preserved the full AADL architecture and replaced target annex block(s) locally.",
                        "confidence": "high",
                    }
                ],
            )
            return merged
        if self._is_plausible_complete_aadl(candidate, current_artifact):
            raise ValueError("Repair returned a complete AADL artifact with no detectable AGREE annex block.")
        raise ValueError("Repair output contained no detectable AGREE annex block and was not a complete AADL artifact.")

    def _repair_plan_requires_complete_model(self, repair_plan: dict[str, Any] | None) -> bool:
        if not isinstance(repair_plan, dict):
            return False
        if str(repair_plan.get("repair_mode") or "").strip().lower() in {"edit_full_model", "edit_owner"}:
            return True
        text = json.dumps(repair_plan, ensure_ascii=False).lower()
        markers = (
            "complete aadl",
            "complete model",
            "complete-model",
            "full aadl",
            "full model",
            "model-level",
            "owner-level",
            "wrong owner",
            "wrong scope",
            "delete an entire annex",
            "delete the entire annex",
            "remove an entire annex",
            "remove the entire annex",
            "moving clauses between",
            "move clauses between",
            "move the guarantee",
            "duplicate owner",
            "with clause",
            "package",
            "property set",
            "property-set",
            "dependency",
        )
        return any(marker in text for marker in markers)

    def _is_plausible_complete_aadl(self, candidate: str, current_artifact: str) -> bool:
        if not candidate:
            return False
        lowered = candidate.lower()
        if "package " not in lowered or "end " not in lowered:
            return False
        if current_artifact and len(candidate) < max(100, int(len(current_artifact) * 0.8)):
            return False
        current_package = re.search(r"(?im)^\s*package\s+([A-Za-z_][A-Za-z0-9_:]*)\b", current_artifact or "")
        candidate_package = re.search(r"(?im)^\s*package\s+([A-Za-z_][A-Za-z0-9_:]*)\b", candidate or "")
        if current_package and candidate_package:
            return current_package.group(1).lower() == candidate_package.group(1).lower()
        return True

    def _replace_repaired_annexes(
        self,
        current_artifact: str,
        annexes: list[str],
        state: PipelineState,
        repair_plan: dict[str, Any] | None = None,
    ) -> str:
        component_type, implementation = split_target_component_names(state.target_component, current_artifact)
        sanitizer = ModelFusionAgent(self.runtime)
        output = current_artifact
        if len(annexes) >= 2:
            type_annex, type_actions = sanitizer._sanitize_annex_for_target(state, annexes[0], component_type)
            impl_annex, impl_actions = sanitizer._sanitize_annex_for_target(state, annexes[1], implementation)
            self.runtime.record_recovery(state, "validation_repair", type_actions + impl_actions)
            if type_annex:
                output = self._replace_or_insert_annex(output, component_type, type_annex)
            if implementation and impl_annex:
                output = self._replace_or_insert_annex(output, implementation, impl_annex)
        else:
            annex, actions = sanitizer._sanitize_annex_for_target(state, annexes[0], component_type)
            self.runtime.record_recovery(state, "validation_repair", actions)
            if annex:
                planned_scope = self._planned_repair_scope(repair_plan)
                if planned_scope == "component_type":
                    return self._replace_or_insert_annex(output, component_type, annex)
                if planned_scope == "component_implementation" and implementation:
                    return self._replace_or_insert_annex(output, implementation, annex)
                output = self._replace_first_target_annex(output, component_type, implementation, annex)
        return output

    def _planned_repair_scope(self, repair_plan: dict[str, Any] | None) -> str:
        if not isinstance(repair_plan, dict):
            return ""
        mode = str(repair_plan.get("repair_mode") or "").strip().lower()
        if mode == "edit_annex":
            return "component_type"
        targets = repair_plan.get("target_annexes")
        if not isinstance(targets, list):
            return ""
        scopes = [
            str(item.get("scope") or "").strip().lower()
            for item in targets
            if isinstance(item, dict)
        ]
        if "component_type" in scopes:
            return "component_type"
        if "component_implementation" in scopes:
            return "component_implementation"
        return ""

    def _replace_first_target_annex(self, aadl_model: str, component_type: str, implementation: str, annex: str) -> str:
        for name in (component_type, implementation):
            if self._component_has_annex(aadl_model, name):
                return self._replace_or_insert_annex(aadl_model, name, annex)
        return self._replace_or_insert_annex(aadl_model, component_type, annex)

    def _component_has_annex(self, aadl_model: str, name: str) -> bool:
        declaration = r"(?:system|process|thread|device|abstract|subprogram)(?:\s+implementation)?"
        pattern = re.compile(
            rf"^\s*{declaration}\s+{re.escape(name)}\b.*?annex\s+agree\s*\{{\*\*.*?^\s*end\s+{re.escape(name)}\s*;\s*$",
            re.IGNORECASE | re.MULTILINE | re.DOTALL,
        )
        return bool(pattern.search(aadl_model or ""))

    def _replace_or_insert_annex(self, aadl_model: str, name: str, annex: str) -> str:
        declaration = r"(?:system|process|thread|device|abstract|subprogram)(?:\s+implementation)?"
        pattern = re.compile(
            rf"(^\s*{declaration}\s+{re.escape(name)}\b.*?)(^\s*end\s+{re.escape(name)}\s*;\s*$)",
            re.IGNORECASE | re.MULTILINE | re.DOTALL,
        )
        match = pattern.search(aadl_model)
        if not match:
            raise ValueError(f"Unable to find repair insertion point before 'end {name};'.")
        body = re.sub(
            r"\n?\s*annex\s+agree\s*\{\*\*.*?\*\*\}\s*;\s*",
            "\n",
            match.group(1),
            flags=re.IGNORECASE | re.DOTALL,
        ).rstrip()
        indent = re.match(r"\s*", match.group(2)).group(0)
        block = "\n".join(indent + line if line.strip() else line for line in annex.splitlines())
        replacement = body + "\n" + block + "\n" + match.group(2)
        return aadl_model[: match.start()] + replacement + aadl_model[match.end() :]


class BareDirectAgent:
    def __init__(self, runtime: AgentRuntime):
        self.runtime = runtime

    def run(self, state: PipelineState) -> str:
        reference_context = "\n\n".join(
            f"-- BEGIN REFERENCE AADL FILE: {item.get('path', 'unknown')}\n{item.get('content', '')}\n-- END REFERENCE AADL FILE: {item.get('path', 'unknown')}"
            for item in state.references
        )
        prompt = self.runtime.prompts.render(
            "bare_direct",
            target_component=state.target_component,
            requirement_text=state.raw_requirement,
            aadl_model=state.raw_aadl,
            reference_context=reference_context,
        )
        response = self.runtime.call(
            state,
            "You are the direct-generation bare model baseline. Return complete AADL only.",
            prompt,
            temperature=0.2,
            stage_name="bare_direct",
        )
        return strip_code_fence(response)
