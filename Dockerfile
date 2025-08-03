# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask flask-cors pandas

# Expose port your Flask app will run on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
