from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .ffmpeg import ProbeResult, probe


@dataclass(slots=True)
class AnalysisResult:
    technical: ProbeResult
    source_path: Path
    notes: list[str]


class AudioAnalyzer:
    """Initial analysis facade.

    The first production milestone keeps analysis deterministic and offline.
    Additional local models can later enrich BPM, key, genre/tagging,
    embeddings and content-aware mastering decisions.
    """

    def analyze(self, source: str | Path) -> AnalysisResult:
        path = Path(source)
        technical = probe(path)
        notes: list[str] = []

        if technical.codec in {"mp3", "aac", "opus", "vorbis"}:
            notes.append("Lossy source detected. Exporting to WAV/FLAC will not restore discarded source detail.")

        if technical.sample_rate and technical.sample_rate > 96000:
            notes.append("High sample rate detected; avoid unnecessary resampling.")

        return AnalysisResult(technical=technical, source_path=path, notes=notes)
