# Use a lightweight official Python image based on Debian's Buster
FROM python:3.9.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

RUN apk add --no-cache openssh

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire Flask application code into the container
COPY . .

# Expose the port your Flask app will listen on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "restAPI.py"] 
