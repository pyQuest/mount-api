init:
	pip install -U pipenv
	pipenv lock
	pipenv install --dev

test:
	pipenv run mypy --ignore-missing-imports mountapi/
	pipenv run py.test --capture=no --cov-report term-missing --cov-report html --cov=mountapi --flake8 tests/

