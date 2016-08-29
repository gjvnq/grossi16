# -*- mode: python -*-

block_cipher = None


a = Analysis(['grossi16-gui.py'],
             pathex=['/home/gabriel/Dropbox/Projects/Grossi16/py_installer'],
             binaries=None,
             datas=[ ('base.ui', 'grossi16.gui' ) ],
             hiddenimports=['six', 'packaging', 'packaging.version', 'packaging.specifiers', 'packaging.requirements'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='grossi16-gui',
          debug=False,
          strip=False,
          upx=True,
          console=True )
