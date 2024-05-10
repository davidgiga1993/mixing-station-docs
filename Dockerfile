FROM python:3.8.5-slim-buster

WORKDIR /opt/mkdocs
COPY requirements.txt ./
COPY sort-requirements.txt ./

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    pip3 install --no-cache-dir -r sort-requirements.txt && \
    apt update && apt install -y libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info