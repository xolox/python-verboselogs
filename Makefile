# Verbose and spam log levels for Python's logging module.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: June 23, 2016
# URL: https://github.com/xolox/python-verboselogs

WORKON_HOME ?= $(HOME)/.virtualenvs
VIRTUAL_ENV ?= $(WORKON_HOME)/verboselogs
PATH := $(VIRTUAL_ENV)/bin:$(PATH)
MAKE := $(MAKE) --no-print-directory
SHELL = bash

default:
	@echo 'Makefile for verboselogs'
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make install   install the package in a virtual environment'
	@echo '    make reset     recreate the virtual environment'
	@echo '    make check     check coding style (PEP-8, PEP-257)'
	@echo '    make readme    update usage in readme'
	@echo '    make docs      update documentation using Sphinx'
	@echo '    make publish   publish changes to GitHub/PyPI'
	@echo '    make clean     cleanup all temporary files'
	@echo

install:
	@test -d "$(VIRTUAL_ENV)" || mkdir -p "$(VIRTUAL_ENV)"
	@test -x "$(VIRTUAL_ENV)/bin/python" || virtualenv --quiet "$(VIRTUAL_ENV)"
	@test -x "$(VIRTUAL_ENV)/bin/pip" || easy_install pip
	@test -x "$(VIRTUAL_ENV)/bin/pip-accel" || pip install --quiet pip-accel
	@pip uninstall --yes verboselogs &>/dev/null || true
	@pip install --quiet --editable .

reset:
	$(MAKE) clean
	rm -Rf "$(VIRTUAL_ENV)"
	$(MAKE) install

check: install
	pip-accel install --upgrade --quiet flake8 flake8-docstrings
	flake8

docs: install
	pip-accel install --quiet sphinx
	cd docs && sphinx-build -nb html -d build/doctrees . build/html

publish: install
	git push origin && git push --tags origin
	make clean
	pip-accel install --quiet twine wheel
	python setup.py sdist bdist_wheel
	twine upload dist/*
	make clean

clean:
	rm -Rf *.egg .coverage .tox build dist docs/build htmlcov
	find -depth -type d -name __pycache__ -exec rm -Rf {} \;
	find -type f -name '*.pyc' -delete

.PHONY: default install reset check docs publish clean
