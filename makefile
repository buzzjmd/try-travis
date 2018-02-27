.DEFAULT_GOAL := help

.PHONY: test
test: ## Run tests
	@echo "+ $@"
	@tox

.PHONY: clean
clean: clean-build clean-pyc clean-pytest ## Remove all file artifacts

.PHONY: clobber
clobber: clean-cov clean-tox clean-caches clean ## Remove all file artifacts and empty caches

.PHONY: clean-build
clean-build: ## Remove build artifacts
	@echo "+ $@"
	@rm -fr build/
	@rm -fr dist/
	@find . -type d -name '*.egg-info' -exec rm -rf {} +

.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts
	@echo "+ $@"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

.PHONY: clean-pytest
clean-pytest: ## Remove pytest artifacts
	@echo "+ $@"
	@find . -type d -name '.pytest_cache' -exec rm -rf {} +

.PHONY: clean-cov
clean-cov: ## Remove coverage artifacts
	@echo "+ $@"
	@tox -e clean-cov

.PHONY: clean-tox
clean-tox: ## Remove tox testing artifacts
	@echo "+ $@"
	@rm -rf .tox/

.PHONY: clean-caches
clean-caches: ## Remove cache for downloaded plugins
	@echo "+ $@"
	@rm -fr .eggs/

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
