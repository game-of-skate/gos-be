# Use the official Python image from the DockerHub
FROM python:3.11.3-slim-buster

# Set the working directory in docker
WORKDIR /app

# set environment variables
# PYTHONDONTWRITEBYTECODE Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install make -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install --requirement /app/requirements.txt

# copy project
COPY . /app/

# run entrypoint.sh
ENTRYPOINT ["sh", "/app/scripts/entrypoint.sh"]
