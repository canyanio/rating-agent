docker_image = canyan/rating-agent

.PHONY:
venv:
	virtualenv -p python3 venv --no-site-packages

.PHONY: setup
setup:
	pip install -r requirements.txt
	pip install --editable .

.PHONY: dist
dist:
	python3 setup.py sdist bdist_wheel

.PHONY: clean
clean:
	rm -fr build dist *.egg-info

.PHONY: black
black:
	black --skip-string-normalization rating_agent *.py

.PHONY: black-check
black-check:
	black --check --skip-string-normalization rating_agent *.py

.PHONY: flake8
flake8:
	flake8 --ignore=E501,E402,W503 rating_agent *.py

.PHONY: mypy
mypy:
	mypy rating_agent

.PHONY: pylint
pylint:
	pylint rating_agent *.py

.PHONY: pycodestyle
pycodestyle:
	pycodestyle --ignore=E501,W503,E402,E701 rating_agent *.py

.PHONY: check
check: black-check flake8 mypy pylint pycodestyle

.PHONY: test
test:
	py.test -p no:warnings

.PHONY: coverage
coverage:
	coverage run -m py.test -p no:warnings
	coverage report
	coverage html
	coverage xml

.PHONY: agent
agent:
	rating-agent -h 0.0.0.0 -p 8000

.PHONY: agent-dev
agent-dev:
	rating-agent -h 0.0.0.0 -p 8000 --debug

.PHONY: dockerfile
dockerfile:
	docker build -t $(docker_image):master .

.PHONY: dockerfile-tests
dockerfile-tests:
	docker build -t $(docker_image):tests -f Dockerfile.tests .

.PHONY: docker-start
docker-start:
	docker-compose -f docker-compose.yaml -f docker-compose.tests.yaml up -d

.PHONY: docker-stop
docker-stop:
	docker-compose -f docker-compose.yaml -f docker-compose.tests.yaml down
