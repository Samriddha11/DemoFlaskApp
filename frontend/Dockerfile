# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install curl, ping, telnet, and necessary dependencies
RUN apt-get update && apt-get install -y \
    curl \
    iputils-ping \
    telnet \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8989

# Set environment variables
ENV REDIS_HOST=redis-service
ENV REDIS_PORT=6379

# Define the command to run the app using Flask
CMD ["python", "app.py"]
