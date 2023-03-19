SHEll := /bin/bash


TEST = python3 -m pytest --verbosity=2 --showlocals --log-level=DEBUG

test:
	$(TEST)

test-cov:
	$(TEST) --cov=src --cov-report html --cov-fail-under=90

clean: 
	rm -fr __pycache__ .pytest_cache .coverage htmlcov 
