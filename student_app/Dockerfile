# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "app/main.py"]

