# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.7-alpine

WORKDIR /app

# install the requirements
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . .

# initialize the database (create DB, tables, populate)
RUN python app.py

EXPOSE 5000/tcp

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]