# Feature Specification

## Full Auto

- drag and drop source files
- independent per-track analysis
- automatic source-quality checks
- adaptive processing policy
- auto mastering
- QC
- configurable export profiles
- batch queue

## Humanize & Master

"Humanize" refers to production character and musical naturalness, not detector evasion.

Planned controls:

- conservative / balanced / strong processing strength
- tonal balance
- dynamic EQ
- compression
- transient control
- harmonic saturation
- stereo width and correlation protection
- bass/sub management
- harshness / de-essing controls when needed
- limiter / loudness target
- bypass per stage
- source/processed A/B
- loudness-matched A/B

## Smart Converter

Supported target families planned:

- WAV
- FLAC
- MP3
- AAC / M4A
- ALAC
- OGG Vorbis
- Opus
- AIFF

Principles:

- preserve source sample rate by default
- do not fake resolution
- warn about lossy-to-lossless conversion
- stream-copy when technically valid
- optional metadata copy / edit
- batch convert

## Merge / Mix

- manual ordering
- gapless join
- crossfade
- silence trim (optional)
- fade in / out
- loudness matching
- chapter / cue timestamps
- final WAV / FLAC / MP3 / AAC render
- future BPM/key-aware transition assistant

## Quality Control

- codec/source-quality summary
- integrated LUFS
- true peak
- clipping
- stereo correlation
- mono compatibility warning
- DC offset
- silence detection
- export validation
- processing report

## User experience

- professional dark workstation theme
- simple mode and advanced mode
- drag and drop
- real-time job status
- waveform/spectrum visualization
- persistent recent-output folder
- crash-safe logs
- multiple themes planned: Studio Dark, OLED Black, Light Studio, Neon Accent

## Batch

Each track must be analyzed independently. Batch mode must never blindly apply a single fixed chain to every file.
