.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test clean-celery  ## remove all build, test, coverage and Python artifacts

zip-data:
	tar -zcvf archive/data.tar.gz data

extract-data:
	tar -xf archive/data.tar.gz data/

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . \( -path ./env -o -path ./venv -o -path ./.env -o -path ./.venv \) -prune -o -name '*.egg-info' -exec rm -fr {} +
	find . \( -path ./env -o -path ./venv -o -path ./.env -o -path ./.venv \) -prune -o -name '*.egg' -exec rm -f {} +

clean-celery:  ## Clean up celery artifacts
	-rm celerybeat.pid celerybeat-schedule

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 npi tests

coverage: ## check code coverage quickly with the default Python
	coverage run --source npi -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/npi.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ npi
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

test: clean ## test with local docker env
	docker-compose -f local.yml run django pytest

startapp: ## start new django app. Eg. make startapp app=dummy_app_name
	docker-compose -f local.yml run django sh -c "cd brb/ && python ../manage.py startapp $(app)"

up:  ## Docker compose up (skips building)
	docker-compose -f local.yml up

build-local:  ## build with local docker env
	docker-compose -f local.yml up --build

docker-down:  ## stop deamon process running the local build
	docker-compose -f local.yml down

docker-shell:  ## access the docker conainer shell
	docker-compose -f local.yml run django /bin/sh

make-migrations:  # make migrations
	docker-compose -f production.yml run django python manage.py makemigrations

migrate:  # django migrate
	docker-compose -f local.yml run django python manage.py migrate

build-production:  ## build production env and run on localhost
	docker-compose -f production.yml up --build

prune-volumes: ## prune docker volumes
	docker system prune --volumes

install: clean ## install the package to the active Python's site-packages
	python setup.py install

