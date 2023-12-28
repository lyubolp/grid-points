venv:
    . .venv/bin/activate

init:
    python3 -m venv .venv
    venv
    pip install -r requirements.txt

lint: venv
    python3 -m pylint src/* tst/* --fail-under 9
    mypy src tst --ignore-missing-imports
    flake8 src tst

test: venv
    python3 -m unittest discover -s tst


pre-push: venv lint test coverage

push: pre-push
    git push

coverage: venv
    coverage run -m unittest discover -s tst
    coverage report -m --fail-under 75

run: venv
    python3 src/main.py