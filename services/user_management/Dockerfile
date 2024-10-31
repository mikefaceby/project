# Dockerfile für den Service (z.B. user_management_service)

FROM python:3.9-slim
WORKDIR /app

# Installiere erforderliche Pakete
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Kopiere requirements.txt und installiere Abhängigkeiten
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Code
COPY . .

CMD ["python", "app.py"]
