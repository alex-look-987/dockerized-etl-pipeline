# Archivo: Dockerfile

FROM python:3.12-slim

WORKDIR /app

COPY requiriments.txt .
RUN pip install --no-cache-dir -r requiriments.txt

COPY etl/ ./etl/
COPY data/ ./data/

CMD ['python', "etl/pipeline.py"]