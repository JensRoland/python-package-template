#!/bin/bash
find . -name 'mypy.svg' -delete
poetry run mypy --config-file pyproject.toml hooks >>.logs/mypy.txt
export mypy_result=$(grep 'Success' .logs/mypy.txt | cut -d\  -f1 | tr -d ':')
echo "mypy result:" $mypy_result
poetry run anybadge -o --value=${mypy_result} --file=assets/images/mypy.svg --label=mypy
