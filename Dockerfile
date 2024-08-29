# Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt first for better caching
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variables (optional)
ENV FLASK_APP=app
ENV FLASK_ENV=development

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
