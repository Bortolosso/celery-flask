# pull official base image
FROM python:3.10.2-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update
RUN apt-get install -y unixodbc-dev \
      && apt-get install -y curl \
      && apt-get install -y gnupg2

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt \
      --trusted-host pypi.org \
      --trusted-host files.pythonhosted.org

RUN ACCEPT_EULA=Y curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    ACCEPT_EULA=Y curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    exit

RUN apt-get update \
      && ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17 \
      && ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated mssql-tools \
      && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
      && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc 

RUN apt-get update

COPY . .
