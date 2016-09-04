# PYINSTALLER_OPTS=--log-level=DEBUG --debug
MAKESPEC_OPTS=--additional-hooks-dir=hooks
PYI-MAKESPEC=pyi-makespec
PYINSTALLER=pyinstaller
PYTHON=python3

# init:
# 	pip install -r requirements.txt

all: egg gui-one-file cli-one-file

install:
	$(PYTHON) setup.py install

install-user:
	$(PYTHON) setup.py install --user

install-dev:
	$(PYTHON) setup.py develop --user

egg:
	$(PYTHON) setup.py bdist_egg

fmt:
	find ./ -iname "*.py" | xargs yapf -i

test:
	cd grossi16 && py.test-3

gui-one-file: grossi16/gui/hack/gui-hack.py
	$(PYI-MAKESPEC) --onefile $(MAKESPEC_OPTS) -n grossi16-gui grossi16/gui/hack/gui-hack.py
	$(PYINSTALLER) --distpath dist/onefile/ $(PYINSTALLER_OPTS) grossi16-gui.spec

gui-one-dir: grossi16/gui/hack/gui-hack.py
	$(PYI-MAKESPEC) --onedir $(MAKESPEC_OPTS) -n grossi16-gui grossi16/gui/hack/gui-hack.py
	$(PYINSTALLER) -y --distpath dist/onedir/ $(PYINSTALLER_OPTS) grossi16-gui.spec

cli-one-file: grossi16/cli/cli.py
	$(PYI-MAKESPEC) --onefile $(MAKESPEC_OPTS) -n grossi16-cli grossi16/cli/cli.py
	$(PYINSTALLER) --distpath dist/onefile/ $(PYINSTALLER_OPTS) grossi16-cli.spec

cli-one-dir: grossi16/cli/cli.py
	$(PYI-MAKESPEC) --onedir $(MAKESPEC_OPTS) -n grossi16-cli grossi16/cli/cli.py
	$(PYINSTALLER) -y --distpath dist/onedir/ $(PYINSTALLER_OPTS) grossi16-cli.spec

clean:
	-rm -rf build __pycache__
	-rm *.spec

clean_bins:
	-rm -rf dist dist_onefile dist_onedir