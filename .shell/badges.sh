#!/bin/bash
rm -rf .logs
mkdir .logs
sh .shell/pylint.sh
sh .shell/mypy.sh
sh .shell/safety.sh
sh .shell/cov.sh
