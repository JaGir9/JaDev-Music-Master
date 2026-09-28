from pathlib import Path

from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules("PySide6")

a = Analysis(
    ["src/jadev_music_master/__main__.py"],
    pathex=["src"],
    binaries=[],
    datas=[],
    hiddenimports=hiddenimports,
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="JaDevMusicMaster",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)
