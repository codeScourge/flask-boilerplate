FROM python:3.9.6-alpine3.14

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-c", "config.py", "app:app"]
