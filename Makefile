.PHONY: install run

install:
    python3 -m venv env
    source env/bin/activate && pip3 install -r requirements.txt

run:
    source env/bin/activate && python3 src/main.py
