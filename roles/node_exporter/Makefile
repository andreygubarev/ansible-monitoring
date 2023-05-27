ANSIBLE_VERSION := 7.0.0
ANSIBLE_VIRTUALENV ?= .venv
ANSIBLE_PYTHON := $(ANSIBLE_VIRTUALENV)/bin/python3
ANSIBLE_PIP := $(ANSIBLE_PYTHON) -m pip
ANSIBLE_LINT := $(ANSIBLE_VIRTUALENV)/bin/ansible-lint
ANSIBLE_GALAXY := $(ANSIBLE_VIRTUALENV)/bin/ansible-galaxy

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

$(ANSIBLE_VIRTUALENV):
	python3 -m venv $(ANSIBLE_VIRTUALENV)
	$(ANSIBLE_PIP) install -U pip setuptools wheel
	$(ANSIBLE_PIP) install \
		'ansible>=$(ANSIBLE_VERSION)' \
		'ansible-lint' \
		'molecule>=5.0.0' \
		'testinfra>=6.0.0'

.PHONY: virtualenv
virtualenv: $(ANSIBLE_VIRTUALENV) ## Create local environment

.PHONY: lint
lint: virtualenv ## Lint Ansible code
	@$(ANSIBLE_LINT) -v

.PHONY: clean
clean: ## Remove temporary files
	rm -rf $(ANSIBLE_VIRTUALENV) *.tar.gz
