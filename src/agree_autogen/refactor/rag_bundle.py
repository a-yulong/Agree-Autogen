"""Tri-modular RAG bundle implementation.

Every RAG-enabled agent invocation receives a fixed Ksyn/Kexp/Kdef bundle.
Kdef cards are hard constraints; Ksyn and Kexp cards are selected by
case-specific retrieval features from the local knowledge base.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List


@dataclass
class RagCard:
    kind: str
    card_id: str
    source: str
    topic: str
    body: str
    metadata: Dict[str, str]


@dataclass
class RetrievalFeatures:
    target_scope: str
    target_component: str
    visible_inputs: List[str]
    visible_outputs: List[str]
    visible_variables: List[str]
    contract_patterns: List[str]
    logic_features: List[str]
    relevant_identifiers: List[str]
    required_operators: List[str]
    avoid_patterns: List[str]
    source_priority: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "target_scope": self.target_scope,
            "target_component": self.target_component,
            "visible_inputs": self.visible_inputs,
            "visible_outputs": self.visible_outputs,
            "visible_variables": self.visible_variables,
            "contract_patterns": self.contract_patterns,
            "logic_features": self.logic_features,
            "relevant_identifiers": self.relevant_identifiers,
            "required_operators": self.required_operators,
            "avoid_patterns": self.avoid_patterns,
            "source_priority": self.source_priority,
        }


@dataclass
class RetrievalQuery:
    query: str
    source: str | None
    purpose: str

    def to_dict(self) -> Dict[str, str | None]:
        return {"query": self.query, "source": self.source, "purpose": self.purpose}


@dataclass
class ScoredCard:
    card: RagCard
    score: float
    details: Dict[str, Any]


KDEF_HARD_CARDS: List[RagCard] = [
    RagCard(
        kind="Kdef",
        card_id="KDEF-SCOPE-NAMING",
        source="built-in defensive rule",
        topic="Scope & Naming",
        body=(
            "Rule: AGREE expressions may only reference identifiers visible in the current "
            "component scope. Must: use exact current-case names from the model index. "
            "Forbid: copying identifiers from examples or inventing ports/components."
        ),
        metadata={"category": "Scope & Naming", "severity": "hard"},
    ),
    RagCard(
        kind="Kdef",
        card_id="KDEF-SYNTAX-PROHIBITIONS",
        source="built-in defensive rule",
        topic="Syntax Prohibitions",
        body=(
            "Rule: return only the requested structured format. Must: preserve annex agree "
            "{** ... **}; delimiters when an annex is requested. Forbid: Markdown fences "
            "inside AADL artifacts, free-form explanations, duplicate declarations, and "
            "standalone assignments outside legal AGREE constructs."
        ),
        metadata={"category": "Syntax Prohibitions", "severity": "hard"},
    ),
    RagCard(
        kind="Kdef",
        card_id="KDEF-STRUCTURAL-BINDING",
        source="built-in defensive rule",
        topic="Structural Binding",
        body=(
            "Rule: component types and implementations have different legal scopes. Must: "
            "place assume/guarantee/eq/const in the component type when they describe "
            "interface behavior, and implementation-oriented assign/assert clauses in the "
            "matching implementation. Forbid: redesigning architecture during fusion/repair."
        ),
        metadata={"category": "Structural Binding", "severity": "hard"},
    ),
    RagCard(
        kind="Kdef",
        card_id="KDEF-UNDER-SPECIFIED-VALIDITY",
        source="built-in grounding guidance",
        topic="Underspecified Validity and Envelopes",
        body=(
            "Guidance: requirements often mention validity, legal operating states, safe "
            "boundaries, or algorithm envelopes without giving the actual state set, "
            "bound, or relation. Treat those phrases as missing information unless the "
            "current requirement or model provides a concrete value, named constant, "
            "enumeration state, or visible relation. Use range examples only when the "
            "case supplies the bounds or relation to instantiate."
        ),
        metadata={"category": "Grounding", "severity": "guidance"},
    ),
]


def _tokenize(text: str) -> set[str]:
    return {tok.lower() for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_]+", text or "")}


def _truncate(text: str, limit: int = 1800) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:limit]


def _ordered(values: Iterable[str]) -> List[str]:
    seen = set()
    ordered = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


def _contains_any(text: str, needles: Iterable[str]) -> bool:
    lowered = text.lower()
    return any(needle and needle.lower() in lowered for needle in needles)


def _has_word(text: str, word: str) -> bool:
    return bool(re.search(rf"(?<![A-Za-z0-9_]){re.escape(word)}(?![A-Za-z0-9_])", text or "", flags=re.IGNORECASE))


def _has_any_word(text: str, words: Iterable[str]) -> bool:
    return any(_has_word(text, word) for word in words)


def _infer_card_tags(card: RagCard) -> set[str]:
    metadata_tags = card.metadata.get("tags", "")
    if metadata_tags:
        return {tag.strip() for tag in metadata_tags.split(",") if tag.strip()}

    text = f"{card.topic} {card.body} {' '.join(str(v) for v in card.metadata.values())}".lower()
    tags: set[str] = set()
    if any(token in text for token in ("if ", " then ", " else ", "conditional", "selector", "chosen")):
        tags.add("conditional_assignment")
        tags.add("if_then_else")
    if any(token in text for token in ("out data port", "output", "assign ", "flag follows", "mirrors")):
        tags.add("output_assignment")
    if any(token in text for token in ("range", "within", "lower_limit", "upper_limit", "min_", "max_", "bounded")):
        tags.add("range_constraint")
    if any(token in text for token in ("pre(", "previous", "history", "nondecreasing")):
        tags.add("temporal_history")
        tags.add("history_pre")
    if any(token in text for token in (" and ", " or ", " not ")):
        tags.add("boolean_logic")
    if any(token in text for token in ("=>", "implies", "implication")):
        tags.add("implication")
    if any(token in text for token in ("component implementation", "system implementation", ".impl")):
        tags.add("component_implementation")
    if any(token in text for token in ("component type", "system ")):
        tags.add("component_type")
    if any(token in text for token in (">=", "<=", ">", "<", "comparison", "difference")):
        tags.add("comparison")
    if "=" in text:
        tags.add("equality")
    if any(token in text for token in ("+", "-", "*", "/", "arithmetic", "counter")):
        tags.add("arithmetic_constraint")
    if "annex agree {**" in text:
        tags.add("valid_annex_delimiter")
    if "range_constraint" in tags and not ({"conditional_assignment", "output_assignment", "temporal_history"} & tags):
        tags.add("range_only")
    return tags


class RagBundleBuilder:
    """Build fixed-size Ksyn/Kexp/Kdef bundles from a local knowledge base."""

    def __init__(self, knowledge_base: str | Path):
        self.root = Path(knowledge_base)
        self.ksyn_count = int(os.environ.get("AGREE_RAG_KSYN_COUNT", "3"))
        self.kexp_count = int(os.environ.get("AGREE_RAG_KEXP_COUNT", "3"))
        self.kdef_count = int(os.environ.get("AGREE_RAG_KDEF_COUNT", "3"))
        self.chunk_size = int(os.environ.get("AGREE_RAG_CHUNK_SIZE", "465"))
        self.chunk_overlap = int(os.environ.get("AGREE_RAG_CHUNK_OVERLAP", "80"))
        self.retrieval_mode = os.environ.get("AGREE_RAG_RETRIEVAL_MODE", "hybrid").lower()
        self.embedding_model_name = os.environ.get("AGREE_RAG_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
        self._embedding_model: Any = None
        self._embedding_error: str | None = None
        self._retrieval_cards: Dict[str, List[RagCard]] | None = None
        self._embedding_cards: List[RagCard] | None = None
        self._embedding_matrix: Any = None
        self.cards = {
            "Ksyn": self._load_ksyn_cards(),
            "Kexp": self._load_kexp_cards(),
            "Kdef": self._load_kdef_cards(),
        }

    def build(self, queries: Dict[str, str], enabled: bool) -> str:
        if not enabled:
            return "RAG_DISABLED"
        selected = {
            "Ksyn": self._select("Ksyn", queries.get("Ksyn", ""), self.ksyn_count),
            "Kexp": self._select("Kexp", queries.get("Kexp", ""), self.kexp_count),
            "Kdef": self._select("Kdef", queries.get("Kdef", ""), self.kdef_count),
        }
        return self.format_bundle(selected)

    def build_enhanced(
        self,
        queries: Dict[str, str],
        enabled: bool,
        requirement: str,
        aadl_context: str,
        target_component: str | None,
        agent_name: str,
        model_analysis: Any = None,
        diagnostic_context: str = "",
    ) -> Dict[str, Any]:
        if not enabled:
            return {
                "context": "RAG_DISABLED",
                "metadata": {"Ksyn": [], "Kexp": [], "Kdef": []},
                "debug": {},
            }
        features = self.extract_retrieval_features(
            requirement,
            aadl_context,
            target_component,
            model_analysis,
            diagnostic_context=diagnostic_context,
        )
        retrieval_queries = self.build_retrieval_queries(features, queries, agent_name, diagnostic_context=diagnostic_context)
        raw_candidates = self.retrieve_candidates(retrieval_queries)
        reranked = self.rerank_candidates(raw_candidates, features, agent_name)
        if agent_name == "requirement_analyst":
            # Requirement analysis should be grounded by requirement-to-expression
            # examples and light syntax reminders. Repair/defensive cards belong
            # to generation and validation repair; feeding them here shifts the
            # task toward error avoidance instead of semantic formalization.
            selected = {
                "Ksyn": [item.card for item in self._select_unique(reranked.get("Ksyn", []), min(2, self.ksyn_count))],
                "Kexp": [
                    item.card
                    for item in self._select_kexp_for_features(
                        reranked.get("Kexp", []),
                        features,
                        min(2, self.kexp_count),
                    )
                ],
                "Kdef": [],
            }
        else:
            selected = {
                "Ksyn": [item.card for item in self._select_unique(reranked.get("Ksyn", []), self.ksyn_count)],
                "Kexp": [item.card for item in self._select_kexp_for_features(reranked.get("Kexp", []), features, self.kexp_count)],
                "Kdef": [item.card for item in self._select_unique(reranked.get("Kdef", []), self.kdef_count)],
            }
            while len(selected["Kdef"]) < min(self.kdef_count, len(KDEF_HARD_CARDS)):
                selected["Kdef"].append(KDEF_HARD_CARDS[len(selected["Kdef"])])
        context = self.format_bundle(selected, features=features)
        metadata = {
            key: [{"id": card.card_id, "source": card.source, "topic": card.topic} for card in cards]
            for key, cards in selected.items()
        }
        debug = {
            "retrieval_config": {
                "mode": self.retrieval_mode,
                "embedding_model": self.embedding_model_name,
                "chunk_size": self.chunk_size,
                "chunk_overlap": self.chunk_overlap,
                "selected_counts": {"Ksyn": self.ksyn_count, "Kexp": self.kexp_count, "Kdef": self.kdef_count},
                "embedding_error": self._embedding_error or "",
            },
            "retrieval_features": features.to_dict(),
            "retrieval_queries": [query.to_dict() for query in retrieval_queries],
            "retrieved_candidates_raw": [
                self._scored_card_to_dict(item, include_body=False)
                for group in raw_candidates.values()
                for item in group
            ],
            "reranked_candidates": [
                self._scored_card_to_dict(item, include_body=False)
                for group in reranked.values()
                for item in group
            ],
            "compressed_rag_cards": context,
        }
        return {"context": context, "metadata": metadata, "debug": debug}

    def selected_metadata(self, queries: Dict[str, str], enabled: bool) -> Dict[str, List[Dict[str, str]]]:
        if not enabled:
            return {"Ksyn": [], "Kexp": [], "Kdef": []}
        selected = {
            "Ksyn": self._select("Ksyn", queries.get("Ksyn", ""), self.ksyn_count),
            "Kexp": self._select("Kexp", queries.get("Kexp", ""), self.kexp_count),
            "Kdef": self._select("Kdef", queries.get("Kdef", ""), self.kdef_count),
        }
        return {
            key: [{"id": card.card_id, "source": card.source, "topic": card.topic} for card in cards]
            for key, cards in selected.items()
        }

    def format_bundle(self, selected: Dict[str, List[RagCard]], features: RetrievalFeatures | None = None) -> str:
        def fmt_ksyn(card: RagCard, index: int) -> str:
            return (
                f"[KSYN-{index}]\n"
                f"Source: {card.source}\n"
                f"Topic: {card.topic}\n"
                f"{_truncate(card.body, 1200)}"
            )

        def fmt_kexp(card: RagCard, index: int) -> str:
            return (
                f"[KEXP-{index}]\n"
                f"Source: {card.source}\n"
                f"Topic: {card.topic}\n"
                f"{_truncate(card.body, 1200)}"
            )

        def fmt_kdef(card: RagCard, index: int) -> str:
            return (
                f"[KDEF-{index}]\n"
                f"Source: {card.source}\n"
                f"Topic: {card.topic}\n"
                f"{_truncate(card.body, 1200)}"
            )

        return "\n\n".join(
            [
                "<RAG_CONTEXT>",
                "<KSYN_CARDS>",
                "\n\n".join(fmt_ksyn(card, i + 1) for i, card in enumerate(selected["Ksyn"])),
                "</KSYN_CARDS>",
                "<KEXP_CARDS>",
                "\n\n".join(fmt_kexp(card, i + 1) for i, card in enumerate(selected["Kexp"])),
                "</KEXP_CARDS>",
                "<KDEF_CARDS>",
                "\n\n".join(fmt_kdef(card, i + 1) for i, card in enumerate(selected["Kdef"])),
                "</KDEF_CARDS>",
                "</RAG_CONTEXT>",
            ]
        )

    def _select(self, kind: str, query: str, count: int) -> List[RagCard]:
        candidates = self.cards.get(kind, [])
        if not candidates:
            return []
        query_terms = _tokenize(query)
        scored = []
        for card in candidates:
            haystack = _tokenize(f"{card.topic} {card.body} {card.source}")
            scored.append((len(query_terms & haystack), card.card_id, card))
        scored.sort(key=lambda item: (-item[0], item[1]))
        return [item[2] for item in scored[:count]]

    def extract_retrieval_features(
        self,
        requirement: str,
        aadl_context: str,
        target_component: str | None,
        model_analysis: Any = None,
        diagnostic_context: str = "",
    ) -> RetrievalFeatures:
        text = f"{requirement or ''}\n{diagnostic_context or ''}".lower()
        target = target_component or self._infer_target_component_from_text(requirement, aadl_context)
        target_scope = "component_implementation" if ".impl" in target.lower() or "implementation layer" in text else "component_type"
        if target and re.search(rf"\bsubprogram\s+{re.escape(target.split('.')[0])}\b", aadl_context or "", re.IGNORECASE):
            target_scope = "subprogram"
        visible_inputs, visible_outputs = self._extract_visible_ports(aadl_context, target)
        visible_inputs = self._prioritize_by_requirement(visible_inputs, requirement)
        visible_outputs = self._prioritize_by_requirement(visible_outputs, requirement)
        model_ids = self._identifiers_from_model_analysis(model_analysis)
        relevant = self._extract_relevant_identifiers(requirement, visible_inputs + visible_outputs + model_ids)
        patterns: List[str] = []
        features: List[str] = []
        operators: List[str] = []
        avoid: List[str] = []

        has_branch = bool(re.search(r"\b(if|when|whenever|otherwise|else|case|provided that)\b", text))
        has_comparison = bool(
            re.search(
                r"\b(equal|equals|higher|lower|greater|less|above|below|exceed|exceeds|threshold|strictly)\b",
                text,
            )
            or any(op in requirement for op in (">=", "<=", ">", "<", "="))
        )
        visible_output_in_requirement = any(output.lower() in text for output in visible_outputs)
        has_output_intent = bool(
            re.search(r"\b(set|assign|output|required|command|emit|produce|return)\b", text)
            or "value should" in text
            or "speed should" in text
            or visible_output_in_requirement
        )

        if has_branch:
            patterns.append("conditional_assignment")
            features.append("if_then_else")
            operators.append("if then else")
        if has_comparison:
            features.append("comparison")
            operators.extend([">", "<"])
        if has_output_intent:
            patterns.append("output_assignment")
            features.append("equality")
            operators.append("=")
        if _has_any_word(text, ("previous", "pre", "last", "history", "prior", "past")) or "pre(" in text:
            patterns.append("temporal_history")
            features.append("previous_value")
            operators.append("pre")
        else:
            avoid.append("history_pre")
        if any(w in text for w in ("range", "between", "within", "at least", "at most", "minimum", "maximum")) or has_comparison:
            patterns.append("range_constraint")
            features.extend(["threshold", "comparison"])
            operators.extend([">=", "<="])
        else:
            avoid.append("range_only")
        if _has_any_word(text, ("and", "or", "not", "boolean", "bool", "flag")):
            patterns.append("boolean_logic")
            features.append("boolean_logic")
            operators.extend(["and", "or", "not"])
        if any(w in text for w in ("integer", "boolean", "couldn't resolve reference", "type mismatch", "actual type", "assumed type")):
            features.extend(["type_name", "type_mismatch", "unresolved_reference"])
            operators.extend(["int", "bool", "real"])
        if any(w in text for w in ("recursive", "step", "time step", "recurrence")):
            patterns.append("arithmetic_constraint")
            features.extend(["arithmetic", "previous_value"])
            operators.extend(["pre", "+"])
        if "=>" in requirement or "implies" in text:
            patterns.append("implication")
            operators.append("=>")

        if not patterns:
            patterns.append("equality_constraint")
        source_priority = self._source_priority_for_features(patterns, target_scope)
        return RetrievalFeatures(
            target_scope=target_scope or "unknown",
            target_component=target,
            visible_inputs=_ordered(visible_inputs),
            visible_outputs=_ordered(visible_outputs),
            visible_variables=[],
            contract_patterns=_ordered(patterns),
            logic_features=_ordered(features),
            relevant_identifiers=_ordered(relevant),
            required_operators=_ordered(operators),
            avoid_patterns=_ordered(avoid),
            source_priority=source_priority,
        )

    def build_retrieval_queries(
        self,
        features: RetrievalFeatures,
        base_queries: Dict[str, str],
        agent_name: str,
        diagnostic_context: str = "",
    ) -> List[RetrievalQuery]:
        queries: List[RetrievalQuery] = []
        pattern_terms = " ".join(features.contract_patterns + features.logic_features + features.required_operators)
        if pattern_terms:
            queries.append(RetrievalQuery(f"AGREE {pattern_terms} contract pattern", "Kexp", "pattern"))
        if features.target_scope:
            queries.append(RetrievalQuery(f"AGREE annex {features.target_scope} visible input output ports local variable", "Ksyn", "scope"))
            queries.append(RetrievalQuery(f"AGREE {features.target_scope} scope naming structural binding", "Kdef", "scope"))
        if features.relevant_identifiers:
            queries.append(RetrievalQuery(" ".join(features.relevant_identifiers), None, "identifier"))
        if agent_name == "validation_repair":
            queries.append(RetrievalQuery("AGREE validation error malformed annex unresolved reference type mismatch repair", "Kdef", "syntax"))
            diagnostic_query = self._diagnostic_query(diagnostic_context)
            if diagnostic_query:
                queries.append(RetrievalQuery(diagnostic_query, "Kdef", "validator_diagnostics"))
                queries.append(RetrievalQuery(diagnostic_query, "Ksyn", "validator_diagnostics"))
                queries.append(RetrievalQuery(diagnostic_query, "Kexp", "validator_diagnostics"))
        else:
            queries.append(RetrievalQuery("AGREE guarantee syntax assume eq const assign if then else", "Ksyn", "syntax"))
        for source, query in base_queries.items():
            if query:
                queries.append(RetrievalQuery(query, source, "base_agent_query"))
        return queries

    def _diagnostic_query(self, diagnostic_context: str, limit: int = 1200) -> str:
        text = re.sub(r"\s+", " ", diagnostic_context or "").strip()
        if not text:
            return ""
        phrases = []
        patterns = [
            r"Couldn't resolve reference to '[^']+'",
            r"Couldn't resolve reference to [A-Za-z_][A-Za-z0-9_:'.]*",
            r"The assumed type of [^.]+",
            r"actual type is '[^']+'",
            r"named thing must be an expression with a type",
            r"must be of type '[^']+'",
            r"left and right sides of binary expression '[^']+'",
            r"Expression for guarantee statement is of type '[^']+'",
            r"Package [^.] +has duplicates",
        ]
        for pattern in patterns:
            phrases.extend(match.group(0) for match in re.finditer(pattern, text, flags=re.IGNORECASE))
        if not phrases:
            phrases.append(text[:limit])
        return "AGREE validator diagnostic repair " + " ".join(_ordered(phrases))[:limit]

    def retrieve_candidates(self, retrieval_queries: List[RetrievalQuery]) -> Dict[str, List[ScoredCard]]:
        grouped: Dict[str, List[ScoredCard]] = {"Ksyn": [], "Kexp": [], "Kdef": []}
        retrieval_cards = self._retrieval_cards_by_kind()
        vector_scores = self._vector_scores(retrieval_queries)
        for kind, cards in retrieval_cards.items():
            for card in cards:
                best_score = 0
                best_query = ""
                for query in retrieval_queries:
                    if query.source and query.source != kind:
                        continue
                    score = len(_tokenize(query.query) & _tokenize(f"{card.topic} {card.body} {card.source}"))
                    if score > best_score:
                        best_score = score
                        best_query = query.query
                vector_score = vector_scores.get(card.card_id, 0.0)
                if self.retrieval_mode == "embedding":
                    combined_score = vector_score * 10.0
                elif self.retrieval_mode == "lexical":
                    combined_score = float(best_score)
                else:
                    combined_score = float(best_score) + vector_score * 10.0
                grouped.setdefault(kind, []).append(
                    ScoredCard(
                        card=card,
                        score=combined_score,
                        details={
                            "lexical_score": best_score,
                            "embedding_score": round(vector_score, 6),
                            "best_query": best_query,
                            "retrieval_mode": self.retrieval_mode,
                            "embedding_error": self._embedding_error or "",
                        },
                    )
                )
        return grouped

    def rerank_candidates(
        self,
        candidates: Dict[str, List[ScoredCard]],
        features: RetrievalFeatures,
        agent_name: str,
    ) -> Dict[str, List[ScoredCard]]:
        reranked: Dict[str, List[ScoredCard]] = {}
        for kind, items in candidates.items():
            scored = []
            for item in items:
                scored.append(self._score_candidate(item.card, item.score, features, agent_name))
            scored.sort(key=lambda item: (-item.score, item.card.card_id))
            reranked[kind] = self._dedupe_scored(scored)
        return reranked

    def _select_kexp_for_features(self, items: List[ScoredCard], features: RetrievalFeatures, limit: int) -> List[ScoredCard]:
        """Select KEXP cards with pattern diversity and current-case grounding."""
        if limit <= 0:
            return []
        selected: List[ScoredCard] = []
        used_sources: set[str] = set()
        used_primary: set[str] = set()
        used_fingerprints: set[str] = set()
        wanted_patterns = [
            pattern
            for pattern in (
                "temporal_history",
                "conditional_assignment",
                "output_assignment",
                "range_constraint",
                "boolean_logic",
                "arithmetic_constraint",
                "implication",
            )
            if pattern in features.contract_patterns or pattern in features.logic_features
        ]

        def add_best_for(pattern: str) -> None:
            for item in items:
                tags = _infer_card_tags(item.card)
                if pattern not in tags or item in selected:
                    continue
                if self._card_is_unsafe_for_features(tags, features):
                    continue
                fingerprint = self._card_fingerprint(item.card)
                if self._dedupe_key(item.card) in used_sources or fingerprint in used_fingerprints:
                    continue
                selected.append(item)
                used_sources.add(self._dedupe_key(item.card))
                used_primary.add(pattern)
                used_fingerprints.add(fingerprint)
                return

        for item in items:
            if len(selected) >= min(2, limit):
                break
            if item.card.source != "distilled pattern library":
                continue
            tags = _infer_card_tags(item.card)
            if self._card_is_unsafe_for_features(tags, features):
                continue
            primary = self._effective_primary_tag(tags, features)
            fingerprint = self._card_fingerprint(item.card)
            if self._dedupe_key(item.card) in used_sources or fingerprint in used_fingerprints or (primary in used_primary and len(selected) < limit - 1):
                continue
            selected.append(item)
            used_sources.add(self._dedupe_key(item.card))
            used_primary.add(primary)
            used_fingerprints.add(fingerprint)

        for pattern in wanted_patterns:
            add_best_for(pattern)
            if len(selected) >= limit:
                return selected

        for item in items:
            if item in selected:
                continue
            tags = _infer_card_tags(item.card)
            if self._card_is_unsafe_for_features(tags, features):
                continue
            primary = self._effective_primary_tag(tags, features)
            fingerprint = self._card_fingerprint(item.card)
            if self._dedupe_key(item.card) in used_sources or fingerprint in used_fingerprints:
                continue
            duplicate_primary = primary in used_primary
            if duplicate_primary and len(selected) < limit - 1:
                continue
            selected.append(item)
            used_sources.add(self._dedupe_key(item.card))
            used_primary.add(primary)
            used_fingerprints.add(fingerprint)
            if len(selected) >= limit:
                break
        return selected

    def _select_unique(self, items: List[ScoredCard], limit: int) -> List[ScoredCard]:
        selected: List[ScoredCard] = []
        seen: set[str] = set()
        for item in items:
            key = f"{self._dedupe_key(item.card)}|{self._card_fingerprint(item.card)}"
            if key in seen:
                continue
            seen.add(key)
            selected.append(item)
            if len(selected) >= limit:
                break
        return selected

    def _dedupe_scored(self, items: List[ScoredCard]) -> List[ScoredCard]:
        deduped: List[ScoredCard] = []
        seen: set[str] = set()
        for item in items:
            key = f"{self._dedupe_key(item.card)}|{self._card_fingerprint(item.card)}"
            if key in seen:
                continue
            seen.add(key)
            deduped.append(item)
        return deduped

    def _dedupe_key(self, card: RagCard) -> str:
        return str(card.metadata.get("parent_id") or card.card_id)

    def _card_fingerprint(self, card: RagCard) -> str:
        text = re.sub(r"\s+", " ", f"{card.kind} {card.source} {card.topic} {card.body}".lower()).strip()
        return text[:360]

    def _card_is_unsafe_for_features(self, tags: set[str], features: RetrievalFeatures) -> bool:
        # Do not feed implementation-only assignment patterns to component type generation.
        if "component_implementation" in tags and features.target_scope != "component_implementation" and "component_type" not in tags:
            return True
        target_text = f"{features.target_scope} {features.target_component}".lower()
        if "subprogram" in target_text:
            target_is_subprogram = True
        else:
            target_is_subprogram = False
        if not target_is_subprogram and "subprogram" in " ".join(sorted(tags)).lower():
            return True
        if "history_pre" in tags and "temporal_history" not in features.contract_patterns:
            return True
        if "range_only" in tags and "range_constraint" not in features.contract_patterns:
            return True
        if "output_assignment" in tags and not features.visible_outputs:
            return True
        return False

    def _retrieval_cards_by_kind(self) -> Dict[str, List[RagCard]]:
        """Return chunked cards for retrieval while preserving parent metadata for de-duplication."""
        if self._retrieval_cards is not None:
            return self._retrieval_cards
        chunked: Dict[str, List[RagCard]] = {"Ksyn": [], "Kexp": [], "Kdef": []}
        for kind, cards in self.cards.items():
            for card in cards:
                chunked[kind].extend(self._chunk_card(card))
        self._retrieval_cards = chunked
        return chunked

    def _chunk_card(self, card: RagCard) -> List[RagCard]:
        text = card.body or ""
        if len(text) <= self.chunk_size:
            metadata = dict(card.metadata)
            metadata.setdefault("parent_id", card.card_id)
            return [RagCard(card.kind, card.card_id, card.source, card.topic, card.body, metadata)]

        chunks: List[RagCard] = []
        step = max(1, self.chunk_size - max(0, self.chunk_overlap))
        for index, start in enumerate(range(0, len(text), step), 1):
            chunk = text[start : start + self.chunk_size].strip()
            if not chunk:
                continue
            metadata = dict(card.metadata)
            metadata["parent_id"] = card.card_id
            metadata["chunk_index"] = str(index)
            chunks.append(
                RagCard(
                    card.kind,
                    f"{card.card_id}.chunk{index}",
                    card.source,
                    f"{card.topic} chunk {index}",
                    chunk,
                    metadata,
                )
            )
            if start + self.chunk_size >= len(text):
                break
        return chunks or [card]

    def _vector_scores(self, retrieval_queries: List[RetrievalQuery]) -> Dict[str, float]:
        """Embedding recall scores. Falls back silently to lexical-only when embeddings are unavailable."""
        if self.retrieval_mode == "lexical":
            return {}
        cards = [card for group in self._retrieval_cards_by_kind().values() for card in group]
        if not cards:
            return {}
        queries = [query.query for query in retrieval_queries if query.query]
        if not queries:
            return {}
        matrix = self._ensure_embedding_matrix(cards)
        if matrix is None:
            return {}
        try:
            import numpy as np

            query_vectors = self._embedding_model.encode(queries, normalize_embeddings=True, show_progress_bar=False)
            scores = np.asarray(query_vectors) @ matrix.T
            best = scores.max(axis=0)
            return {card.card_id: float(score) for card, score in zip(cards, best)}
        except Exception as exc:
            self._embedding_error = f"{type(exc).__name__}: {exc}"
            return {}

    def _ensure_embedding_matrix(self, cards: List[RagCard]):
        if self._embedding_matrix is not None and self._embedding_cards is not None:
            return self._embedding_matrix
        try:
            from sentence_transformers import SentenceTransformer

            if self._embedding_model is None:
                self._embedding_model = SentenceTransformer(self.embedding_model_name)
            texts = [self._embedding_text(card) for card in cards]
            self._embedding_matrix = self._embedding_model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
            self._embedding_cards = cards
            self._embedding_error = None
            return self._embedding_matrix
        except Exception as exc:
            self._embedding_error = f"{type(exc).__name__}: {exc}"
            return None

    def _embedding_text(self, card: RagCard) -> str:
        tags = card.metadata.get("tags", "")
        return f"{card.kind}\nSource: {card.source}\nTopic: {card.topic}\nTags: {tags}\n{card.body}"

    def _score_candidate(self, card: RagCard, lexical_score: float, features: RetrievalFeatures, agent_name: str) -> ScoredCard:
        tags = _infer_card_tags(card)
        haystack = f"{card.topic} {card.body} {card.source}".lower()
        pattern_hits = sorted(set(features.contract_patterns) & tags)
        logic_hits = sorted(set(features.logic_features) & tags)
        avoid_hits = sorted(set(features.avoid_patterns) & tags)
        identifier_hits = [identifier for identifier in features.relevant_identifiers if identifier.lower() in haystack]
        visible_output_hits = [identifier for identifier in features.visible_outputs if identifier.lower() in haystack]
        visible_input_hits = [identifier for identifier in features.visible_inputs if identifier.lower() in haystack]
        operator_hits = [operator for operator in features.required_operators if operator.lower() in haystack]
        score = lexical_score
        score += 3 * len(pattern_hits)
        score += 2 * len(logic_hits)
        score += 2 * len(visible_output_hits)
        score += 1 * len(visible_input_hits)
        score += 1.5 * len(operator_hits)
        if features.target_scope in tags:
            score += 2
        if card.kind in features.source_priority:
            score += max(0, 3 - features.source_priority.index(card.kind))
        if card.source == "distilled pattern library":
            score += 4
            if "subprogram" in card.topic.lower() and features.target_scope == "component_type":
                score += 3
            if "implementation" in card.topic.lower() and features.target_scope == "component_implementation":
                score += 3
            if "range" in card.topic.lower() and "range_constraint" in features.contract_patterns:
                score += 2
            if "history" in card.topic.lower() and "temporal_history" in features.contract_patterns:
                score += 2
        if "conditional_assignment" in features.contract_patterns and "conditional_assignment" not in tags:
            score -= 6
        if "output_assignment" in features.contract_patterns and "output_assignment" not in tags:
            score -= 4
        score -= 5 * len(avoid_hits)
        if "range_only" in tags and "conditional_assignment" in features.contract_patterns:
            score -= 5
        if "history_pre" in tags and "temporal_history" not in features.contract_patterns:
            score -= 6
        if card.kind == "Kexp" and "valid_annex_delimiter" in tags:
            score += 1
        if agent_name == "validation_repair" and card.kind == "Kdef":
            repair_terms = {
                "type_name",
                "type_mismatch",
                "unresolved_reference",
                "named_thing_no_type",
                "validator_error_pattern",
            }
            score += 5 * len(repair_terms & tags)
        details = {
            "lexical_score": lexical_score,
            "tags": sorted(tags),
            "pattern_hits": pattern_hits,
            "logic_hits": logic_hits,
            "operator_hits": operator_hits,
            "identifier_hits": identifier_hits,
            "visible_input_hits": visible_input_hits,
            "visible_output_hits": visible_output_hits,
            "avoid_hits": avoid_hits,
            "agent_name": agent_name,
        }
        return ScoredCard(card=card, score=score, details=details)

    def _select_diverse(self, items: List[ScoredCard], limit: int) -> List[ScoredCard]:
        if limit <= 0:
            return []
        selected: List[ScoredCard] = []
        used_primary_tags: set[str] = set()
        for item in items:
            tags = _infer_card_tags(item.card)
            primary = self._effective_primary_tag(tags, features)
            if primary not in used_primary_tags:
                selected.append(item)
                used_primary_tags.add(primary)
            if len(selected) >= limit:
                return selected
        for item in items:
            if item not in selected:
                selected.append(item)
            if len(selected) >= limit:
                break
        return selected

    def _primary_tag(self, tags: set[str]) -> str:
        for tag in ("conditional_assignment", "output_assignment", "temporal_history", "range_constraint", "boolean_logic", "component_implementation"):
            if tag in tags:
                return tag
        return sorted(tags)[0] if tags else "untagged"

    def _effective_primary_tag(self, tags: set[str], features: RetrievalFeatures) -> str:
        if "conditional_assignment" in features.contract_patterns and "conditional_assignment" in tags:
            return "conditional_assignment"
        if "temporal_history" in features.contract_patterns and "temporal_history" in tags:
            return "temporal_history"
        if "range_constraint" in features.contract_patterns and "range_constraint" in tags and "output_assignment" not in tags:
            return "range_constraint"
        if "output_assignment" in features.contract_patterns and "output_assignment" in tags and "range_constraint" not in tags:
            return "output_assignment"
        if "boolean_logic" in features.contract_patterns and "boolean_logic" in tags:
            return "boolean_logic"
        if "range_constraint" in features.contract_patterns and "range_constraint" in tags:
            return "range_constraint"
        if "output_assignment" in features.contract_patterns and "output_assignment" in tags:
            return "output_assignment"
        return self._primary_tag(tags)

    def _load_ksyn_cards(self) -> List[RagCard]:
        files = list((self.root / "processed" / "ksyn").glob("*.md")) + list((self.root / "raw" / "ksyn").glob("*.md"))
        cards = []
        for path in sorted(files):
            text = path.read_text(encoding="utf-8", errors="replace")
            chunks = [chunk.strip() for chunk in re.split(r"\n\s*\n", text) if chunk.strip()]
            for idx, chunk in enumerate(chunks[:12], 1):
                cards.append(RagCard("Ksyn", f"ksyn.{path.stem}.{idx}", str(path.relative_to(self.root)), path.stem, _truncate(chunk), {}))
        if not cards:
            cards.append(RagCard("Ksyn", "ksyn.fallback.1", "fallback", "AGREE syntax", "Use legal AGREE annex syntax and current-case identifiers only.", {}))
        return cards

    def _load_kexp_cards(self) -> List[RagCard]:
        cards: List[RagCard] = []
        for path in sorted((self.root / "processed" / "kexp").glob("*.jsonl")):
            cards.extend(self._load_jsonl_examples(path))
        for path in sorted((self.root / "processed" / "kexp").glob("*.txt")):
            cards.extend(self._load_text_examples(path))
        cards.extend(self._synthetic_pattern_cards())
        if not cards:
            cards.append(RagCard("Kexp", "kexp.fallback.1", "fallback", "example", "guarantee \"example\": true;", {},))
        return cards

    def _synthetic_pattern_cards(self) -> List[RagCard]:
        """Small distilled cards that prevent long examples from dominating retrieval."""
        specs = [
            (
                "kexp.pattern.type_range_assumption_guarantee",
                "type scope range assumption and guarantee",
                "For component type contracts, place input envelope assumptions and output range guarantees inside annex agree only when the case supplies concrete bounds, named constants, or a visible relation. Use case-provided thresholds and legal visible feature names.",
                {"component_type", "range_constraint", "comparison", "equality", "output_assignment", "valid_annex_delimiter"},
            ),
            (
                "kexp.pattern.type_dependency_guarantee",
                "type scope deterministic dependency guarantee",
                "For output dependency contracts, write a guarantee that relates visible outputs to visible inputs. Do not use implementation-only subcomponent paths in a component type annex.",
                {"component_type", "output_assignment", "boolean_logic", "comparison", "equality", "valid_annex_delimiter"},
            ),
            (
                "kexp.pattern.impl_assign_output",
                "implementation scope output assign",
                "For implementation contracts, use assign only when the left-hand side is an existing output feature or declared auxiliary variable. Do not place guarantee statements in implementation scope.",
                {"component_implementation", "output_assignment", "conditional_assignment", "if_then_else", "equality", "valid_annex_delimiter"},
            ),
            (
                "kexp.pattern.history_initialized",
                "initialized history comparison",
                "For pre() expressions, declare an initialized state such as initialized : bool = false -> true and guard previous-value comparisons on initialized.",
                {"component_type", "temporal_history", "history_pre", "comparison", "equality", "valid_annex_delimiter"},
            ),
            (
                "kexp.pattern.recurrence_eq",
                "recursive state equation",
                "For recursive variables, define an initialized eq expression with -> and pre(x), then relate visible outputs to that state with a separate guarantee or assign.",
                {"component_type", "temporal_history", "history_pre", "arithmetic_constraint", "equality", "valid_annex_delimiter"},
            ),
            (
                "kexp.pattern.subprogram_parameters",
                "subprogram parameter contract",
                "Subprogram features may be in/out parameters rather than ports. Treat visible parameters like legal AGREE identifiers in the owning subprogram scope.",
                {"subprogram", "component_type", "range_constraint", "output_assignment", "comparison", "equality", "valid_annex_delimiter"},
            ),
        ]
        return [
            RagCard(
                "Kexp",
                card_id,
                "distilled pattern library",
                topic,
                body,
                {"tags": ",".join(sorted(tags)), "pattern_type": self._primary_tag(tags)},
            )
            for card_id, topic, body, tags in specs
        ]

    def _load_kdef_cards(self) -> List[RagCard]:
        cards = list(KDEF_HARD_CARDS)
        for path in sorted((self.root / "processed" / "kdef").glob("*.jsonl")):
            for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
                if not line.strip():
                    continue
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                title = str(item.get("title") or item.get("id") or "defensive rule")
                category = str(item.get("category") or "general")
                description = str(item.get("description") or "")
                recommended = str(item.get("recommended_pattern") or "")
                body = description if not recommended else f"{description} Recommended pattern: {recommended}"
                tags = self._tags_for_kdef(category, title, body)
                cards.append(
                    RagCard(
                        "Kdef",
                        str(item.get("id") or f"kdef.{path.stem}.{len(cards) + 1}"),
                        str(path.relative_to(self.root)),
                        title,
                        body,
                        {"category": category, "severity": "hard", "tags": ",".join(sorted(tags))},
                    )
                )
        return cards

    def _tags_for_kdef(self, category: str, title: str, body: str) -> set[str]:
        text = f"{category} {title} {body}".lower()
        tags = {"defensive_rule"}
        if "validator_error_pattern" in text or any(term in text for term in ("couldn't resolve reference", "diagnostic", "actual type", "assumed type", "named thing", "<error>")):
            tags.add("validator_error_pattern")
        if any(term in text for term in ("scope", "placement", "annex", "component")):
            tags.add("component_type")
            tags.add("component_implementation")
        if any(term in text for term in ("integer", "boolean", "int", "bool", "real", "scalar type")):
            tags.add("type_name")
        if any(term in text for term in ("assign", "declaration", "variable", "double definition")):
            tags.add("output_assignment")
        if any(term in text for term in ("unresolved", "reference", "modelunit", "package", "data type")):
            tags.add("unresolved_reference")
        if any(term in text for term in ("type mismatch", "actual type", "assumed type", "<error>")):
            tags.add("type_mismatch")
        if "named thing" in text:
            tags.add("named_thing_no_type")
        if any(term in text for term in ("pre", "recurrence", "state")):
            tags.add("temporal_history")
        if any(term in text for term in ("if", "conditional", "elsif")):
            tags.add("conditional_assignment")
        if any(term in text for term in ("range", "threshold", "constant")):
            tags.add("range_constraint")
        if any(term in text for term in ("and", "or", "not", "boolean")):
            tags.add("boolean_logic")
        if any(term in text for term in ("quote", "syntax", "operator", "ascii", "equality")):
            tags.add("syntax_rule")
        return tags

    def _load_jsonl_examples(self, path: Path) -> Iterable[RagCard]:
        loaded = []
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            body = _truncate(item.get("agree_code") or item.get("code_agree") or item.get("description") or "")
            loaded.append(
                RagCard(
                    "Kexp",
                    str(item.get("id") or f"kexp.{path.stem}.{len(loaded) + 1}"),
                    str(path.relative_to(self.root)),
                    str(item.get("description") or "AGREE example"),
                    body,
                    {
                        "requirement_nl": str(item.get("requirement_nl") or "unknown"),
                        "logic_prop": str(item.get("logic_prop") or "unknown"),
                        "tags": ",".join(sorted(self._tags_for_kexp(body, str(item.get("description") or "")))),
                    },
                )
            )
        return loaded

    def _load_text_examples(self, path: Path) -> Iterable[RagCard]:
        text = path.read_text(encoding="utf-8", errors="replace")
        chunks = self._split_kexp_packages(text)
        cards: List[RagCard] = []
        for idx, chunk in enumerate(chunks[:80], 1):
            topic = self._topic_for_kexp(chunk)
            tags = self._tags_for_kexp(chunk, topic)
            cards.append(
                RagCard(
                    "Kexp",
                    f"kexp.{path.stem}.{idx}",
                    str(path.relative_to(self.root)),
                    topic,
                    _truncate(chunk, 2400),
                    {"tags": ",".join(sorted(tags)), "pattern_type": self._primary_tag(tags)},
                )
            )
        return cards

    def _split_kexp_packages(self, text: str) -> List[str]:
        text = text.replace("\ufeff", "")
        starts = [match.start() for match in re.finditer(r"(?im)(?=^\s*package\s+[A-Za-z_][A-Za-z0-9_]*)", text)]
        if not starts:
            return [chunk.strip() for chunk in re.split(r"\n\s*\n", text) if chunk.strip()]
        chunks: List[str] = []
        starts.append(len(text))
        for index in range(len(starts) - 1):
            chunk = text[starts[index] : starts[index + 1]].strip()
            if chunk:
                chunks.append(chunk)
        return chunks

    def _topic_for_kexp(self, body: str) -> str:
        match = re.search(r"(?im)^\s*package\s+([A-Za-z_][A-Za-z0-9_]*)", body)
        name = match.group(1) if match else "AGREE example"
        cleaned = name.replace("agree_kexp_", "").replace("_", " ")
        return cleaned.strip() or name

    def _tags_for_kexp(self, body: str, topic: str = "") -> set[str]:
        text = f"{topic} {body}".lower()
        tags = {"valid_annex_delimiter"} if "annex agree {**" in text else set()
        if any(term in text for term in ("if ", " then ", " else ", "conditional", "selection", "selector", "chosen", "clamped")):
            tags.update({"conditional_assignment", "if_then_else"})
        if any(term in text for term in ("out data port", "output", "assign ", "flag follows", "mirrors", "selected output")):
            tags.add("output_assignment")
        if any(term in text for term in ("pre(", "history", "previous", "recurrence", "counter", "mode transition", "nondecreasing")):
            tags.update({"temporal_history", "history_pre"})
        if any(term in text for term in ("range", "within", "lower_limit", "upper_limit", "bounded", "envelope", "threshold", "min_", "max_")):
            tags.add("range_constraint")
        if any(term in text for term in (" and ", " or ", " not ", "boolean", "two_conditions")):
            tags.add("boolean_logic")
        if any(term in text for term in ("=>", "implies", "implication")):
            tags.add("implication")
        if any(term in text for term in ("system implementation", ".impl", " assign ")):
            tags.add("component_implementation")
        if "subprogram" in text:
            tags.add("subprogram")
        if "annex agree" in text or re.search(r"(?im)^\s*system\s+[A-Za-z_][A-Za-z0-9_]*\s+features", body):
            tags.add("component_type")
        if any(term in text for term in (">=", "<=", ">", "<", "difference", "comparison")):
            tags.add("comparison")
        if "=" in text:
            tags.add("equality")
        if any(term in text for term in ("+", "-", "*", "/", "arithmetic", "counter", "difference")):
            tags.add("arithmetic_constraint")
        if "range_constraint" in tags and not ({"conditional_assignment", "output_assignment", "temporal_history"} & tags):
            tags.add("range_only")
        return tags

    def _compress_kexp_card(self, card: RagCard, index: int, features: RetrievalFeatures) -> str:
        tags = _infer_card_tags(card)
        effective_tags = set(tags)
        if "conditional_assignment" not in features.contract_patterns:
            effective_tags.discard("conditional_assignment")
            effective_tags.discard("if_then_else")
        if "temporal_history" not in features.contract_patterns:
            effective_tags.discard("temporal_history")
            effective_tags.discard("history_pre")
        if "range_constraint" not in features.contract_patterns:
            effective_tags.discard("range_constraint")
            effective_tags.discard("range_only")
        if "boolean_logic" not in features.contract_patterns:
            effective_tags.discard("boolean_logic")
        if not effective_tags:
            effective_tags = tags
        pattern = self._describe_pattern(effective_tags)
        skeleton = self._skeleton_for_tags(effective_tags, features)
        applicable = self._applicability_for_tags(effective_tags)
        current_notes = [
            f"Target scope: {features.target_scope}",
            f"Target component: {features.target_component or 'unknown'}",
        ]
        if features.target_scope == "component_implementation":
            current_notes.append("For implementation-level output behavior, prefer assign statements or implementation-local equations instead of implementation-level guarantees.")
        if features.visible_outputs:
            current_notes.append(f"Visible output candidates: {', '.join(features.visible_outputs)}")
        elif "output_assignment" in tags:
            current_notes.append("No visible output was identified for the target scope; do not invent an output name or use this as an assignment template.")
        if features.visible_inputs:
            current_notes.append(f"Visible input candidates: {', '.join(features.visible_inputs)}")
        return (
            f"[KEXP-{index}]\n"
            f"Pattern: {pattern}\n"
            f"Use when: {self._inline_lines(applicable)}\n"
            "Skeleton:\n"
            f"{skeleton}\n"
            "Current case: "
            + "; ".join(current_notes)
            + "\nDo not copy example names, constants, component names, or scenario details."
        )

    def _inline_lines(self, text: str) -> str:
        return "; ".join(line.strip("- ").strip() for line in text.splitlines() if line.strip())

    def _describe_pattern(self, tags: set[str]) -> str:
        if "conditional_assignment" in tags and "output_assignment" in tags:
            return "conditional output assignment"
        if "temporal_history" in tags:
            return "history or previous-value comparison"
        if "range_constraint" in tags:
            return "range or threshold constraint"
        if "boolean_logic" in tags:
            return "boolean decision logic"
        if "component_implementation" in tags:
            return "component implementation placement"
        return "general AGREE contract pattern"

    def _applicability_for_tags(self, tags: set[str]) -> str:
        lines = []
        if "conditional_assignment" in tags:
            lines.append("- The requirement assigns different values under different conditions.")
        if "output_assignment" in tags:
            lines.append("- The target output is visible in the current AGREE scope.")
        if "temporal_history" in tags:
            lines.append("- The requirement explicitly depends on previous, prior, or historical values.")
        if "range_constraint" in tags:
            lines.append("- The requirement constrains a value to remain within a numeric bound or threshold.")
        if not lines:
            lines.append("- The contract pattern matches the current requirement and component scope.")
        return "\n".join(lines)

    def _skeleton_for_tags(self, tags: set[str], features: RetrievalFeatures) -> str:
        output = features.visible_outputs[0] if features.visible_outputs else "<output>"
        inputs = features.visible_inputs[:2]
        lhs = inputs[0] if inputs else "<input_a>"
        rhs = inputs[1] if len(inputs) > 1 else "<input_b>"
        if "conditional_assignment" in tags and "output_assignment" in tags:
            if not features.visible_outputs:
                return (
                    "No safe assignment skeleton is provided because the target scope has no visible output candidates.\n"
                    "First identify a legal current-case output or downgrade this example to a conceptual pattern only."
                )
            if features.target_scope == "component_implementation":
                return (
                    f"assign {output} =\n"
                    f"  if <condition using {lhs} and {rhs}> then <value1>\n"
                    "  else <value2>;\n"
                    "eq <local_condition_name> : bool = <condition using visible inputs>;"
                )
            return (
                "guarantee \"<name>\":\n"
                f"  if <condition using {lhs} and {rhs}> then {output} = <value1>\n"
                f"  else {output} = <value2>;"
            )
        if "temporal_history" in tags:
            return (
                "eq initialized : bool = false -> true;\n"
                "guarantee \"<name>\":\n"
                "  initialized => <value> >= pre(<value>);"
            )
        if "range_constraint" in tags:
            return (
                "const provided_min : <type> = <case_supplied_min>;\n"
                "const provided_max : <type> = <case_supplied_max>;\n"
                "guarantee \"<name>\": <value> >= provided_min and <value> <= provided_max;"
            )
        if "boolean_logic" in tags:
            return "guarantee \"<name>\": <output_bool> = (<condition_a> and <condition_b>);"
        return "guarantee \"<name>\": <expression over visible current-case identifiers>;"

    def _infer_target_component_from_text(self, requirement: str, aadl_context: str) -> str:
        req = requirement or ""
        for match in re.finditer(r"\b([A-Z][A-Za-z0-9_]*(?:\.impl)?)\b", req):
            name = match.group(1)
            if re.search(rf"\b(system|process|thread)\s+{re.escape(name.split('.')[0])}\b", aadl_context or "", re.IGNORECASE):
                return name
        match = re.search(r"^\s*system\s+([A-Za-z_][A-Za-z0-9_]*)", aadl_context or "", re.MULTILINE)
        return match.group(1) if match else ""

    def _extract_visible_ports(self, aadl_context: str, target_component: str) -> tuple[List[str], List[str]]:
        component = (target_component or "").split(".")[0]
        block = aadl_context or ""
        if component:
            match = re.search(
                rf"\b(?:system|process|thread|device|abstract|subprogram)\s+{re.escape(component)}\b(.*?)(?:^\s*end\s+{re.escape(component)}\s*;)",
                aadl_context or "",
                flags=re.IGNORECASE | re.DOTALL | re.MULTILINE,
            )
            if match:
                block = match.group(1)
        inputs: List[str] = []
        outputs: List[str] = []
        port_pattern = re.compile(
            r"\b([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(in|out)\s+(?:(?:event\s+data|event|data)\s+port|parameter)\b",
            flags=re.IGNORECASE,
        )
        for name, direction in port_pattern.findall(block):
            if direction.lower() == "in":
                inputs.append(name)
            else:
                outputs.append(name)
        return inputs, outputs

    def _prioritize_by_requirement(self, identifiers: List[str], requirement: str) -> List[str]:
        req = (requirement or "").lower()
        return sorted(
            _ordered(identifiers),
            key=lambda item: (0 if item.lower() in req else 1, req.find(item.lower()) if item.lower() in req else 10_000, item.lower()),
        )

    def _identifiers_from_model_analysis(self, model_analysis: Any) -> List[str]:
        if not isinstance(model_analysis, dict):
            return []
        whitelist = model_analysis.get("identifier_whitelist")
        if not isinstance(whitelist, dict):
            return []
        values: List[str] = []
        for key in ("ports", "component_types", "component_implementations", "data_types", "subcomponents"):
            entry = whitelist.get(key)
            if isinstance(entry, list):
                values.extend(str(item) for item in entry)
        return values

    def _extract_relevant_identifiers(self, requirement: str, known_identifiers: List[str]) -> List[str]:
        relevant = []
        lowered_req = (requirement or "").lower()
        for identifier in known_identifiers:
            if identifier and identifier.lower() in lowered_req:
                relevant.append(identifier)
        for token in re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", requirement or ""):
            if "_" in token or any(ch.isupper() for ch in token[1:]):
                relevant.append(token)
        return _ordered(relevant)

    def _source_priority_for_features(self, patterns: List[str], target_scope: str) -> List[str]:
        if "temporal_history" in patterns or "conditional_assignment" in patterns or "output_assignment" in patterns:
            return ["Kexp", "Ksyn", "Kdef"]
        if "component_implementation" in target_scope:
            return ["Ksyn", "Kdef", "Kexp"]
        return ["Ksyn", "Kexp", "Kdef"]

    def _scored_card_to_dict(self, item: ScoredCard, include_body: bool = False) -> Dict[str, Any]:
        payload = {
            "id": item.card.card_id,
            "kind": item.card.kind,
            "source": item.card.source,
            "topic": item.card.topic,
            "score": item.score,
            "details": item.details,
            "body_preview": _truncate(item.card.body, 280),
        }
        if include_body:
            payload["body"] = item.card.body
        return payload
