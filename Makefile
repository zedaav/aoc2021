.SILENT:
SHELL := /bin/bash

# Default: nothing to do
.PHONY: default
default:
	true

# Clean un-tracked files
.PHONY: clean
clean:
	git clean -fdX

# Venv setup
VENV := venv
IN_VENV := source $(VENV)/bin/activate &&
ALL_REQUIREMENTS := requirements-dev.txt requirements-test.txt
PYTHON := python3.8
$(VENV): $(ALL_REQUIREMENTS)
	rm -Rf $(VENV)
	$(PYTHON) -m venv $(VENV)
	$(IN_VENV) pip install pip --upgrade
	$(IN_VENV) pip install pip $(foreach req,$(ALL_REQUIREMENTS),-r $(req))

# Venv clean
.PHONY: clean-venv
clean-venv:
	rm -Rf $(VENV)

# Build
.PHONY: build
build:
	rm -Rf out/dist
	$(IN_VENV) ./setup.py sdist --dist-dir out/dist
	$(IN_VENV) pip uninstall -y aoc2021
	$(IN_VENV) pip install out/dist/*.tar.gz

# Tests
.PHONY: tests
tests: build
	rm -Rf out/tests out/coverage* out/.coverage
	$(IN_VENV) pytest --cov-fail-under=100
