#!/bin/bash
find . -name 'pylint.svg' -delete
poetry run pylint src >>.logs/pylint-log.txt
export lintscore=$(grep 'rated at' .logs/pylint-log.txt | cut -d\  -f7 | cut -d \/ -f 1)
echo "pylint score:" $lintscore
poetry run anybadge -o --value=${lintscore} --file=assets/images/pylint.svg --label=pylint
