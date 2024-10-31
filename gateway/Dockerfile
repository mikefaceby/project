# Im Verzeichnis ./gateway/Dockerfile

FROM python:3.9-slim
WORKDIR /app

# Installiere erforderliche Pakete
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Kopiere die API-Gateway-Datei und die Abhängigkeiten
COPY api_gateway.py /app/api_gateway.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Starte den API-Gateway-Service
CMD ["python", "/app/api_gateway.py"]
