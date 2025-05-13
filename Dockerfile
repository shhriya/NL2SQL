# Base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Set environment variables (optional; or use secrets during deployment)
# ENV GOOGLE_API_KEY=your_key_here
# ENV GOOGLE_APPLICATION_CREDENTIALS=/app/path/to/service-account.json

# Default command
CMD ["python", "main.py"]
