import hashlib
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

try:
    import tiktoken
except ImportError:
    tiktoken = None

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

try:
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
except NameError:
    script_dir = os.getcwd()
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from experiment_recorder import ExperimentRecorder, create_recorder


def configure_utf8_stdio():
    """Force UTF-8 standard streams on Windows consoles."""
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    os.environ.setdefault("PYTHONUTF8", "1")
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="replace")


configure_utf8_stdio()

RESULT_ROOT = os.environ.get("AGREE_RESULT_ROOT", os.path.abspath("results"))
DEFAULT_MODEL_API_KEY = ""
DEFAULT_MODEL_BASE_URL = os.environ.get("AGREE_MODEL_BASE_URL", "https://api.openai.com/v1")
DEFAULT_MODEL_NAME = os.environ.get("AGREE_MODEL_NAME", "gpt-4o-mini")
MODEL_API_KEY = os.environ.get("AGREE_MODEL_API_KEY", DEFAULT_MODEL_API_KEY)
MODEL_BASE_URL = DEFAULT_MODEL_BASE_URL
MODEL_NAME = DEFAULT_MODEL_NAME


def update_runtime_model_config(
    model_base_url: Optional[str] = None,
    model_api_key: Optional[str] = None,
    model_name: Optional[str] = None,
    result_root: Optional[str] = None,
):
    global MODEL_BASE_URL, MODEL_API_KEY, MODEL_NAME, RESULT_ROOT
    if model_base_url:
        MODEL_BASE_URL = model_base_url
    if model_api_key is not None:
        MODEL_API_KEY = model_api_key
    if model_name:
        MODEL_NAME = model_name
    if result_root:
        RESULT_ROOT = result_root


try:
    import win32con
    import win32gui

    HAS_WIN32 = True
except ImportError:
    HAS_WIN32 = False
    logger.warning("pywin32 is not installed; license pop-up auto-close is disabled.")


def _get_token_encoder():
    if tiktoken is None:
        return None
    try:
        return tiktoken.get_encoding("cl100k_base")
    except Exception:
        try:
            return tiktoken.encoding_for_model("gpt-4o")
        except Exception:
            return None


TOKEN_ENCODER = _get_token_encoder()


def estimate_text_tokens(text: str) -> int:
    if not text:
        return 0
    if TOKEN_ENCODER is not None:
        try:
            return len(TOKEN_ENCODER.encode(text))
        except Exception:
            pass
    return max(1, int(len(text.encode("utf-8")) / 4))


def estimate_messages_tokens(messages: List[Dict[str, str]]) -> int:
    total = 0
    for message in messages:
        total += 4
        total += estimate_text_tokens(message.get("role", ""))
        content = message.get("content", "")
        if isinstance(content, str):
            total += estimate_text_tokens(content)
        else:
            total += estimate_text_tokens(json.dumps(content, ensure_ascii=False))
    return total + 2


def normalize_token_usage(messages: List[Dict[str, str]], response: str, token_usage) -> Dict[str, Any]:
    estimated_prompt = estimate_messages_tokens(messages)
    estimated_completion = estimate_text_tokens(response)

    provider_prompt = getattr(token_usage, "prompt_tokens", None) if token_usage else None
    provider_completion = getattr(token_usage, "completion_tokens", None) if token_usage else None
    provider_total = getattr(token_usage, "total_tokens", None) if token_usage else None

    prompt_suspicious = provider_prompt is None or provider_prompt < max(20, int(estimated_prompt * 0.25))
    completion_suspicious = provider_completion is None or provider_completion < max(10, int(estimated_completion * 0.25))

    final_prompt = estimated_prompt if prompt_suspicious else provider_prompt
    final_completion = estimated_completion if completion_suspicious else provider_completion
    final_total = final_prompt + final_completion

    return {
        "prompt_tokens": final_prompt,
        "completion_tokens": final_completion,
        "total_tokens": final_total,
        "provider_prompt_tokens": provider_prompt,
        "provider_completion_tokens": provider_completion,
        "provider_total_tokens": provider_total,
        "estimated_prompt_tokens": estimated_prompt,
        "estimated_completion_tokens": estimated_completion,
        "used_estimated_prompt": prompt_suspicious,
        "used_estimated_completion": completion_suspicious,
    }


def format_file_link(file_path):
    """Format a local file path as a file URI."""
    if not file_path:
        return ""
    abs_path = os.path.abspath(file_path).replace("\\", "/")
    if abs_path.startswith("/"):
        return f"file://{abs_path}"
    return f"file:///{abs_path}"


def close_license_error_window():
    """Automatically close known AADL Inspector license pop-up windows."""
    if not HAS_WIN32:
        return

    def callback(hwnd, _):
        title = win32gui.GetWindowText(hwnd)
        if title == "AADLInspector":
            return True

        try:
            class_name = win32gui.GetClassName(hwnd)
        except Exception:
            class_name = ""

        try:
            is_visible = win32gui.IsWindowVisible(hwnd)
        except Exception:
            is_visible = False
        if not is_visible:
            return True

        try:
            style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
            is_popup = (style & win32con.WS_POPUP) != 0
            is_dialog = (style & win32con.WS_OVERLAPPEDWINDOW) == 0 and is_popup
        except Exception:
            is_popup = False
            is_dialog = False

        has_ok_button = False
        has_license_text = False

        def child_callback(child_hwnd, _):
            nonlocal has_ok_button, has_license_text
            try:
                child_text = win32gui.GetWindowText(child_hwnd)
                if child_text in ["OK", "Ok"]:
                    has_ok_button = True
                if "license error" in child_text.lower():
                    has_license_text = True
            except Exception:
                pass
            return True

        try:
            win32gui.EnumChildWindows(hwnd, child_callback, None)
        except Exception:
            pass

        is_error_window = False
        if "error" in title.lower() or "license" in title.lower() or "Error in startup script" in title:
            is_error_window = True
        if title == "" and has_ok_button and (is_popup or is_dialog):
            is_error_window = True
        if has_license_text:
            is_error_window = True

        if is_error_window:
            try:
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                logger.info("Attempted to close error window: title='%s', class='%s'", title, class_name)
                if has_ok_button:
                    def click_button(child_hwnd, _):
                        try:
                            child_text = win32gui.GetWindowText(child_hwnd)
                            if child_text in ["OK", "Ok"]:
                                win32gui.PostMessage(child_hwnd, win32con.BM_CLICK, 0, 0)
                                logger.info("Clicked button: %s", child_text)
                        except Exception:
                            pass
                        return True

                    try:
                        win32gui.EnumChildWindows(hwnd, click_button, None)
                    except Exception:
                        pass
            except Exception as exc:
                logger.debug("Error while closing window: %s", exc)
        return True

    try:
        win32gui.EnumWindows(callback, None)
    except Exception as exc:
        logger.debug("Error while enumerating windows: %s", exc)


def start_window_monitor(stop_event, interval=0.5):
    """Start a background monitor that closes known pop-up windows."""
    def monitor():
        while not stop_event.is_set():
            close_license_error_window()
            time.sleep(interval)

    thread = threading.Thread(target=monitor, daemon=True)
    thread.start()
    return thread
