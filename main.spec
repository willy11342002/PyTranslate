# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
import builtins
for line in Path('.env').read_text().split('\n'):
        if line:
            key, value = line.split('=', 1)
            setattr(builtins, key, value)

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\User\\Pictures\\專案程式碼\\翻譯機'],
             binaries=[],
             datas=[
                 ('.env', '.'),
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='翻譯機',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name=f'翻譯機 V{builtins.VERSION}')
