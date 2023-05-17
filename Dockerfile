FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv env \
    && . env/bin/activate \
    && pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [". env/bin/activate && python3 src/main.py"]