FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8009

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8009"]