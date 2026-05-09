"""Prepare the public GF_Monitor example in the current case-layout format."""

import argparse
from pathlib import Path


def prepare_case(case_num: int, case_letter: str, source_root: Path) -> Path:
    repo_root = Path(__file__).resolve().parents[1]
    example_dir = repo_root / "data" / "examples" / "gf_monitor"
    case_id = f"Case{case_num:02d}"
    target_dir = source_root / f"{case_id}_{case_letter}"
    target_dir.mkdir(parents=True, exist_ok=True)

    (target_dir / f"{case_id}_Base.txt").write_text((example_dir / "input.aadl").read_text(encoding="utf-8"), encoding="utf-8")
    (target_dir / f"{case_id}_Req.txt").write_text((example_dir / "requirement.txt").read_text(encoding="utf-8"), encoding="utf-8")
    return target_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare GF_Monitor as a CaseXX_A input.")
    parser.add_argument("--case-num", type=int, default=1)
    parser.add_argument("--case-letter", default="A")
    parser.add_argument("--source-root", default="./data/Sources")
    args = parser.parse_args()

    path = prepare_case(args.case_num, args.case_letter, Path(args.source_root))
    print(f"Prepared GF_Monitor case at {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

