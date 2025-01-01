# Use the official Python image from the DockerHub
FROM python:3.11.3-slim-buster

# Set the working directory in docker
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get install -y \
    make \
    netcat \
    gcc \
    postgresql-client \
    libpq-dev \
    python3-dev

# install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# copy project
COPY . /app/

# Make sure the entrypoint script exists and is executable
COPY scripts/entrypoint.sh /app/scripts/
RUN chmod +x /app/scripts/entrypoint.sh

ENTRYPOINT ["/app/scripts/entrypoint.sh"]