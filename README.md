
# speaker-verification-api

Speaker Verification API Based on Django. The Django image is based on ubuntu:20.04 Docker image.

  

### Running the project

  

- Install [docker-compose](https://docs.docker.com/compose/install/) on your computer.

- Copy .env.dev.db.sample & .env.dev.sample files from sample_envs to project root. Remove .sample at the end of the file extensions.

- Populate POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB in .env.dev.db - Choose any user name and password. Copy these values to the corresponding fields in: .env.dev POSTGRES_USER=SQL_USER, POSTGRES_DB=SQL_DATABASE, POSTGRES_PASSWORD=SQL_PASSWORD.

- Populate SECRET_KEY in .env.dev - You can generate a key with the following Python command *`python3 -c 'import random; result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]); print(result)'`*

- Run *`docker-compose -f docker-compose.yml up -d --build`*

  

### Testing the project

  
#### Enrolling a user
- Submit a POST request to http://localhost:8000/enroll with the content: `{"id": 123456789, "recording_link": "https://speaker-ver-api-td.s3-ap-southeast-2.amazonaws.com/enrollment.flac"}` - If this has been successful you should see `{ "success": true }`.

#### Validating a recording
- Submit a POST request to http://localhost:8000/validate with the content: `{"id": 123456789, "recording_link": "https://speaker-ver-api-td.s3-ap-southeast-2.amazonaws.com/validation.flac"}` - If this has been successful you should see `{"success": true,"data": { "score": 83.34 }}`.