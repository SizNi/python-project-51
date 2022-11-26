install: # install poetry
	poetry install

build:
	poetry build

pytest:
	poetry run pytest

lint: # запуск flake8 на проект python-project-50
	poetry run flake8

page-loader:
	poetry run page-loader