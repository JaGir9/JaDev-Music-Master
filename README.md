# JaDev Music Master

Professional offline audio mastering, adaptive humanization, conversion, batch processing, and mix/merge workstation for Windows.

> Status: initial production scaffold. The application is designed to run locally without requiring an AI API key for its core audio workflow.

## Product vision

JaDev Music Master is designed as a desktop audio workstation focused on one-click processing without hiding the technical details from advanced users. The core workflow is:

**Import → Analyze → Adaptive Humanize → Master → Quality Control → Export**

The application is intended to support a wide range of music, including pop, hip-hop/R&B, jazz, Melayu/Dangdut, rock, metal, EDM, house, nightcore, acoustic, orchestral, lo-fi, reggae, religious/instrumental, and mixed-genre material.

## Core modules

- **Full Auto** — analyzes the source, estimates musical/audio characteristics, chooses a conservative processing chain, performs mastering, runs QC, then exports.
- **Humanize & Master** — adaptive dynamics, tonal shaping, transient control, stereo management, harmonic treatment, loudness management, and safety checks.
- **Converter** — MP3/WAV/FLAC/AAC/M4A/ALAC/OGG/Opus conversion with source-quality safeguards.
- **Merge / Mix** — joins multiple tracks into one file with gapless, crossfade, loudness matching, and future BPM/key-aware transition support.
- **Batch Processor** — processes large queues while analyzing each track independently.
- **A/B & QC** — source vs processed comparison, loudness/peak checks, clipping checks, and processing report.

## Important design principle

The software is built to improve audio quality and make production feel more natural and polished. It is **not** designed to falsify provenance, bypass platform checks, or guarantee that any detector or distributor will classify AI-generated audio as human-made.

## Professional architecture

```text
JaDev Music Master
├─ UI / UX (PySide6 / Qt)
├─ Analysis Engine
│  ├─ FFprobe metadata
│  ├─ loudness / true-peak analysis
│  ├─ spectrum & dynamics analysis
│  └─ optional local genre / tagging models
├─ Processing Engine
│  ├─ adaptive EQ
│  ├─ dynamics control
│  ├─ transient / saturation stages
│  ├─ stereo management
│  └─ limiter / loudness management
├─ Converter Engine
├─ Merge / Mix Engine
├─ Quality Guard
├─ Export Engine
└─ Reports / Logs
```

## Quick start for development

### 1. Requirements

- Windows 10/11 (primary target)
- Python 3.11+
- FFmpeg + FFprobe available in PATH during development
- Optional: Essentia or another local model package for genre/tagging expansion

### 2. Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run

```bash
python -m jadev_music_master
```

### 4. Build Windows executable

```bash
pyinstaller JaDevMusicMaster.spec
```

The final production installer can bundle FFmpeg binaries and required runtime assets so end users can launch the app directly without Python or CMD.

## Output philosophy

For mastering, WAV or FLAC should be used as the primary lossless master. MP3/AAC should be generated from the finished master rather than repeatedly transcoding lossy files.

If the input is MP3, exporting to WAV does **not** recreate information already lost by MP3 compression. The application therefore avoids misleading "fake quality" upsampling and preserves source sample rate unless a user explicitly requests otherwise.

## Roadmap

See [docs/ROADMAP.md](docs/ROADMAP.md) and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
