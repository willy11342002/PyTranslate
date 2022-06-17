# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
import builtins
p = Path('.env')
for line in p.read_text(encoding='utf8').split('\n'):
    if '=' not in line:
        continue
    key, value = line.split('=', 1)
    setattr(builtins, key, value)


a = Analysis(
    ['main.py'],
    pathex=[Path(SPECPATH).absolute()],
    binaries=[],
    datas=[
        ('icon.png', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='中鍵快速鍵小工具',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=f'中鍵快速鍵小工具 V{VERSION}',
)
