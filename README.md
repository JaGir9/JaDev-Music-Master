# JaDev Music Master

**Professional Offline Audio Production, Mastering, Conversion & Mix Workstation for Windows**

JaDev Music Master is an offline-first desktop audio workstation designed around a simple workflow:

**Import → Analyze → Adaptive Processing → Master → Quality Control → Export**

> **Development status:** Preview / active development. The Windows build is automated, but the complete adaptive mastering engine is still being implemented. Do not treat the current preview as the final v1.0 mastering release.

## Highlights

- **Full Auto** — analyze each track independently and prepare an adaptive processing workflow.
- **Humanize & Master** — production-focused tonal, dynamics, transient, harmonic and stereo processing.
- **Smart Converter** — WAV, FLAC, MP3, AAC/M4A, ALAC, OGG, Opus and related workflows.
- **Merge / Mix** — combine multiple tracks with gapless/crossfade-oriented workflows.
- **Batch Processing** — queue many songs while keeping per-track analysis independent.
- **Quality Control** — architecture for loudness, peak, clipping, stereo and export checks.
- **Offline-first** — the core application is designed not to require an AI API key.
- **Windows EXE build** — GitHub Actions builds a self-contained Windows executable with FFmpeg/FFprobe bundled.

The project is intended for Pop, Hip-Hop/R&B, Jazz, Melayu/Dangdut, Rock/Metal, EDM/House/Nightcore, Acoustic, Orchestral, Lo-fi, Reggae, religious/instrumental music and other styles. Genre/style detection is planned as an advisory signal; processing decisions should ultimately depend on the actual audio.

## Download for Windows

> **Windows EXE:** [Download JaDev Music Master](https://github.com/JaGir9/JaDev-Music-Master/actions)
>
> Open the latest successful **Build Windows EXE** run, then download the **JaDevMusicMaster-Windows** artifact. After extracting the ZIP, run `JaDevMusicMaster.exe`.
>
> **Current status:** development preview. A direct GitHub Releases download will replace the Actions link when the first stable release package is published.

## Windows — Installation & Usage

### Recommended: prebuilt EXE

1. Open the repository **Actions** tab.
2. Select the latest successful **Build Windows EXE** workflow.
3. Under **Artifacts**, download **JaDevMusicMaster-Windows**.
4. Extract the downloaded ZIP.
5. Double-click **JaDevMusicMaster.exe**.
6. No Python installation or command prompt is required for the packaged build.

> Windows SmartScreen may warn about unsigned development builds. Public releases should eventually be code-signed. Only run binaries obtained from this repository's official build/release workflow.

### Basic usage

1. Launch **JaDevMusicMaster.exe**.
2. Choose **Add Audio Files** or add supported audio to the queue.
3. Select the required module:
   - **Full Auto** — intended one-click workflow.
   - **Humanize & Master** — production/mastering workflow.
   - **Converter** — format conversion without creative mastering.
   - **Merge / Mix** — combine multiple tracks.
   - **Batch** — process a larger queue.
   - **Quality Control** — technical verification.
4. Choose the output format/profile when available.
5. Process the queue and review the resulting files/report.

**Note:** the current build is a development preview. Some module screens and advanced DSP features are still under implementation.

## Audio quality principles

JaDev Music Master follows several rules intended to prevent unnecessary quality loss:

- sources remain non-destructive;
- processing should use high precision internally;
- WAV/FLAC are preferred as final lossless masters;
- MP3/AAC should be derived from the finished master rather than repeatedly transcoded;
- source sample rate should normally be preserved unless conversion is intentional;
- MP3 → WAV does **not** restore information already discarded by MP3 encoding;
- converter-only operations must not silently apply mastering;
- batch mode should not blindly apply one identical chain to every song;
- quality-control logic should reduce or reject processing that introduces clipping, excessive dynamics reduction, stereo/phase problems or other measurable degradation.

## Architecture

```text
JaDev Music Master
├── Desktop UI / UX (PySide6 / Qt)
├── Project & Batch Queue
├── Analysis Engine
│   ├── FFprobe technical inspection
│   ├── loudness / true-peak analysis
│   ├── spectrum / dynamics analysis
│   ├── BPM / key analysis
│   └── optional offline genre/style models
├── Adaptive Processing Engine
│   ├── tonal / EQ stage
│   ├── dynamics stage
│   ├── transient stage
│   ├── harmonic / saturation stage
│   ├── stereo management
│   └── limiter / loudness management
├── Never-Degrade / Quality Guard
├── Smart Converter
├── Merge / Mix Engine
├── Export Engine
└── Reports / Logs
```

See [Architecture](docs/ARCHITECTURE.md), [Features](docs/FEATURES.md), and [Roadmap](docs/ROADMAP.md) for the detailed technical plan.

## Developer installation

### Requirements

- Windows 10/11 recommended
- Python 3.11+
- FFmpeg + FFprobe in PATH when running directly from source

### Setup

```powershell
git clone https://github.com/JaGir9/JaDev-Music-Master.git
cd JaDev-Music-Master

py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

$env:PYTHONPATH = "src"
python -m jadev_music_master
```

## Building the EXE locally

```powershell
pip install pyinstaller
pyinstaller --clean --noconfirm JaDevMusicMaster.spec
```

The GitHub workflow performs the Windows build automatically and bundles FFmpeg/FFprobe for the packaged executable.

## Project documentation

- [Feature specification](docs/FEATURES.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Roadmap](docs/ROADMAP.md)
- [Windows build guide](docs/BUILD-WINDOWS.md)

## Responsible use

The project is intended to improve audio production, mastering quality and workflow efficiency. “Humanize” refers to musical/production character and naturalness. The project does not promise detector evasion, false provenance, or guaranteed acceptance by distributors/platforms.

## License

See [LICENSE](LICENSE).
