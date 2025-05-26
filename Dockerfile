FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Установка пакета в контейнере
RUN pip install -e .

CMD ["python", "-m", "app.app"]