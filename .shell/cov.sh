#!/bin/bash
PYTHONPATH=`pwd` poetry run pytest --cov-report term --cov hooks tests/ >>.logs/coverage.txt
poetry run coverage-badge -o assets/images/coverage.svg -f -q
