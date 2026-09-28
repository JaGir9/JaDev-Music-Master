# Windows Build

## Development run

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:PYTHONPATH = "src"
python -m jadev_music_master
```

FFmpeg and FFprobe must be available in PATH for the current scaffold.

## PyInstaller

Install:

```powershell
pip install pyinstaller
```

Then build from the repository root:

```powershell
pyinstaller JaDevMusicMaster.spec
```

## Production packaging target

The final Windows package should bundle FFmpeg/FFprobe and required Qt runtime files so the user can launch JaDev Music Master by double-clicking the EXE. A separate installer can add Start Menu/Desktop shortcuts and file associations.

Code-signing is strongly recommended for public distribution.
