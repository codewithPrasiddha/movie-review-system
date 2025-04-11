# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt

# Install netcat for wait-for-db.sh
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy all project files
COPY . .

# Make wait script executable
RUN chmod +x wait-for-db.sh

# Start by running wait script and then uvicorn
CMD ["sh", "./wait-for-db.sh", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]