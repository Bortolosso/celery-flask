# pull official base image
FROM python:3.10.2-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update  -y
RUN apt-get install -y unixodbc-dev
RUN apt-get install -y unixodbc
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt \
      --trusted-host pypi.org \
      --trusted-host files.pythonhosted.org

# copy project
COPY . .
