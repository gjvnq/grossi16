# PYINSTALLER_OPTS=--log-level=DEBUG --debug
MAKESPEC_OPTS=--additional-hooks-dir=hooks

gui-one-file: grossi16-gui.py
	pyi-makespec --onefile $(MAKESPEC_OPTS) grossi16-gui.py
	pyinstaller --distpath dist_onefile/ $(PYINSTALLER_OPTS) grossi16-gui.spec

gui-one-dir: grossi16-gui.py
	pyi-makespec --onedir $(MAKESPEC_OPTS) grossi16-gui.py
	pyinstaller -y --distpath dist_onedir/ $(PYINSTALLER_OPTS) grossi16-gui.spec

cli-one-file: grossi16-cli.py
	pyi-makespec --onefile $(MAKESPEC_OPTS) grossi16-cli.py
	pyinstaller --distpath dist_onefile/ $(PYINSTALLER_OPTS) grossi16-cli.spec

cli-one-dir: grossi16-cli.py
	pyi-makespec --onedir $(MAKESPEC_OPTS) grossi16-cli.py
	pyinstaller -y --distpath dist_onedir/ $(PYINSTALLER_OPTS) grossi16-cli.spec

clean:
	-rm -rf build __pycache__
	-rm *.spec

clean_bins:
	-rm -rf dist dist_onefile dist_onedir