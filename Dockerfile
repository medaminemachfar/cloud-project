# Dockerfile
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Run the application
CMD ["python", "app.py"]
# Dockerfile for MySQL
FROM mysql:8

ENV MYSQL_DATABASE=flaskdb
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_USER=flaskuser
ENV MYSQL_PASSWORD=flaskpassword