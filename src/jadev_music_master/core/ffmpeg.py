from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from jadev_music_master.runtime import bundled_binary


@dataclass(slots=True)
class ProbeResult:
    duration: float | None
    codec: str | None
    sample_rate: int | None
    channels: int | None
    bit_rate: int | None


def ffmpeg_available() -> bool:
    ffmpeg = bundled_binary("ffmpeg")
    ffprobe = bundled_binary("ffprobe")
    ffmpeg_ok = Path(ffmpeg).exists() or shutil.which(ffmpeg) is not None
    ffprobe_ok = Path(ffprobe).exists() or shutil.which(ffprobe) is not None
    return ffmpeg_ok and ffprobe_ok


def probe(path: str | Path) -> ProbeResult:
    command = [
        bundled_binary("ffprobe"), "-v", "error",
        "-show_entries", "format=duration,bit_rate:stream=codec_name,sample_rate,channels",
        "-select_streams", "a:0", "-of", "json", str(path),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=True)
    data = json.loads(completed.stdout)
    streams = data.get("streams") or [{}]
    stream = streams[0]
    fmt = data.get("format") or {}
    return ProbeResult(
        duration=float(fmt["duration"]) if fmt.get("duration") else None,
        codec=stream.get("codec_name"),
        sample_rate=int(stream["sample_rate"]) if stream.get("sample_rate") else None,
        channels=int(stream["channels"]) if stream.get("channels") else None,
        bit_rate=int(fmt["bit_rate"]) if fmt.get("bit_rate") else None,
    )


def convert(source: str | Path, destination: str | Path, extra_args: list[str] | None = None) -> None:
    command = [bundled_binary("ffmpeg"), "-hide_banner", "-y", "-i", str(source)]
    if extra_args:
        command.extend(extra_args)
    command.append(str(destination))
    subprocess.run(command, check=True)
