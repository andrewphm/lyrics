# Use an official Python runtime (version 3.8) as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the rest of the application code
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variable for the Flask application
ENV FLASK_APP=app.py

# Set environment variable 
ENV FLASK_ENV=production

# Run the command to start Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
