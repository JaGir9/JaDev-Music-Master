from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class Track:
    path: Path


@dataclass(slots=True)
class AudioProject:
    tracks: list[Track] = field(default_factory=list)

    def add(self, path: str | Path) -> Track:
        track = Track(Path(path))
        self.tracks.append(track)
        return track

    def clear(self) -> None:
        self.tracks.clear()
