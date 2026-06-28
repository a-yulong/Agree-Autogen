"""Simulate initial AGREE annex generation and score the result.

This is an offline audit helper. It does not call an LLM. It estimates what a
conservative downstream generator should do when given AADL + Req:

- behavior requirements: produce a simple initial annex when a clear expression
  can be recovered from the natural language;
- structural/property requirements: produce an empty annex and route the case to
  AADL-level validation instead of fabricating AGREE clauses.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\Sources_Curated_ParagraphStyle_20260603")
DEFAULT_REPORT_ROOT = Path(r"C:\Users\25780\Desktop\Exp_Data\SourceReq_Quality_Audit")


EMPTY_ANNEX = "annex agree {**\n**};"


@dataclass(frozen=True)
class Score:
    traceability: int
    feasibility: int
    non_fabrication: int
    coverage: int
    syntax: int

    @property
    def total(self) -> int:
        return self.traceability + self.feasibility + self.non_fabrication + self.coverage + self.syntax


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulate AGREE generation and score outputs.")
    parser.add_argument("--root", default=str(DEFAULT_ROOT))
    parser.add_argument("--report-root", default=str(DEFAULT_REPORT_ROOT))
    args = parser.parse_args()

    root = Path(args.root)
    report_root = Path(args.report_root)
    report_root.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    for case_dir in sorted(iter_case_dirs(root), key=lambda p: natural_key(p.name)):
        rows.append(simulate_case(case_dir))

    csv_path = report_root / "paragraph_req_simulated_agree_scoring.csv"
    md_path = report_root / "paragraph_req_simulated_agree_scoring.md"
    write_csv(csv_path, rows)
    write_summary(md_path, rows)
    print(f"Simulated labels: {len(rows)}")
    print(f"CSV: {csv_path}")
    print(f"Summary: {md_path}")
    return 0


def iter_case_dirs(root: Path) -> list[Path]:
    return [p for p in root.iterdir() if p.is_dir() and re.fullmatch(r"Case\d+_[A-Z]", p.name)]


def natural_key(text: str) -> list[Any]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def simulate_case(case_dir: Path) -> dict[str, Any]:
    match = re.fullmatch(r"Case(\d+)_([A-Z])", case_dir.name)
    assert match
    case_label = f"Case{int(match.group(1)):02d}"
    req_path = case_dir / f"{case_label}_Req.txt"
    sidecar_path = case_dir / f"{case_label}_Req_Expected.json"
    aadl_path = case_dir / f"{case_label}_Base.aadl"
    if not aadl_path.exists():
        aadl_path = case_dir / f"{case_label}_Base.txt"
    req = req_path.read_text(encoding="utf-8", errors="replace").strip()
    sidecar = json.loads(sidecar_path.read_text(encoding="utf-8", errors="replace"))
    aadl = aadl_path.read_text(encoding="utf-8", errors="replace") if aadl_path.exists() else ""
    items = sidecar.get("requirement_items", [])
    classes = Counter(item.get("requirement_class", "") for item in items)
    target = sidecar.get("target", "") or infer_target(req, aadl)
    route = infer_route(classes, sidecar.get("action", ""))
    annex, decision, rationale = generate_initial_annex(req, aadl, target, route)
    score, notes = score_output(req, aadl, items, route, annex, decision)
    return {
        "label": case_dir.name,
        "target": target,
        "route": route,
        "decision": decision,
        "score_total": score.total,
        "score_traceability_30": score.traceability,
        "score_feasibility_20": score.feasibility,
        "score_non_fabrication_25": score.non_fabrication,
        "score_coverage_15": score.coverage,
        "score_syntax_10": score.syntax,
        "score_notes": notes,
        "simulated_initial_agree_annex": annex,
        "rationale": rationale,
        "req_text": req,
        "classes": dict(classes),
    }


def infer_route(classes: Counter, action: str) -> str:
    if classes.get("kept_existing_precise") or action == "kept_existing_high_quality":
        return "agree_generation"
    if classes.get("structural_check") and classes.get("property_check"):
        return "aadl_structural_property_validation"
    if classes.get("structural_check"):
        return "aadl_structural_validation"
    if classes.get("property_check"):
        return "aadl_property_validation"
    return "unknown"


def infer_target(req: str, aadl: str) -> str:
    match = re.search(r"\bThe\s+([A-Za-z_][A-Za-z0-9_.]*)\s+component\b", req)
    if match:
        return match.group(1)
    match = re.search(r"(?im)^\s*(?:system|process|thread|device)\s+([A-Za-z_][A-Za-z0-9_]*)\b", aadl)
    return match.group(1) if match else ""


def generate_initial_annex(req: str, aadl: str, target: str, route: str) -> tuple[str, str, str]:
    if route != "agree_generation":
        return (
            EMPTY_ANNEX,
            "empty_annex_structural_or_property_requirement",
            "The requirement is traceable to AADL structure/property facts rather than AGREE runtime expressions.",
        )
    features = extract_features(aadl, target)
    visible = {feature["name"]: feature for feature in features}
    clauses = infer_behavior_clauses(req, visible)
    if not clauses:
        return (
            EMPTY_ANNEX,
            "empty_annex_no_safe_expression_recovered",
            "No safe expression over visible target-interface symbols was recovered without inventing variables.",
        )
    annex = "annex agree {**\n" + "\n".join(f"  {clause}" for clause in clauses[:4]) + "\n**};"
    return annex, "non_empty_initial_agree_annex", "Recovered conservative assume/guarantee clauses over visible symbols."


def extract_features(aadl: str, target: str) -> list[dict[str, str]]:
    block = extract_component_block(aadl, target)
    if not block:
        return []
    section = extract_section(block, "features")
    pattern = re.compile(
        r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*"
        r"(?:(in|out|in\s+out)\s+)?"
        r"(?:(event\s+data|event|data)\s+)?port\s*([^;{]*)\s*;"
    )
    features = []
    for match in pattern.finditer(section):
        features.append(
            {
                "name": match.group(1),
                "direction": re.sub(r"\s+", " ", match.group(2) or "in out").strip(),
                "category": re.sub(r"\s+", " ", match.group(3) or "data").strip(),
                "type": re.sub(r"\s+", " ", match.group(4) or "").strip(),
                "scalar": infer_scalar(match.group(4) or "", match.group(3) or "data"),
            }
        )
    return features


def infer_scalar(type_text: str, category: str) -> str:
    text = f"{type_text} {category}".lower()
    if "boolean" in text or re.search(r"\bbool\b", text):
        return "bool"
    if any(token in text for token in ("float", "real", "double", "integer", "int", "unsigned", "long", "short")):
        return "numeric"
    if "event" in text:
        return "event"
    return "opaque"


def extract_component_block(aadl: str, target: str) -> str:
    if not target:
        return ""
    component = target.split(".", 1)[0]
    kind = r"(?:system|process|thread|device|abstract|subprogram|processor)"
    start = re.search(rf"(?im)^\s*{kind}\s+{re.escape(component)}\b.*$", aadl)
    if not start:
        return ""
    end = re.search(rf"(?im)^\s*end\s+{re.escape(component)}\s*;", aadl[start.end() :])
    if not end:
        return ""
    return aadl[start.start() : start.end() + end.end()]


def extract_section(block: str, name: str) -> str:
    match = re.search(
        rf"(?ims)^\s*{re.escape(name)}\s*$"
        r"(.*?)(?=^\s*(?:features|subcomponents|connections|flows|properties|modes|calls|annex|end\b)\s*)",
        block,
    )
    return match.group(1) if match else ""


def infer_behavior_clauses(req: str, visible: dict[str, dict[str, str]]) -> list[str]:
    clauses: list[str] = []
    names = sorted(visible, key=len, reverse=True)
    lower = req.lower()

    # Range patterns. Keep these deliberately local so one variable does not
    # accidentally inherit another variable's range from the same sentence.
    for name in names:
        if name.lower() not in lower:
            continue
        if visible[name].get("scalar") != "numeric":
            continue
        range_expr = find_local_range_expr(req, name)
        if range_expr:
            keyword = "assume" if visible[name]["direction"].startswith("in") else "guarantee"
            clauses.append(f'{keyword} "{name} range": {range_expr};')

    clauses.extend(infer_bool_trigger_clauses(req, visible))

    # Simple output equality: "Output ... equal to ... Input"
    eq_patterns = [
        r"\b([A-Za-z_][A-Za-z0-9_]*)\b[^.]{0,80}shall[^.]{0,40}(?:be|is|are)?\s*(?:strictly\s+)?equal(?: to)?[^.]{0,80}\b([A-Za-z_][A-Za-z0-9_]*)\b",
        r"\b([A-Za-z_][A-Za-z0-9_]*)\b[^.]{0,80}=\s*\b([A-Za-z_][A-Za-z0-9_]*)\b",
    ]
    for pattern in eq_patterns:
        for match in re.finditer(pattern, req, flags=re.IGNORECASE):
            left, right = match.group(1), match.group(2)
            if left in visible and right in visible and left != right:
                out, inp = choose_output_input(left, right, visible)
                if out and inp:
                    clauses.append(f'guarantee "{out} equals {inp}": {out} = {inp};')

    return dedupe(clauses)


def infer_bool_trigger_clauses(req: str, visible: dict[str, dict[str, str]]) -> list[str]:
    clauses: list[str] = []
    bool_outputs = [
        name
        for name, feature in visible.items()
        if feature.get("scalar") == "bool" and feature.get("direction", "").startswith("out")
    ]
    numeric_inputs = [
        name
        for name, feature in visible.items()
        if feature.get("scalar") == "numeric" and feature.get("direction", "").startswith("in")
    ]
    if not bool_outputs or not numeric_inputs:
        return clauses
    sentences = re.split(r"(?<=[.!?;])\s+", req)
    for sentence in sentences:
        sent_lower = sentence.lower()
        if not re.search(r"\b(if|when|whenever)\b", sent_lower):
            continue
        if not re.search(r"\b(true|activated|requested|raised|set)\b", sent_lower):
            continue
        for out_name in bool_outputs:
            if not re.search(rf"\b{re.escape(out_name)}\b", sentence, flags=re.IGNORECASE):
                continue
            conditions = []
            for in_name in numeric_inputs:
                condition = find_condition_expr(sentence, in_name)
                if condition:
                    conditions.append(condition)
            if conditions:
                clauses.append(f'guarantee "{out_name} trigger": {" or ".join(conditions)} => {out_name} = true;')
    return clauses


def choose_output_input(left: str, right: str, visible: dict[str, dict[str, str]]) -> tuple[str, str]:
    if visible[left]["direction"].startswith("out") and visible[right]["direction"].startswith("in"):
        return left, right
    if visible[right]["direction"].startswith("out") and visible[left]["direction"].startswith("in"):
        return right, left
    return "", ""


def find_local_range_expr(req: str, name: str) -> str | None:
    sentences = re.split(r"(?<=[.!?;])\s+", req)
    name_re = re.compile(rf"\b{re.escape(name)}\b", flags=re.IGNORECASE)
    for sentence in sentences:
        if not name_re.search(sentence):
            continue
        if re.search(r"\b(if|when|whenever|only if)\b", sentence, flags=re.IGNORECASE):
            continue
        if re.search(r"\btrue\s+only\s+if\b|\bonly\s+if\b", sentence, flags=re.IGNORECASE):
            # "output is true only if input < threshold" is a boolean implication,
            # not a range constraint on the output or a plain input assumption.
            continue
        # If several visible-looking identifiers are listed before a single
        # range expression, do not guess that all share the same range.
        if re.search(r"\bfollowing\s+variables\b|\bas follows\b", sentence, flags=re.IGNORECASE):
            continue
        expr = find_direct_numeric_relation(sentence, name)
        if expr:
            return expr
    return None


def find_condition_expr(sentence: str, name: str) -> str | None:
    if not re.search(rf"\b{re.escape(name)}\b", sentence, flags=re.IGNORECASE):
        return None
    return find_direct_numeric_relation(sentence, name)


def find_direct_numeric_relation(sentence: str, name: str) -> str | None:
    subject = (
        rf"\b{re.escape(name)}\b"
        r"(?:\s+(?:input|output|signal|port|parameter|variable|value))*"
        r"(?:\s+(?:has|have)\s+(?:a\s+)?value)?"
        r"(?:\s+(?:is|are|shall\s+be|must\s+be|remains?|remain|stays?|stay|has|have))?"
        r"\s*(?:a\s+value\s+)?"
    )
    between = re.search(
        subject
        + r"(?:strictly\s+)?(?:between|within(?: the)?(?: closed interval)?)\s*(?:\[)?\s*(-?\d+(?:\.\d+)?)\s*(?:,|and|to)\s*(-?\d+(?:\.\d+)?)",
        sentence,
        flags=re.IGNORECASE,
    )
    if between:
        return f"{name} >= {between.group(1)} and {name} <= {between.group(2)}"
    reverse_between = re.search(
        r"(?:between|within(?: the)?(?: closed interval)?)\s*(?:\[)?\s*(-?\d+(?:\.\d+)?)\s*(?:,|and|to)\s*(-?\d+(?:\.\d+)?)\s*(?:\])?\s+"
        + rf"(?:for|on|of)?\s*\b{re.escape(name)}\b",
        sentence,
        flags=re.IGNORECASE,
    )
    if reverse_between:
        return f"{name} >= {reverse_between.group(1)} and {name} <= {reverse_between.group(2)}"
    le = re.search(subject + r"(?:less than or equal to|at most|no more than)\s*(-?\d+(?:\.\d+)?)", sentence, flags=re.IGNORECASE)
    if le:
        return f"{name} <= {le.group(1)}"
    ge = re.search(subject + r"(?:greater than or equal to|at least|no less than)\s*(-?\d+(?:\.\d+)?)", sentence, flags=re.IGNORECASE)
    if ge:
        return f"{name} >= {ge.group(1)}"
    gt = re.search(subject + r"(?:strictly\s+)?greater than\s*(-?\d+(?:\.\d+)?)", sentence, flags=re.IGNORECASE)
    if gt:
        return f"{name} > {gt.group(1)}"
    lt = re.search(subject + r"(?:strictly\s+)?less than\s*(-?\d+(?:\.\d+)?)", sentence, flags=re.IGNORECASE)
    if lt:
        return f"{name} < {lt.group(1)}"
    # List form: "a, b, and c are all greater than 0". Only use it when the
    # sentence explicitly says the listed variables all share the relation.
    list_match = re.search(
        rf"\b{re.escape(name)}\b[^.;]{{0,80}}\ball\s+(?:are|remain|hold)?\s*(?:strictly\s+)?greater than\s*(-?\d+(?:\.\d+)?)",
        sentence,
        flags=re.IGNORECASE,
    )
    if list_match:
        return f"{name} > {list_match.group(1)}"
    list_between = re.search(
        rf"\b{re.escape(name)}\b[^.;]{{0,80}}\ball\s+(?:are|remain|hold)?\s*(?:between|within)\s*(-?\d+(?:\.\d+)?)\s*(?:,|and|to)\s*(-?\d+(?:\.\d+)?)",
        sentence,
        flags=re.IGNORECASE,
    )
    if list_between:
        return f"{name} >= {list_between.group(1)} and {name} <= {list_between.group(2)}"
    return None


def dedupe(items: list[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def score_output(
    req: str,
    aadl: str,
    items: list[dict[str, Any]],
    route: str,
    annex: str,
    decision: str,
) -> tuple[Score, str]:
    trace_score = score_traceability(items, aadl)
    feasibility_score = 20 if route != "unknown" else 8
    fabricated = detects_fabrication(annex, aadl)
    non_fabrication = 25 if not fabricated else 5
    syntax = 10 if annex_syntax_ok(annex) else 0
    if route == "agree_generation":
        # The simulator is intentionally conservative and only recovers simple
        # clauses. A non-empty behavior annex is useful but still only an
        # initial draft; an empty behavior annex means the requirement likely
        # needs real LLM reasoning instead of rule extraction.
        coverage = 12 if decision == "non_empty_initial_agree_annex" else 4
    else:
        coverage = 15 if annex.strip() == EMPTY_ANNEX else 4
    notes = []
    if fabricated:
        notes.append("annex may reference identifiers not found in AADL")
    if route != "agree_generation" and annex.strip() == EMPTY_ANNEX:
        notes.append("empty annex is appropriate for structural/property requirement")
    if route == "agree_generation" and decision != "non_empty_initial_agree_annex":
        notes.append("behavior requirement needs LLM reasoning; heuristic produced no safe expression")
    if route == "agree_generation" and decision == "non_empty_initial_agree_annex":
        notes.append("initial annex is conservative and may be partial")
    return Score(trace_score, feasibility_score, non_fabrication, coverage, syntax), "; ".join(notes) or "ok"


def score_traceability(items: list[dict[str, Any]], aadl: str) -> int:
    if not items:
        return 0
    ok = 0
    for item in items:
        check = item.get("expected_check") or {}
        if not check:
            # kept behavior items have weaker sidecar trace, but are known AGREE-derived.
            if item.get("requirement_class") == "kept_existing_precise":
                ok += 0.75
            continue
        missing = missing_trace_terms(check, aadl)
        if not missing:
            ok += 1
    return round(30 * ok / len(items))


def missing_trace_terms(check: dict[str, Any], aadl: str) -> list[str]:
    terms: list[str] = []
    kind = check.get("kind", "")
    if kind == "connection":
        terms.extend([check.get("connection", ""), check.get("source", ""), check.get("destination", "")])
    elif kind == "property":
        terms.extend([check.get("property", ""), check.get("value", "")])
        if check.get("element"):
            terms.append(check.get("element", ""))
    aadl_lower = aadl.lower()
    aadl_compact = re.sub(r"\s+", "", aadl_lower)
    missing = []
    for term in terms:
        term = str(term).strip()
        if not term:
            continue
        if term.lower() not in aadl_lower and re.sub(r"\s+", "", term.lower()) not in aadl_compact:
            missing.append(term)
    return missing


def detects_fabrication(annex: str, aadl: str) -> bool:
    if annex.strip() == EMPTY_ANNEX:
        return False
    no_labels = re.sub(r'"[^"]*"', '""', annex)
    identifiers = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", no_labels))
    reserved = {
        "annex",
        "agree",
        "assume",
        "guarantee",
        "true",
        "false",
        "and",
        "or",
        "if",
        "then",
        "else",
    }
    aadl_lower = aadl.lower()
    for ident in identifiers - reserved:
        if ident.startswith("_"):
            continue
        if ident.lower() not in aadl_lower:
            # quoted label words also appear as identifiers in this regex; ignore common label tokens by len.
            if len(ident) > 2:
                return True
    return False


def annex_syntax_ok(annex: str) -> bool:
    return annex.strip().startswith("annex agree {**") and annex.strip().endswith("**};")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = [
        "label",
        "target",
        "route",
        "decision",
        "score_total",
        "score_traceability_30",
        "score_feasibility_20",
        "score_non_fabrication_25",
        "score_coverage_15",
        "score_syntax_10",
        "score_notes",
        "simulated_initial_agree_annex",
        "rationale",
        "req_text",
        "classes",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: json.dumps(row[field], ensure_ascii=False) if isinstance(row.get(field), dict) else row.get(field, "") for field in fields})


def write_summary(path: Path, rows: list[dict[str, Any]]) -> None:
    routes = Counter(row["route"] for row in rows)
    decisions = Counter(row["decision"] for row in rows)
    scores = [int(row["score_total"]) for row in rows]
    bands = Counter(score_band(score) for score in scores)
    lines = [
        "# Simulated Initial AGREE Annex Scoring",
        "",
        f"- Rows: {len(rows)}",
        f"- Routes: `{json.dumps(dict(routes), ensure_ascii=False)}`",
        f"- Decisions: `{json.dumps(dict(decisions), ensure_ascii=False)}`",
        f"- Score bands: `{json.dumps(dict(bands), ensure_ascii=False)}`",
        f"- Average score: {sum(scores) / len(scores):.1f}",
        "",
        "## Scoring System",
        "",
        "- Traceability: 30 points. Checks whether sidecar trace terms can be found in AADL.",
        "- Feasibility: 20 points. Checks whether the requirement has a clear downstream route.",
        "- Non-fabrication: 25 points. Penalizes invented AGREE identifiers.",
        "- Coverage: 15 points. Rewards non-empty AGREE for behavior requirements and empty annex for structural/property requirements.",
        "- Syntax: 10 points. Checks basic `annex agree {** ... **};` form.",
        "",
        "## Interpretation",
        "",
        "For structural/property requirements, an empty AGREE annex is scored as correct because the proper downstream action is AADL-level validation, not fabricated AGREE generation.",
        "",
        "## Lowest Scoring Examples",
        "",
    ]
    for row in sorted(rows, key=lambda item: int(item["score_total"]))[:20]:
        lines.append(
            f"- `{row['label']}` score={row['score_total']} route={row['route']} decision={row['decision']} notes={row['score_notes']}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def score_band(score: int) -> str:
    if score >= 90:
        return "90-100"
    if score >= 80:
        return "80-89"
    if score >= 70:
        return "70-79"
    if score >= 60:
        return "60-69"
    return "<60"


if __name__ == "__main__":
    raise SystemExit(main())
