# speaker-verification-api

As [Speaker Verification](https://github.com/OnTrack-UG-Squad/speaker-verification), a Python package, matures, the direction of its finial implementation needs to be considered. This project tends to be a continually evolving extension of Doubtfire. This direction, Speaker Verification API Based on Django, will serve as an effective way to guide next steps on how the project will proceed.

## Table of Contents

- [Tech stack](#tech-stack)
- [Running the project](#running-the-project)
  - [Prerequisites](#prerequisites)
  - [Setting up the project](#setting-up-the-project)
- [API Documentation](#api-documentation)
  - [API Description](#api-description)
  - [Example](#example)

## Tech stack

- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Celery](https://github.com/celery/celery)

## Running the project

### Prerequisites

- [docker-compose](https://docs.docker.com/compose/install/)
- [python3](https://www.python.org/downloads/)

### Setting up the project

1. Clone the repository

```bash
$ git clone https://github.com/OnTrack-UG-Squad/speaker-verification-api.git
```

2. Copy .env.dev.db.sample & .env.dev.sample files from sample_envs to project root. Remove .sample at the end of the file extensions.

```bash
$ cp sample_envs/.env.dev.db.sample .env.dev.db
$ cp sample_envs/.env.dev.sample .env.dev
```

3. Fill the env files

- Populate `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` in `.env.dev.db` (Choose any user name and password)
- Copy these values to the corresponding fields in .env.dev: `SQL_USER=POSTGRES_USER`, `SQL_DATABASE=POSTGRES_DB` `SQL_PASSWORD=POSTGRES_PASSWORD`

4. Populate `SECRET_KEY` in `.env.dev` - Generate a key with the following Python command
```bash
$ python3 -c 'import random; result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-*=+)") for i in range(50)]); print(result)'
```

5. Run the Docker containers

```bash
$ docker-compose -f docker-compose.yml up -d --build
```

6. The app is listening at `http://localhost:8000`

- Open `http://localhost:8000/redis-healthcheck`: Check the `Redis`'s health and the response would be `Redis is connected successfully`
- Open `http://localhost:8000/flower`: Redirects to the `Flower` dashboard

The runtime output can be viewed via `docker logs`

## API Documentation

### API Description

- __Enrolling a user__

```
POST /enroll
```

**Request** `POST`

| Parameter      |  Type  | Description           |
| -------------- | :----: | --------------------- |
| id             | number | User ID               |
| recording_link | string | User's recording link |

**Response**
| Field   | Type    | Description                          | 
|---------|:-------:|--------------------------------------|
| success | boolean | The result of enrolment's processing |

- __Validating a recording__

```
POST /validate
```

**Request** `POST`

| Parameter      |  Type  | Description           |
| -------------- | :----: | ----------------------|
| id             | number | User ID               |
| recording_link | string | User's recording link |

**Response**
| Field   | Type    | Description                           |
|---------|:-------:|---------------------------------------|
| success | boolean | The result of enrolment's processing  |
| data    | object  | The value contains the accuracy score |

### Example

__Enrolling a user__

Send POST request to http://localhost:8000/enroll with the content:
```json
{
  "id": 123456789, 
  "recording_link": "https://speaker-ver-api-td.s3-ap-southeast-2.amazonaws.com/enrollment.flac"
}
``` 
If this has been successful you should see in the response:
```json
{ 
  "success": true 
}
```

__Validating a recording__

Send a POST request to http://localhost:8000/validate with the content: 

```json
{
  "id": 123456789, 
  "recording_link": "https://speaker-ver-api-td.s3-ap-southeast-2.amazonaws.com/validation.flac"
}
``` 
If this has been successful you should see in the response:
```json
{
  "success": true,
  "data": { 
    "score": 83.34 
  }
}
```
