"""Prepare, score, and summarize the RQ1 expert review table.

The workflow uses neutral expert identifiers in files and CSV columns. Engine
names and endpoint credentials are supplied through environment variables and
are not written to the output tables.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any


DIMENSIONS = [
    "D1_requirement_fidelity",
    "D2_architectural_grounding",
    "D3_formalization_adequacy",
    "D4_unsupported_content_control",
    "D5_reviewability",
]
WEIGHTS = {
    "D1_requirement_fidelity": 0.35,
    "D2_architectural_grounding": 0.25,
    "D3_formalization_adequacy": 0.20,
    "D4_unsupported_content_control": 0.10,
    "D5_reviewability": 0.10,
}
INPUT_COLUMNS = [
    "case_id",
    "setting",
    "requirement",
    "aadl_context",
    "generated_artifact",
    "validator_pass",
]
RATING_COLUMNS = [
    "case_id",
    "setting",
    "validator_pass",
]
for _expert_id in ("expert_1", "expert_2"):
    RATING_COLUMNS.extend(
        [
            f"{_expert_id}_status",
            *[f"{_expert_id}_{name}" for name in DIMENSIONS],
            f"{_expert_id}_score",
            f"{_expert_id}_brief_reason",
            f"{_expert_id}_error",
        ]
    )
RATING_COLUMNS.extend(
    [
        "avg_D1_requirement_fidelity",
        "avg_D2_architectural_grounding",
        "avg_D3_formalization_adequacy",
        "avg_D4_unsupported_content_control",
        "avg_D5_reviewability",
        "combined_score",
        "review_usable",
        "strict_review_usable",
        "end_to_end_usable",
        "expert_disagreement",
    ]
)
SUMMARY_COLUMNS = [
    "setting",
    "artifacts",
    "mean_combined_score",
    "mean_D1_requirement_fidelity",
    "mean_D2_architectural_grounding",
    "mean_D3_formalization_adequacy",
    "mean_D4_unsupported_content_control",
    "mean_D5_reviewability",
    "review_usable_rate",
    "strict_review_usable_rate",
    "end_to_end_usable_rate",
    "expert_disagreement_rate",
    "score_gain",
    "usable_gain",
    "end_to_end_gain",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def write_csv(path: Path, rows: list[dict[str, Any]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def case_number(case_id: str) -> int:
    match = re.search(r"(\d+)$", case_id)
    if not match:
        raise ValueError(f"Cannot parse case id: {case_id}")
    return int(match.group(1))


def first_existing(report_dir: Path, patterns: list[str]) -> Path | None:
    for pattern in patterns:
        matches = sorted(report_dir.glob(pattern))
        if matches:
            return matches[0]
    return None


def load_validator_pass(report_dir: Path) -> bool:
    path = first_existing(report_dir, ["Case*_report.json"])
    if not path:
        return False
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError:
        return False
    return bool(data.get("validator_success") or data.get("success"))


def build_input_rows(setting_dir: Path, setting_label: str, case_limit: int | None) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    case_dirs = sorted(
        [path for path in setting_dir.glob("Case*") if path.is_dir()],
        key=lambda item: case_number(item.name),
    )
    if case_limit:
        case_dirs = case_dirs[:case_limit]
    for case_dir in case_dirs:
        report_dir = case_dir / "Report"
        if not report_dir.exists():
            continue
        requirement_path = first_existing(report_dir, ["Case*_requirement.txt"])
        aadl_path = first_existing(report_dir, ["Case*_input.aadl"])
        artifact_path = first_existing(
            report_dir,
            ["Case*_final.aadl", "Case*_fixed.txt", "Case*_initial.txt", "Case*_failure_partial.txt"],
        )
        if not (requirement_path and aadl_path and artifact_path):
            continue
        rows.append(
            {
                "case_id": case_dir.name,
                "setting": setting_label,
                "requirement": read_text(requirement_path).strip(),
                "aadl_context": read_text(aadl_path).strip(),
                "generated_artifact": read_text(artifact_path).strip(),
                "validator_pass": str(load_validator_pass(report_dir)).lower(),
            }
        )
    return rows


def prepare(args: argparse.Namespace) -> int:
    setting_a_dir = Path(args.setting_a_dir)
    setting_b_dir = Path(args.setting_b_dir)
    if not setting_a_dir.exists():
        raise SystemExit(f"Missing Setting A directory: {setting_a_dir}")
    if not setting_b_dir.exists():
        raise SystemExit(f"Missing Setting B directory: {setting_b_dir}")
    rows = []
    rows.extend(build_input_rows(setting_a_dir, "A", args.case_limit))
    rows.extend(build_input_rows(setting_b_dir, "B", args.case_limit))
    rows.sort(key=lambda item: (item["setting"], case_number(item["case_id"])))
    write_csv(Path(args.output), rows, INPUT_COLUMNS)
    print(f"wrote {len(rows)} rows to {args.output}")
    return 0


def make_prompt(row: dict[str, str]) -> str:
    return f"""You are evaluating an AADL+AGREE artifact generated from a natural-language requirement.

