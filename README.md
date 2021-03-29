# speaker-verification-api
Speaker Verification API Based on Django. The Django image is based on ubuntu:20.04 Docker image. 

### Running the project

 - Install [docker-compose](https://docs.docker.com/compose/install/) on your computer. 
 - Copy .env.db.dev.sample & .env.dev.sample files from sample_envs to project root. Remove .sample at the end of the file extensions.
 - Populate POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB in .env.db.dev - Choose any user name and password. Copy these values to the corresponding fields in: .env.dev POSTGRES_USER=SQL_USER, POSTGRES_DB=SQL_DATABASE, POSTGRES_PASSWORD=SQL_PASSWORD.
 - Populate SECRET_KEY in .env.dev - You can generate a key with the following Python command *`python3 -c 'import random; result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]); print(result)'`*
 - Run *`docker-compose -f docker-compose.yml up -d --build`*
 - To verify the project is running, visit: [http://localhost:8000](http://localhost:8000) on your development machine. You should see: *The install worked successfully! Congratulations!*