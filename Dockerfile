# starting point for the python application
FROM python:3.8-slim-buster

# install the application and python deps
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# set the timezone
ENV TZ=America/Los_Angeles

# copy over the application package
COPY caesar caeser

EXPOSE 5000
ENTRYPOINT gunicorn --workers=5 --bind=0.0.0.0:5000 caesar:app --reload