ANSIBLE_VIRTUALENV ?= .venv
ANSIBLE_PYTHON := . $(ANSIBLE_VIRTUALENV)/bin/activate && python3
ANSIBLE_PIP := $(ANSIBLE_PYTHON) -m pip
ANSIBLE_LINT := . $(ANSIBLE_VIRTUALENV)/bin/activate && ansible-lint
ANSIBLE_GALAXY := . $(ANSIBLE_VIRTUALENV)/bin/activate && ansible-galaxy
ANSIBLE_MOLECULE := . $(ANSIBLE_VIRTUALENV)/bin/activate && molecule

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

$(ANSIBLE_VIRTUALENV):
	python3 -m venv $(ANSIBLE_VIRTUALENV)
	$(ANSIBLE_PIP) install -U pip setuptools wheel
	$(ANSIBLE_PIP) install -U -r requirements.txt

.PHONY: virtualenv
virtualenv: $(ANSIBLE_VIRTUALENV) ## Create local environment

.PHONY: lint
lint: virtualenv ## Lint Ansible code
	@$(ANSIBLE_LINT) -v

.PHONY: test
test: virtualenv ## Test Ansible code
	@$(ANSIBLE_MOLECULE) test

.PHONY: clean
clean: ## Remove temporary files
	rm -rf $(ANSIBLE_VIRTUALENV) *.tar.gz
