FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install build dependencies required for kociemba (which has C extensions)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# Copy application files
COPY . .

# Expose port
EXPOSE 8000

# Run with Gunicorn (4 worker processes)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
