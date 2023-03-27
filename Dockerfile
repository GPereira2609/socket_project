FROM python:3

WORKDIR /socket

COPY . .

CMD ["python", "socket/server.py"]