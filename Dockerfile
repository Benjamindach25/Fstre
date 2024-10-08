FROM python:3.8-slim-buster
WORKDIR /app
RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 main.py
