FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY healthcheck.py .
COPY .env .

# Create a volume for logs
VOLUME ["/app/logs"]

# Run the script
CMD ["python", "healthcheck.py"] 