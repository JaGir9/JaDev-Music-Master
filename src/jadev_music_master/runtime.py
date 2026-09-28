from __future__ import annotations

import os
import sys
from pathlib import Path


def app_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(getattr(sys, "_MEIPASS", Path(sys.executable).parent))
    return Path(__file__).resolve().parents[2]


def bundled_binary(name: str) -> str:
    exe = f"{name}.exe" if os.name == "nt" else name
    candidate = app_root() / "vendor" / "ffmpeg" / "bin" / exe
    if candidate.exists():
        return str(candidate)
    return name
