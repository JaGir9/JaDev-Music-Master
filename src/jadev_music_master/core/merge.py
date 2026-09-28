from __future__ import annotations

from pathlib import Path


class MixPlan:
    """Represents a non-destructive merge/mix plan.

    Rendering is intentionally separated from planning so the GUI can expose
    ordering, transition length and future BPM/key-aware decisions before
    committing to a final file.
    """

    def __init__(self) -> None:
        self.tracks: list[Path] = []
        self.crossfade_seconds: float = 0.0

    def add(self, path: str | Path) -> None:
        self.tracks.append(Path(path))

    def reorder(self, old_index: int, new_index: int) -> None:
        track = self.tracks.pop(old_index)
        self.tracks.insert(new_index, track)
