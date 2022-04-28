# Caesar 🍹

[Flask](https://flask.palletsprojects.com/en/2.0.x/) web server that handles "heavy" tasks asynchronously via [Celery](https://docs.celeryproject.org/en/stable/index.html).

## Why did you make this?

Another project I was working on needed to be able to crunch a bunch of data, and email a report out.
Requests to the route using this function were sluggish, so I wanted to implement a task-queue in Flask, and this was the easiest solution I found.

## When would you want this?

1. When dealing with mass email sends / a high volume of singular email sends
2. When doing large multi-step operations like deleting a large number of records or preparing a data export
3. etc, etc, etc.

## Getting Started

There are a few things you're going to have to do regardless of if you're running the app in production, or development mode.

1. create a `.env` file in the root directory, and set the `REDIS_PASS` value (see .env.example)
2. run `docker-compose build` to build everything

### Development Mode

Run the command `docker-compose up caeser_dev redis`, this will start the dev server, and a redis cache

### Production Mode

Run the command `docker-compose up caeser_prod redis`, this will start the prod server, and a redis cache.


## Questions?
create an issue!