FROM python:alpine

WORKDIR /app
COPY requirements.txt /app/
COPY App /app/App
COPY static /app/static
COPY templates /app/templates
COPY server.py

RUN pip install -r requirements.txt
