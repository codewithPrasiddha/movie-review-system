FROM python:3.9

WORKDIR /app

COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y netcat-openbsd

COPY . .  

COPY wait-for-db.sh .
RUN chmod +x wait-for-db.sh
CMD ["./wait-for-db.sh", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
