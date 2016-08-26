init:
	pip install -r requirements.txt

install:
	python3 setup.py install

install-user:
	python3 setup.py install --user

install-dev:
	python3 setup.py develop --user

egg:
	python3 setup.py bdist_egg

fmt:
	find ./ -iname "*.py" | xargs yapf -i

test:
	cd grossi16 && py.test-3
