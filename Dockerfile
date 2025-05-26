FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -e .

ENV FLASK_APP=src.myapp.app
CMD ["flask", "run", "--host=0.0.0.0"]