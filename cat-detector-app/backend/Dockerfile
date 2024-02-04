# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app to the working directory
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Command to start the app
CMD ["python", "app.py"]
