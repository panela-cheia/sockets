FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN python -m venv env \
    && . env/bin/activate \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [". env/bin/activate && python src/main.py"]