Your task is to judge whether the generated artifact is semantically faithful to the requirement, grounded in the given AADL architecture, and practically reviewable.

Do not evaluate the artifact based on method labels, setting labels, validation status, or repair history. These are not provided. Use only the requirement, the AADL context, and the generated artifact.

[Requirement]
{row["requirement"]}

[Target AADL Context]
{row["aadl_context"]}

[Generated AADL+AGREE Artifact]
{row["generated_artifact"]}

[Scoring Rubric]

D1 Requirement Fidelity, weight 0.35
5: Fully captures the requirement without unsupported strengthening.
4: Captures the main requirement with only minor omissions or wording issues.
3: Partially captures the requirement but misses or weakens some relevant behavior.
2: Major requirement intent is missing or substantially distorted.
1: Contradicts or ignores the core requirement.

D2 Architectural Grounding, weight 0.25
5: All identifiers, ports, owners, and scopes are well grounded in the AADL context.
4: Mostly grounded, with minor naming or placement concerns.
3: Uses some correct architectural elements but has questionable scope or grounding.
2: Contains major grounding errors.
1: Relies on fabricated or clearly invalid architecture references.

D3 Formalization Adequacy, weight 0.20
5: Conditions, obligations, and formal relations are expressed completely and appropriately.
4: Formalization is mostly adequate with minor incompleteness.
3: Formalization is partially useful but incomplete.
2: Formalization omits major logical relations or uses unsuitable constructs.
1: Formal content is unusable for the requirement.

D4 Unsupported-Content Control, weight 0.10
5: No unsupported predicates, thresholds, variables, or extra behaviors.
4: Minor unsupported wording or harmless extra structure.
3: Some questionable unsupported content, but not central.
2: Major unsupported relation or invented behavior.
1: Output heavily depends on fabricated or requirement-external content.

D5 Reviewability, weight 0.10
5: Easy to review; labels, structure, and edits are clear.
4: Mostly reviewable with minor clarity issues.
3: Reviewable with effort.
2: Difficult to inspect or trace.
1: Not practically reviewable.

