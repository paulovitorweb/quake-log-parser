# Variables
PYTHON = python
PIP = $(PYTHON) -m pip
POETRY = poetry
IMAGE_NAME = quake-log-parser-api

# Targets
.PHONY: install test lint check run docker-build docker-run

install:
	$(POETRY) install

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run -p 127.0.0.1:8000:8000 $(IMAGE_NAME)

test:
	$(POETRY) run pytest --cov=src tests -vv
	$(POETRY) run coverage-badge -f -o coverage.svg

lint:
	$(POETRY) run ruff check .

check: lint test

run:
	$(POETRY) run uvicorn src.app.main:app --reload
