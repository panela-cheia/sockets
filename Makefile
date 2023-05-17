.PHONY: install run

install:
    python -m venv env
    source env/bin/activate && pip install -r requirements.txt

run:
    source env/bin/activate && python src/main.py
