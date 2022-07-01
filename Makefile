# Copyright (c) 2021 Koen Vervloesem
# SPDX-License-Identifier: MIT

generate: ## Generate code
	@echo "Generating code..."
	python3 scripts/generate_modules.py
	black src
	isort src

check: ## Check code
	@echo "Checking code..."
	mypy src
	pflake8 src

test: ## Test code
	@echo "Testing code..."
	pytest

help: ## Show this help message
	@echo "Supported targets:\n"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1:\3/p' \
	| column -t -s ':'

package: ## Package project as source distribution and wheel
	@echo "Packaging project..."
	python3 setup.py sdist bdist_wheel

upload: ## Upload package to PyPI
	@echo "Uploading package to PyPI..."
	python3 -m pip install twine
	twine upload dist/*

.DEFAULT_GOAL := help
.PHONY: \
	generate \
	check \
	test \
    help \
    package \
    upload
