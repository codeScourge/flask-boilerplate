FROM python:3.10-bookworm
WORKDIR /app

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./backend .

CMD ["bash", "run.sh"]
