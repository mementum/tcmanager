# -*- mode: python -*-
a = Analysis(['src/tcmanager.pyw'],
             pathex=['./scripts'],
             hiddenimports=[],
             hookspath=['./scripts/hooks'],
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='tcmanager.exe',
          debug=False,
          strip=None,
          upx=False,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=False,
               name='tcmanager')
