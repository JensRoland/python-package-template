#!/bin/bash
poetry run pytest --cov-report term --cov src tests/ >>.logs/coverage.txt
poetry run coverage-badge -o assets/images/coverage.svg -f -q
