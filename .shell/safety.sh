#!/bin/bash
find . -name 'vulnerabilities.svg' -delete
poetry run safety check -o .logs/safety.txt
export vulnerabilities=$(grep 'vulnerabilities' .logs/safety.txt | cut -d\  -f2)
echo "safety vulnerabilities:" $vulnerabilities
poetry run anybadge -o --value=${vulnerabilities} --file=assets/images/vulnerabilities.svg --color="#40aef9" --label=vulnerabilities
