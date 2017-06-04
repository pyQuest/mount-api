init:
	pip install -U pipenv
	pipenv lock
	pipenv install --dev

test:
	mypy mount_api/
	pipenv run py.test --capture=no --cov-report term-missing --cov-report html --cov=mount_api --flake8 tests/

