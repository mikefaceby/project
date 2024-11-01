# Dockerfile für jeden Service

FROM python:3.9-slim
WORKDIR /app

# Installiere erforderliche Pakete
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Kopiere das wait-for-it-Skript und setze die Ausführungsberechtigung
COPY ../wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Kopiere requirements.txt und installiere Abhängigkeiten
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Code
COPY . .

CMD ["python", "app.py"]