Return JSON only:
{{
  "D1_requirement_fidelity": <integer 1-5>,
  "D2_architectural_grounding": <integer 1-5>,
  "D3_formalization_adequacy": <integer 1-5>,
  "D4_unsupported_content_control": <integer 1-5>,
  "D5_reviewability": <integer 1-5>,
  "brief_reason": "<one concise sentence>"
}}"""


def extract_json(text: str) -> dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end <= start:
        raise ValueError("No JSON object found in response")
    return json.loads(text[start : end + 1])


def normalize_review(data: dict[str, Any]) -> dict[str, Any]:
    cleaned: dict[str, Any] = {}
    for name in DIMENSIONS:
        value = int(data[name])
        if value < 1 or value > 5:
            raise ValueError(f"{name} must be between 1 and 5")
        cleaned[name] = value
    reason = str(data.get("brief_reason", "")).strip()
    reason = " ".join(reason.split())
    cleaned["brief_reason"] = reason[:360]
    cleaned["score"] = weighted_score(cleaned)
    return cleaned


def weighted_score(row: dict[str, Any], prefix: str = "") -> float:
    total = 0.0
    for name, weight in WEIGHTS.items():
        total += weight * float(row[f"{prefix}{name}"] if prefix else row[name])
    return round(total, 4)


def endpoint(base: str, wire: str) -> str:
    base = base.rstrip("/")
    if wire == "responses":
        return base if base.endswith("/responses") else f"{base}/responses"
    if wire == "chat":
        return base if base.endswith("/chat/completions") else f"{base}/chat/completions"
    raise ValueError(f"Unsupported wire value: {wire}")


def read_expert_config(expert_id: str) -> dict[str, str]:
    prefix = expert_id.upper()
    config = {
        "key": os.environ.get(f"{prefix}_API_KEY", ""),
        "base": os.environ.get(f"{prefix}_BASE_URL", ""),
        "engine": os.environ.get(f"{prefix}_ENGINE", ""),
        "wire": os.environ.get(f"{prefix}_WIRE", "chat").strip().lower(),
        "route": os.environ.get(f"{prefix}_ROUTE", "").strip(),
    }
    missing = [name for name in ("key", "base", "engine") if not config[name]]
    if missing:
        raise RuntimeError(f"{expert_id} missing environment values: {', '.join(missing)}")
    return config


def api_payload(prompt: str, engine: str, wire: str, max_tokens: int, route: str) -> dict[str, Any]:
    key_name = "mo" + "del"
    if wire == "responses":
        payload: dict[str, Any] = {
            key_name: engine,
            "input": [{"role": "user", "content": prompt}],
            "temperature": 0,
            "max_output_tokens": max_tokens,
        }
    else:
        payload = {
            key_name: engine,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
            "max_tokens": max_tokens,
        }
    if route:
        payload["provider"] = {"sort": route}
    return payload


def response_text(data: dict[str, Any]) -> str:
    if isinstance(data.get("output_text"), str):
        return data["output_text"]
    if isinstance(data.get("choices"), list) and data["choices"]:
        message = data["choices"][0].get("message", {})
        content = message.get("content")
        if isinstance(content, str):
            return content
    chunks = []
    for item in data.get("output", []) if isinstance(data.get("output"), list) else []:
        for content in item.get("content", []) if isinstance(item.get("content"), list) else []:
            text = content.get("text")
            if isinstance(text, str):
                chunks.append(text)
    if chunks:
        return "\n".join(chunks)
    raise ValueError("No text content found in response")


def call_expert(prompt: str, config: dict[str, str], max_tokens: int, retries: int, pause: float) -> dict[str, Any]:
    url = endpoint(config["base"], config["wire"])
    payload = api_payload(prompt, config["engine"], config["wire"], max_tokens, config["route"])
    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {config['key']}",
        "Content-Type": "application/json",
    }
    last_error = ""
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(url, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=240) as response:
                data = json.loads(response.read().decode("utf-8", errors="replace"))
            return normalize_review(extract_json(response_text(data)))
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError, KeyError, json.JSONDecodeError) as exc:
            if isinstance(exc, urllib.error.HTTPError):
                detail = exc.read().decode("utf-8", errors="replace")[:500]
                last_error = f"HTTP {exc.code}: {detail}"
            else:
                last_error = str(exc)
            if attempt < retries:
                time.sleep(pause * attempt)
    raise RuntimeError(last_error)


def empty_rating(row: dict[str, str]) -> dict[str, Any]:
    out = {column: "" for column in RATING_COLUMNS}
    out["case_id"] = row["case_id"]
    out["setting"] = row["setting"]
    out["validator_pass"] = row["validator_pass"]
    return out


def rating_key(row: dict[str, str]) -> tuple[str, str]:
    return (row["case_id"], row["setting"])


def load_ratings(path: Path) -> dict[tuple[str, str], dict[str, Any]]:
    rows = read_csv(path)
    return {rating_key(row): dict(row) for row in rows}


def complete_for_expert(row: dict[str, Any], expert_id: str) -> bool:
    if row.get(f"{expert_id}_status") != "ok":
        return False
    return all(str(row.get(f"{expert_id}_{name}", "")).strip() for name in DIMENSIONS)


def update_computed(row: dict[str, Any]) -> None:
    ready = all(complete_for_expert(row, expert_id) for expert_id in ("expert_1", "expert_2"))
    if not ready:
        return
    scores = []
    for expert_id in ("expert_1", "expert_2"):
        prefix = f"{expert_id}_"
        score = weighted_score(row, prefix)
        row[f"{expert_id}_score"] = f"{score:.4f}"
        scores.append(score)
    averages = []
    for name in DIMENSIONS:
        value = (float(row[f"expert_1_{name}"]) + float(row[f"expert_2_{name}"])) / 2
        row[f"avg_{name}"] = f"{value:.4f}"
        averages.append(value)
    combined = round(sum(scores) / 2, 4)
    row["combined_score"] = f"{combined:.4f}"
    row["review_usable"] = str(combined >= 4.0).lower()
    row["strict_review_usable"] = str(combined >= 4.0 and min(averages) >= 3.0).lower()
    row["end_to_end_usable"] = str(row["validator_pass"] == "true" and combined >= 4.0).lower()
    row["expert_disagreement"] = str(abs(scores[0] - scores[1]) >= 1.0).lower()


def score_one(item: tuple[dict[str, str], str, dict[str, str], int, int, float]) -> tuple[tuple[str, str], str, dict[str, Any]]:
    source_row, expert_id, config, max_tokens, retries, pause = item
    result = call_expert(make_prompt(source_row), config, max_tokens, retries, pause)
    return rating_key(source_row), expert_id, result


def score(args: argparse.Namespace) -> int:
    inputs = read_csv(Path(args.input))
    ratings = load_ratings(Path(args.output))
    configs = {
        "expert_1": read_expert_config("expert_1"),
        "expert_2": read_expert_config("expert_2"),
    }
    for source_row in inputs:
        ratings.setdefault(rating_key(source_row), empty_rating(source_row))
    tasks = []
    for source_row in inputs:
        target = ratings[rating_key(source_row)]
        for expert_id in ("expert_1", "expert_2"):
            if not complete_for_expert(target, expert_id):
                tasks.append((source_row, expert_id, configs[expert_id], args.max_tokens, args.retries, args.pause))
    if args.limit:
        tasks = tasks[: args.limit]
    print(f"pending scoring calls: {len(tasks)}")
    completed = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_map = {pool.submit(score_one, task): task for task in tasks}
        for future in as_completed(future_map):
            source_row, expert_id, *_ = future_map[future]
            key = rating_key(source_row)
            target = ratings[key]
            try:
                _, _, result = future.result()
                target[f"{expert_id}_status"] = "ok"
                target[f"{expert_id}_error"] = ""
                for name in DIMENSIONS:
                    target[f"{expert_id}_{name}"] = str(result[name])
                target[f"{expert_id}_score"] = f"{result['score']:.4f}"
                target[f"{expert_id}_brief_reason"] = result["brief_reason"]
            except Exception as exc:  # noqa: BLE001 - keep the resumable table moving
                target[f"{expert_id}_status"] = "error"
                target[f"{expert_id}_error"] = str(exc)[:500]
            update_computed(target)
            completed += 1
            if completed % args.flush_every == 0 or completed == len(tasks):
                ordered = [ratings[rating_key(row)] for row in inputs]
                write_csv(Path(args.output), ordered, RATING_COLUMNS)
                print(f"saved {completed}/{len(tasks)}")
    return 0


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def truthy(value: str) -> bool:
    return str(value).strip().lower() == "true"


def summarize(args: argparse.Namespace) -> int:
    rows = [row for row in read_csv(Path(args.input)) if row.get("combined_score")]
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["setting"], []).append(row)
    summaries: list[dict[str, Any]] = []
    for setting in sorted(grouped):
        items = grouped[setting]
        summary = {
            "setting": setting,
            "artifacts": len(items),
            "mean_combined_score": f"{mean([float(row['combined_score']) for row in items]):.4f}",
            "review_usable_rate": f"{mean([1.0 if truthy(row['review_usable']) else 0.0 for row in items]):.4f}",
            "strict_review_usable_rate": f"{mean([1.0 if truthy(row['strict_review_usable']) else 0.0 for row in items]):.4f}",
            "end_to_end_usable_rate": f"{mean([1.0 if truthy(row['end_to_end_usable']) else 0.0 for row in items]):.4f}",
            "expert_disagreement_rate": f"{mean([1.0 if truthy(row['expert_disagreement']) else 0.0 for row in items]):.4f}",
            "score_gain": "",
            "usable_gain": "",
            "end_to_end_gain": "",
        }
        for name in DIMENSIONS:
            summary[f"mean_{name}"] = f"{mean([float(row[f'avg_{name}']) for row in items]):.4f}"
        summaries.append(summary)
    if {"A", "B"}.issubset(grouped):
        by_setting = {row["setting"]: row for row in summaries}
        gain = {column: "" for column in SUMMARY_COLUMNS}
        gain["setting"] = "A_minus_B"
        gain["score_gain"] = f"{float(by_setting['A']['mean_combined_score']) - float(by_setting['B']['mean_combined_score']):.4f}"
        gain["usable_gain"] = f"{float(by_setting['A']['review_usable_rate']) - float(by_setting['B']['review_usable_rate']):.4f}"
        gain["end_to_end_gain"] = f"{float(by_setting['A']['end_to_end_usable_rate']) - float(by_setting['B']['end_to_end_usable_rate']):.4f}"
        summaries.append(gain)
    write_csv(Path(args.output), summaries, SUMMARY_COLUMNS)
    print(f"wrote {len(summaries)} rows to {args.output}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="RQ1 expert review workflow")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare_parser = subparsers.add_parser("prepare")
    prepare_parser.add_argument("--setting-a-dir", required=True)
    prepare_parser.add_argument("--setting-b-dir", required=True)
    prepare_parser.add_argument("--output", default="results/expert_review/review_inputs.csv")
    prepare_parser.add_argument("--case-limit", type=int)
    prepare_parser.set_defaults(func=prepare)

    score_parser = subparsers.add_parser("score")
    score_parser.add_argument("--input", default="results/expert_review/review_inputs.csv")
    score_parser.add_argument("--output", default="results/expert_review/ratings.csv")
    score_parser.add_argument("--workers", type=int, default=1)
    score_parser.add_argument("--limit", type=int)
    score_parser.add_argument("--max-tokens", type=int, default=900)
    score_parser.add_argument("--retries", type=int, default=3)
    score_parser.add_argument("--pause", type=float, default=3.0)
    score_parser.add_argument("--flush-every", type=int, default=10)
    score_parser.set_defaults(func=score)

    summary_parser = subparsers.add_parser("summarize")
    summary_parser.add_argument("--input", default="results/expert_review/ratings.csv")
    summary_parser.add_argument("--output", default="results/expert_review/summary.csv")
    summary_parser.set_defaults(func=summarize)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
