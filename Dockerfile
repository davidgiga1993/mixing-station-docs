FROM python:3.8.5-slim-buster

WORKDIR /opt/mkdocs
COPY requirements.txt ./

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt