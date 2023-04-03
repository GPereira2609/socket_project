FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .

ENV PYTHONPATH /usr/src/app

EXPOSE 5000

CMD ["python", "server.py"]