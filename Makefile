# Variables
PYTHON = python
PIP = $(PYTHON) -m pip
POETRY = poetry

# Targets
.PHONY: install test lint check run

install:
	$(POETRY) install

test:
	$(POETRY) run pytest --cov=src tests -vv
	$(POETRY) run coverage-badge -f -o coverage.svg

lint:
	$(POETRY) run ruff check .

check: lint test

run:
	$(POETRY) run uvicorn src.app.main:app --reload
