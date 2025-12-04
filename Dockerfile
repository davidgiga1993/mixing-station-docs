FROM python:3.12-slim-trixie

WORKDIR /opt/mkdocs
COPY requirements.txt ./
COPY sort-requirements.txt ./

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    pip3 install --no-cache-dir -r sort-requirements.txt && \
    apt update && apt install -y libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf-2.0-0 libffi-dev shared-mime-info