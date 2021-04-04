# pull official base image
FROM ubuntu:20.04

# Install Python 3.8, pip & development packages, psycopg2, libsndfile1 for speaker-verification

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    python3.8 python3-pip python3.8-dev postgresql-server-dev-12 gcc musl-dev netcat libsndfile1

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies

RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
