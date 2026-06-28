"""External validator execution for the refactored pipeline."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
import threading
from pathlib import Path
from typing import Dict, List, Sequence

from ..runtime import HAS_WIN32, start_window_monitor
from .config import RuntimeConfig
from .state import PipelineState, ValidationOutcome


def _read_text(path: Path) -> str:
    for encoding in ("utf-8", "utf-16", "latin-1"):
        try:
            return path.read_text(encoding=encoding, errors="replace")
        except Exception:
            continue
    return path.read_bytes().decode("latin-1", errors="replace")


def _strip_aadl_line_comments(content: str) -> str:
    return re.sub(r"(?m)--.*$", "", content or "")


class ValidationRunner:
    PREDECLARED_UNITS = {
        "agree_pltl",
        "agree_stdlib",
        "arinc429",
        "arinc653",
        "arp4761",
        "base_types",
        "behavior_properties",
        "code_generation_properties",
        "data_model",
        "communication_properties",
        "deployment",
        "deployment_properties",
        "dreal",
        "emv2",
        "errorlibrary",
        "linearizer",
        "memory_properties",
        "milstd882",
        "modeling_properties",
        "physical",
        "physicalresources",
        "programming_properties",
        "sei",
        "thread_properties",
        "timing_properties",
    }
    STANDARD_PROPERTY_SET_HINTS = {
        "source_data_size": "Memory_Properties",
    }

    def __init__(self, config: RuntimeConfig):
        self.config = config
        self._aadl_library_index: Dict[str, Path] | None = None
        self._property_definition_index: Dict[str, Path] | None = None

    def validate(self, state: PipelineState, artifact_path: Path) -> ValidationOutcome:
        outcome = ValidationOutcome()
        aadl = self._run_aadl_inspector(state, artifact_path)
        agree = self._run_agree_validator(state, artifact_path)
        outcome.aadl_executed = aadl["executed"]
        outcome.agree_executed = agree["executed"]
        outcome.aadl_errors = aadl["errors"]
        outcome.agree_errors = agree["errors"]
        outcome.warnings = aadl["warnings"] + agree["warnings"]
        outcome.aadl_report_path = aadl.get("report_path", "")
        outcome.agree_report_path = agree.get("report_path", "")
        outcome.raw = {"aadl": aadl, "agree": agree, "artifact_path": str(artifact_path)}
        return outcome

    def _run_aadl_inspector(self, state: PipelineState, artifact_path: Path) -> Dict[str, object]:
        if not self.config.aadl_inspector_path:
            return {"executed": False, "errors": ["AADL_INSPECTOR_PATH is not configured."], "warnings": [], "report_path": ""}
        inspector = Path(self.config.aadl_inspector_path)
        if not inspector.exists():
            return {"executed": False, "errors": [f"AADL Inspector not found: {inspector}"], "warnings": [], "report_path": ""}

        report_dir = state.report_dir(self.config.result_root)
        report_dir.mkdir(parents=True, exist_ok=True)
        report_path = report_dir / "aadl_inspector_report.txt"
        aic_path = report_dir / "aadl_inspector_input.aic"
        aadl_files = [artifact_path]
        reference_paths: List[Path] = []
        for ref in state.references:
            path = ref.get("runtime_path")
            if path and Path(path).exists():
                reference_paths.append(Path(path))
        aadl_files.extend(self._prefer_library_equivalents(reference_paths))
        aadl_files, ignored_duplicates = self._dedupe_files_by_declared_units(aadl_files)
        resolved_dependencies = self._resolve_transitive_dependencies(aadl_files)
        property_seed_files = [path for path in aadl_files + resolved_dependencies if path != artifact_path]
        property_dependencies = self._resolve_property_dependencies(property_seed_files)
        combined_files, ignored_dependency_duplicates = self._dedupe_files_by_declared_units(
            aadl_files + resolved_dependencies + property_dependencies
        )
        resolved_dependencies = [path for path in combined_files if path not in aadl_files]
        aadl_files = combined_files
        aic_path.write_text("\n".join(str(path) for path in aadl_files), encoding="utf-8")

        cmd = [
            str(inspector),
            "-a",
            str(aic_path),
            "--plugin",
            "Static.parse",
            "--result",
            str(report_path),
            "--show",
            "false",
            "--aadlVersion",
            "V2",
        ]
        stop_event = threading.Event()
        monitor_thread = start_window_monitor(stop_event) if HAS_WIN32 else None
        try:
            proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", timeout=300)
        except Exception as exc:
            return {"executed": True, "errors": [f"AADL Inspector exception: {exc}"], "warnings": [], "report_path": str(report_path)}
        finally:
            stop_event.set()
            if monitor_thread:
                monitor_thread.join(timeout=1.0)

        errors: List[str] = []
        warnings: List[str] = []
        content = _read_text(report_path) if report_path.exists() else proc.stdout
        success = "Model parsed successfully" in content and not re.search(r"lappend lines\(error\)\s+\d+", content)
        if not success:
            lines = re.findall(r"TextEditor::fastaddText \$sbpText \"(.*?)\"", content, flags=re.DOTALL)
            for line in lines:
                clean = line.strip()
                if clean and "model parsed successfully" not in clean.lower() and "set lines(" not in clean.lower():
                    errors.append(clean)
            if not errors and proc.returncode != 0:
                errors.append(f"AADL Inspector exited with code {proc.returncode}")
        if re.search(r"lappend lines\(warning\)\s+\d+", content):
            warnings.append("AADL Inspector reported warning lines.")
        warnings.extend(ignored_duplicates + ignored_dependency_duplicates)
        return {
            "executed": True,
            "errors": errors,
            "warnings": warnings,
            "report_path": str(report_path),
            "stdout": proc.stdout,
            "resolved_dependencies": [str(path) for path in resolved_dependencies],
            "ignored_duplicate_units": ignored_duplicates + ignored_dependency_duplicates,
        }

    def _run_agree_validator(self, state: PipelineState, artifact_path: Path) -> Dict[str, object]:
        root = self.config.agree_validator_root
        out_dir = root / "out"
        if not out_dir.exists():
            return {"executed": False, "errors": [f"Standalone validator output directory not found: {out_dir}. Run tools/agree-validator/build.ps1."], "warnings": [], "report_path": ""}
        if not self.config.java_home:
            return {"executed": False, "errors": ["JAVA_HOME is not configured."], "warnings": [], "report_path": ""}
        if not self.config.osate_home:
            return {"executed": False, "errors": ["OSATE_HOME is not configured."], "warnings": [], "report_path": ""}

        report_dir = state.report_dir(self.config.result_root)
        report_dir.mkdir(parents=True, exist_ok=True)
        report_path = report_dir / "agree_validator_report.json"
        with tempfile.TemporaryDirectory(prefix="agree_autogen_") as tmp:
            workspace = Path(tmp) / "workspace"
            project = workspace / "CaseProject"
            project.mkdir(parents=True, exist_ok=True)
            (project / ".project").write_text(
                "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
                "<projectDescription>\n"
                "  <name>CaseProject</name>\n"
                "  <comment></comment>\n"
                "  <projects></projects>\n"
                "  <buildSpec></buildSpec>\n"
                "  <natures></natures>\n"
                "</projectDescription>\n",
                encoding="utf-8",
            )
            focus = project / "modified_model.aadl"
            shutil.copy2(artifact_path, focus)
            external_libs = project / "External_Libs"
            external_libs.mkdir(parents=True, exist_ok=True)
            for ref in state.references:
                name = Path(ref.get("path", "reference.aadl")).name
                target = external_libs / name
                target.write_text(ref.get("content", ""), encoding="utf-8", errors="replace")
            staged_files = [focus] + [path for path in external_libs.glob("*.aadl")]
            staged_files = self._prefer_library_equivalents(staged_files)
            staged_files, ignored_duplicates = self._dedupe_files_by_declared_units(staged_files)
            self._remove_unstaged_external_libs(external_libs, staged_files)
            resolved_dependencies = self._resolve_transitive_dependencies(staged_files)
            property_seed_files = [path for path in staged_files + resolved_dependencies if path != focus]
            property_dependencies = self._resolve_property_dependencies(property_seed_files)
            resolved_dependencies = list(dict.fromkeys(resolved_dependencies + property_dependencies))
            for dep in resolved_dependencies:
                target = external_libs / dep.name
                if not target.exists():
                    shutil.copy2(dep, target)
            staged_files, ignored_dependency_duplicates = self._dedupe_files_by_declared_units(staged_files + resolved_dependencies)
            self._remove_unstaged_external_libs(external_libs, staged_files)

            classpath = f"{out_dir};{Path(self.config.osate_home) / 'plugins' / '*'}"
            java = Path(self.config.java_home) / "bin" / "java.exe"
            java_cmd = str(java) if java.exists() else "java"
            cmd = [
                java_cmd,
                "-cp",
                classpath,
                "org.agreeautogen.validator.AgreeValidationCli",
                "--workspace",
                str(workspace),
                "--project",
                str(project),
                "--osate-home",
                self.config.osate_home,
                "--output",
                str(report_path),
                "--focus-file",
                "modified_model.aadl",
            ]
            proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", timeout=180)

        errors: List[str] = []
        warnings: List[str] = []
        payload: Dict[str, object] = {}
        if report_path.exists():
            try:
                payload = json.loads(report_path.read_text(encoding="utf-8", errors="replace"))
                issues = payload.get("issues", [])
                if isinstance(issues, list):
                    errors = [self._format_issue(item) for item in issues if str(item.get("severity", "")).lower() == "error"]
                    warnings = [self._format_issue(item) for item in issues if str(item.get("severity", "")).lower() == "warning"]
                else:
                    raw_errors = payload.get("errors", [])
                    raw_warnings = payload.get("warnings", [])
                    errors = [self._format_issue(item) for item in raw_errors] if isinstance(raw_errors, list) else []
                    warnings = [self._format_issue(item) for item in raw_warnings] if isinstance(raw_warnings, list) else []
            except Exception as exc:
                errors.append(f"Unable to parse AGREE validator report: {exc}")
        elif proc.returncode != 0:
            errors.append(f"AGREE validator did not produce report. Exit code {proc.returncode}. Output: {proc.stdout[:1000]}")
        errors, ignored_duplicate_package_errors = self._filter_duplicate_external_package_errors(errors)
        warnings.extend(ignored_duplicate_package_errors + ignored_duplicates + ignored_dependency_duplicates)
        return {
            "executed": True,
            "errors": errors,
            "warnings": warnings,
            "report_path": str(report_path),
            "stdout": proc.stdout,
            "json": payload,
            "resolved_dependencies": [str(path) for path in resolved_dependencies],
            "ignored_duplicate_units": ignored_duplicates + ignored_dependency_duplicates,
        }

    def _filter_duplicate_external_package_errors(self, errors: List[str]) -> tuple[List[str], List[str]]:
        """Ignore only validator-environment duplicates caused by staging the focus package as an external lib."""
        kept: List[str] = []
        ignored: List[str] = []
        pattern = re.compile(r"Package\s+([A-Za-z_][A-Za-z0-9_:]*)\s+has\s+duplicates\s+External_Libs/\1\.aadl\b", re.IGNORECASE)
        for error in errors:
            if pattern.search(error or ""):
                ignored.append(f"Ignored validator staging duplicate: {error}")
            else:
                kept.append(error)
        return kept, ignored

    def _dedupe_files_by_declared_units(self, files: Sequence[Path]) -> tuple[List[Path], List[str]]:
        """Keep one file per declared package/property set to avoid validator library conflicts."""
        kept: List[Path] = []
        ignored: List[str] = []
        seen_units: Dict[str, Path] = {}
        seen_paths: set[str] = set()
        for file in files:
            if not file:
                continue
            path_key = str(file.resolve()).lower() if file.exists() else str(file).lower()
            if path_key in seen_paths:
                continue
            declared_units = self._extract_declared_units(_read_text(file)) if file.exists() else []
            duplicate_units = [unit for unit in declared_units if unit.lower() in seen_units]
            if duplicate_units:
                first = seen_units[duplicate_units[0].lower()]
                ignored.append(
                    "Ignored duplicate AADL unit declaration: "
                    f"{file} declares {', '.join(duplicate_units)} already provided by {first}"
                )
                continue
            kept.append(file)
            seen_paths.add(path_key)
            for unit in declared_units:
                seen_units[unit.lower()] = file
        return kept, ignored

    def _remove_unstaged_external_libs(self, external_libs: Path, staged_files: Sequence[Path]) -> None:
        staged = {str(path.resolve()).lower() for path in staged_files if path.exists()}
        if not external_libs.exists():
            return
        for file in external_libs.glob("*.aadl"):
            if str(file.resolve()).lower() not in staged:
                try:
                    file.unlink()
                except OSError:
                    pass

    def _resolve_transitive_dependencies(self, seed_files: Sequence[Path]) -> List[Path]:
        """Resolve missing AADL package/property-set files referenced by with clauses."""
        provided = self._declared_or_file_names(seed_files)
        resolved: List[Path] = []
        resolved_keys = set()
        queue = list(seed_files)

        while queue:
            current = queue.pop(0)
            content = _read_text(current) if current.exists() else ""
            for name in list(dict.fromkeys(self._extract_with_names(content) + self._extract_qualified_unit_references(content))):
                normalized_name = self._normalize_unit_name(name)
                top_name = normalized_name.split("::", 1)[0].strip()
                top_key = top_name.lower()
                key = normalized_name.lower()
                if key in self.PREDECLARED_UNITS or top_key in self.PREDECLARED_UNITS:
                    provided.add(key)
                    continue
                if not key or key in provided:
                    continue
                dependency = self._find_aadl_library(normalized_name) or self._find_aadl_library(top_name)
                if dependency is None:
                    continue
                dep_key = str(dependency.resolve()).lower()
                if dep_key in resolved_keys:
                    provided.add(key)
                    continue
                resolved.append(dependency)
                resolved_keys.add(dep_key)
                provided.update(self._declared_or_file_names([dependency]))
                queue.append(dependency)
        return resolved

    def _resolve_property_dependencies(self, seed_files: Sequence[Path]) -> List[Path]:
        """Resolve property-set files needed by unqualified property associations."""
        provided = self._declared_or_file_names(seed_files)
        resolved: List[Path] = []
        seen_paths: set[str] = set()
        for file in seed_files:
            content = _read_text(file) if file.exists() else ""
            for property_name in self._extract_unqualified_property_associations(content):
                property_set_hint = self.STANDARD_PROPERTY_SET_HINTS.get(property_name.lower())
                if not property_set_hint:
                    continue
                dependency = self._find_property_definition_library(property_name, property_set_hint)
                if dependency is None:
                    continue
                declared = {unit.lower() for unit in self._extract_declared_units(_read_text(dependency))}
                if declared and declared.issubset(provided):
                    continue
                dep_key = str(dependency.resolve()).lower()
                if dep_key in seen_paths:
                    continue
                resolved.append(dependency)
                seen_paths.add(dep_key)
                provided.update(declared)
        return resolved

    def _prefer_library_equivalents(self, files: Sequence[Path]) -> List[Path]:
        """Replace minimal static-libs stubs with configured AADL library files when available."""
        preferred: List[Path] = []
        seen: set[str] = set()
        for file in files:
            replacement = self._preferred_equivalent(file)
            key = str(replacement.resolve()).lower() if replacement.exists() else str(replacement).lower()
            if key in seen:
                continue
            seen.add(key)
            preferred.append(replacement)
        return preferred

    def _preferred_equivalent(self, file: Path) -> Path:
        if not file or not file.exists():
            return file
        static_root = (self.config.agree_validator_root / "static-libs").resolve()
        try:
            file.resolve().relative_to(static_root)
            is_static = True
        except ValueError:
            is_static = False
        declared = self._extract_declared_units(_read_text(file))
        for unit in declared:
            candidate = self._find_aadl_library_excluding(unit, {static_root})
            if candidate is not None and (is_static or self._is_better_library_file(file, candidate)):
                return candidate
        return file

    def _is_better_library_file(self, current: Path, candidate: Path) -> bool:
        current_content = _read_text(current)
        candidate_content = _read_text(candidate)
        if current.resolve() == candidate.resolve():
            return False
        current_units = {unit.lower() for unit in self._extract_declared_units(current_content)}
        candidate_units = {unit.lower() for unit in self._extract_declared_units(candidate_content)}
        if not current_units.issubset(candidate_units):
            return False
        current_data = len(re.findall(r"(?im)^\s*data\s+[A-Za-z_][A-Za-z0-9_]*\b", current_content))
        candidate_data = len(re.findall(r"(?im)^\s*data\s+[A-Za-z_][A-Za-z0-9_]*\b", candidate_content))
        current_lines = len(current_content.splitlines())
        candidate_lines = len(candidate_content.splitlines())
        return candidate_data > current_data + 5 or candidate_lines > current_lines * 2

    def _declared_or_file_names(self, files: Sequence[Path]) -> set[str]:
        names: set[str] = set()
        for file in files:
            if not file:
                continue
            names.add(file.stem.lower())
            if file.exists():
                content = _read_text(file)
                for declared in self._extract_declared_units(content):
                    names.add(declared.lower())
                    names.add(self._normalize_unit_name(declared).split("::", 1)[0].lower())
        return names

    def _extract_with_names(self, content: str) -> List[str]:
        names: List[str] = []
        for clause in re.findall(r"(?im)^\s*with\s+([^;]+);", _strip_aadl_line_comments(content)):
            for item in clause.split(","):
                cleaned = item.strip()
                if cleaned:
                    names.append(cleaned)
        return names

    def _extract_qualified_unit_references(self, content: str) -> List[str]:
        names: List[str] = []
        stripped = _strip_aadl_line_comments(content or "")
        for match in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)+)\b", stripped):
            parts = match.group(1).split("::")
            if len(parts) < 2:
                continue
            if parts[0].lower() in self.PREDECLARED_UNITS:
                continue
            for size in range(len(parts), 1, -1):
                names.append("::".join(parts[:size]))
        return list(dict.fromkeys(names))

    def _extract_declared_units(self, content: str) -> List[str]:
        units: List[str] = []
        patterns = [
            r"(?im)^\s*package\s+([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*)\b",
            r"(?im)^\s*property\s+set\s+([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*)\b",
        ]
        for pattern in patterns:
            units.extend(self._normalize_unit_name(match.group(1)) for match in re.finditer(pattern, content))
        return units

    def _extract_unqualified_property_associations(self, content: str) -> List[str]:
        names: List[str] = []
        for match in re.finditer(r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=>", content or ""):
            name = match.group(1)
            if "::" not in name:
                names.append(name)
        return list(dict.fromkeys(names))

    def _find_property_definition_library(self, property_name: str, property_set_hint: str | None = None) -> Path | None:
        if property_set_hint:
            hinted = self._find_aadl_library(property_set_hint)
            if hinted is not None and self._file_declares_property(hinted, property_name):
                return hinted
        index = self._build_property_definition_index()
        return index.get((property_name or "").lower())

    def _file_declares_property(self, file: Path, property_name: str) -> bool:
        if not file or not file.exists():
            return False
        pattern = rf"(?im)^\s*{re.escape(property_name or '')}\s*:"
        return bool(re.search(pattern, _read_text(file)))

    def _find_aadl_library(self, name: str) -> Path | None:
        index = self._build_aadl_library_index()
        key = self._normalize_unit_name(name).lower()
        if key in index:
            return index[key]
        file_key = f"{key}.aadl"
        return index.get(file_key)

    def _find_aadl_library_excluding(self, name: str, excluded_roots: set[Path]) -> Path | None:
        key = self._normalize_unit_name(name).lower()
        for root in self.config.aadl_library_dirs or []:
            resolved_root = root.resolve()
            if any(resolved_root == excluded or resolved_root.is_relative_to(excluded) for excluded in excluded_roots):
                continue
            if not root.exists() or not root.is_dir():
                continue
            for file in root.rglob("*.aadl"):
                content = _read_text(file)
                declared = {item.lower() for item in self._extract_declared_units(content)}
                if key in declared:
                    return file
        return None

    def _normalize_unit_name(self, name: str) -> str:
        return re.sub(r"\s+", "", (name or "").strip()).replace(".", "::")

    def _build_aadl_library_index(self) -> Dict[str, Path]:
        if self._aadl_library_index is not None:
            return self._aadl_library_index

        index: Dict[str, Path] = {}
        roots = self.config.aadl_library_dirs or []
        for root in roots:
            if not root.exists() or not root.is_dir():
                continue
            for file in root.rglob("*.aadl"):
                if any(part.startswith(".") for part in file.parts):
                    continue
                file_key = file.name.lower()
                index.setdefault(file_key, file)
                index.setdefault(file.stem.lower(), file)
                content = _read_text(file)
                for declared in self._extract_declared_units(content):
                    index.setdefault(declared.lower(), file)
                    index.setdefault(declared.replace("::", "-").lower(), file)
                    index.setdefault(declared.replace("::", "_").lower(), file)
        self._aadl_library_index = index
        return index

    def _build_property_definition_index(self) -> Dict[str, Path]:
        if self._property_definition_index is not None:
            return self._property_definition_index

        index: Dict[str, Path] = {}
        for root in self.config.aadl_library_dirs or []:
            if not root.exists() or not root.is_dir():
                continue
            for file in root.rglob("*.aadl"):
                if any(part.startswith(".") for part in file.parts):
                    continue
                content = _read_text(file)
                if not re.search(r"(?im)^\s*property\s+set\s+", content):
                    continue
                for match in re.finditer(r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:", content):
                    index.setdefault(match.group(1).lower(), file)
        self._property_definition_index = index
        return index

    def _format_issue(self, issue) -> str:
        if isinstance(issue, str):
            return issue
        if not isinstance(issue, dict):
            return str(issue)
        location = issue.get("location") or issue.get("file") or ""
        line = issue.get("line") or issue.get("lineNumber") or ""
        message = issue.get("message") or issue.get("text") or issue.get("issue") or str(issue)
        if location or line:
            return f"{location} | line {line}: {message}"
        return str(message)
