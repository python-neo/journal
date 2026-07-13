.PHONY: install run clean

VENV := venv

ifeq ($(OS),Windows_NT)
	PYTHON := python
	PIP := $(VENV)/Scripts/python -m pip
	RUN := $(VENV)/Scripts/python -m journal
else
	PYTHON := python3
	PIP := $(VENV)/bin/python -m pip
	RUN := $(VENV)/bin/python -m journal
endif

install:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e .

run:
	$(RUN)

clean:
	$(PYTHON) -c "import shutil; shutil.rmtree('$(VENV)', ignore_errors=True)"