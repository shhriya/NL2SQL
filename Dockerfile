# Use the official Python image from DockerHub
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port for your application (change if using a different port)
EXPOSE 5000

# Define the command to run your app (adjust as per your app structure)
CMD ["python", "main.py"]
