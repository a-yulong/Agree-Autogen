import os
import sys
import re
import hashlib
import logging
import subprocess
import time
import tempfile
import threading
import shutil
from pathlib import Path
from typing import List, Dict, Optional, Any, Union
import json

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
    """在 Windows 下强制标准输入输出使用 UTF-8，避免 GBK 控制台编码异常。"""
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    os.environ.setdefault("PYTHONUTF8", "1")

    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="replace")


configure_utf8_stdio()

GLM_RESULT_ROOT = os.environ.get("AGREE_RESULT_ROOT", os.path.abspath("results"))
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
    global MODEL_BASE_URL, MODEL_API_KEY, MODEL_NAME, GLM_RESULT_ROOT

    if model_base_url:
        MODEL_BASE_URL = model_base_url
    if model_api_key is not None:
        MODEL_API_KEY = model_api_key
    if model_name:
        MODEL_NAME = model_name
    if result_root:
        GLM_RESULT_ROOT = result_root


try:
    import win32gui
    import win32con
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
    """
    需求5：格式化文件路径为可点击的链接格式

    在支持的终端中，file:/// 协议的路径可以直接点击打开文件
    """
    if not file_path:
        return ""

    # 转换为绝对路径
    abs_path = os.path.abspath(file_path)

    # 替换反斜杠为正斜杠
    abs_path = abs_path.replace('\\', '/')

    # 格式化: file:///C:/path/to/file
    if abs_path.startswith('/'):
        # Unix/Linux 路径
        return f"file://{abs_path}"
    else:
        # Windows 路径 (需要三个斜杠)
        return f"file:///{abs_path}"


def close_license_error_window():
    """自动关闭 AADL Inspector 的许可证错误弹窗"""
    if not HAS_WIN32:
        return

    def callback(hwnd, _):
        # 获取窗口标题
        title = win32gui.GetWindowText(hwnd)

        # 跳过主程序窗口
        if title == "AADLInspector":
            return True

        # 获取窗口类名
        try:
            class_name = win32gui.GetClassName(hwnd)
        except:
            class_name = ""

        # 检查窗口是否可见
        try:
            is_visible = win32gui.IsWindowVisible(hwnd)
        except:
            is_visible = False

        if not is_visible:
            return True

        # 获取窗口样式，检查是否是弹出窗口/对话框
        try:
            style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
            is_popup = (style & win32con.WS_POPUP) != 0
            is_dialog = (style & win32con.WS_OVERLAPPEDWINDOW) == 0 and is_popup
        except:
            is_popup = False
            is_dialog = False

        # 尝试通过子窗口判断是否是许可证错误弹窗（查找"确定"按钮等）
        has_ok_button = False
        has_license_text = False

        def child_callback(child_hwnd, _):
            nonlocal has_ok_button, has_license_text
            try:
                child_text = win32gui.GetWindowText(child_hwnd)
                if child_text in ["确定", "OK", "Ok"]:
                    has_ok_button = True
                if "License error" in child_text or "license error" in child_text.lower():
                    has_license_text = True
            except:
                pass
            return True

        try:
            win32gui.EnumChildWindows(hwnd, child_callback, None)
        except:
            pass

        # 综合判断是否是需要关闭的错误窗口
        is_error_window = False

        # 1. 标题匹配
        if ("Error" in title or "error" in title.lower() or "License" in title or "Error in startup script" in title):
            is_error_window = True

        # 2. 空标题但有"确定"按钮且是弹出窗口（许可证错误弹窗的特征）
        if title == "" and has_ok_button and (is_popup or is_dialog):
            is_error_window = True

        # 3. 子窗口包含许可证错误文本
        if has_license_text:
            is_error_window = True

        if is_error_window:
            try:
                # 方法1: 发送 WM_CLOSE 消息
                win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                logger.info(f"已尝试关闭错误窗口 (WM_CLOSE): title='{title}', class='{class_name}'")

                # 方法2: 如果有"确定"按钮，直接点击按钮（更可靠）
                if has_ok_button:
                    def click_button(child_hwnd, _):
                        try:
                            child_text = win32gui.GetWindowText(child_hwnd)
                            if child_text in ["确定", "OK", "Ok"]:
                                # 点击按钮：发送 BM_CLICK 消息
                                win32gui.PostMessage(child_hwnd, win32con.BM_CLICK, 0, 0)
                                logger.info(f"已点击按钮: {child_text}")
                        except:
                            pass
                        return True
                    try:
                        win32gui.EnumChildWindows(hwnd, click_button, None)
                    except:
                        pass
            except Exception as e:
                logger.debug(f"关闭窗口时出错: {e}")
        return True

    try:
        win32gui.EnumWindows(callback, None)
    except Exception as e:
        logger.debug(f"枚举窗口时出错: {e}")


def start_window_monitor(stop_event, interval=0.5):
    """启动一个线程持续监控并关闭弹窗"""
    def monitor():
        while not stop_event.is_set():
            close_license_error_window()
            time.sleep(interval)

    thread = threading.Thread(target=monitor, daemon=True)
    thread.start()
    return thread

