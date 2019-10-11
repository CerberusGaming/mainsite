FROM python:alpine

WORKDIR /app
COPY requirements.txt /app/
COPY App /app/App
COPY static /app/static
COPY templates /app/templates
COPY server.py /app/

RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 5000

CMD gunicorn -w 4 -b 0.0.0.0:5000 App:app
