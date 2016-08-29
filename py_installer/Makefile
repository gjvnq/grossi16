HIMPORTS=six packaging packaging.version packaging.specifiers packaging.requirements
PYINSTALLER=pyinstaller

gui-one-file: grossi16-gui.py grossi16-gui.spec
	-mkdir dist_onefile/
	pyinstaller $(addprefix --hidden-import , $(HIMPORTS)) --distpath dist_onefile/ --onefile grossi16-gui.spec -v
