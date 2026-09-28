from __future__ import annotations

from pathlib import Path

from .ffmpeg import convert, probe


class SmartConverter:
    """Conservative conversion policy.

    It intentionally avoids pretending that a lossy source becomes
    higher-resolution simply because the destination is WAV or FLAC.
    """

    def convert_to_wav(self, source: str | Path, destination: str | Path) -> None:
        info = probe(source)
        args = ["-vn", "-c:a", "pcm_s24le"]
        if info.sample_rate:
            args.extend(["-ar", str(info.sample_rate)])
        convert(source, destination, args)

    def convert_to_flac(self, source: str | Path, destination: str | Path) -> None:
        info = probe(source)
        args = ["-vn", "-c:a", "flac"]
        if info.sample_rate:
            args.extend(["-ar", str(info.sample_rate)])
        convert(source, destination, args)

    def convert_to_mp3_320(self, source: str | Path, destination: str | Path) -> None:
        convert(source, destination, ["-vn", "-c:a", "libmp3lame", "-b:a", "320k"])
