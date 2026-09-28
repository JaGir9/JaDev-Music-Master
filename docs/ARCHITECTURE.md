# Architecture

## Goals

JaDev Music Master is an offline-first Windows audio workstation. The architecture intentionally separates UI, analysis, signal-processing decisions, rendering, and quality control so each component can evolve independently.

## Layers

### Presentation

PySide6/Qt provides the desktop shell, drag-and-drop, file queue, module navigation, progress, meters, analysis summaries, A/B controls, and future waveform/spectrum displays.

### Project layer

A project owns the source queue, per-track settings, processing state, reports and export destinations. Sources should be treated as immutable.

### Analysis

Initial technical analysis uses FFprobe. Planned analysis includes:

- duration / codec / channel count / sample rate / bit rate
- integrated loudness / loudness range / true peak
- clipping / DC offset / crest-factor style metrics
- spectrum and low-frequency balance
- stereo correlation
- onset / transient descriptors
- BPM / beat positions
- key / tonal descriptors
- local genre / style tags with confidence

Genre detection is an advisory signal, not the sole source of mastering decisions.

### Adaptive processing

The mastering chain should be generated from measured problems and conservative constraints rather than from a single fixed genre preset.

Potential stages:

1. cleanup only when necessary
2. tonal balance / EQ
3. dynamic control
4. transient shaping
5. harmonic treatment / saturation
6. stereo management
7. final loudness / limiting
8. QC and automatic rollback/reduction when thresholds are violated

### Never-Degrade Guard

The quality guard protects against:

- clipping and true-peak overs
- excessive gain reduction
- pumping
- excessive brightness / harshness
- unstable stereo / negative correlation
- unnecessary resampling
- repeated lossy transcoding
- needless processing of already healthy material

The first implementation should use deterministic safety limits. Later versions can add perceptual comparison models, but the source must remain available for A/B verification.

### Converter

Converter mode is separate from mastering. A user who asks only for MP3 → WAV should not receive EQ, compression, limiting or other creative processing.

A lossy source converted to a lossless container stays a lossy-derived source. The UI must make that distinction clear.

### Merge / Mix

Two initial merge modes:

- Gapless Join
- Crossfade Mix

Future smart transition planning can use beat positions, BPM, musical key, loudness and structure while remaining optional for non-DJ material.

### Precision

Decode to floating-point for processing when practical, avoid intermediate lossy encodes, and render one final master before deriving distribution formats.

## Threading

Long-running analysis and FFmpeg jobs must execute outside the Qt UI thread. The production build should use a job queue with cancellation, progress and structured logs.

## Packaging

Windows production packaging should include:

- application executable
- bundled FFmpeg / FFprobe
- Qt runtime
- local assets / models
- default configuration
- installer and optional portable package

No core workflow should require a cloud API key.
