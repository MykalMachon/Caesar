# python std libs
from os import getenv
from time import sleep

# third party libs
from flask import Flask
from celery import Celery

# basic flask setup
app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET')

# setup celery
redis_conn_str = f"redis://:{getenv('REDIS_PASS')}@redis:6379/0"
celery = Celery(app.name, broker=redis_conn_str)


@app.route('/')
def get_home():
    return "Hello Caesar"


@app.route('/email', methods=['POST'])
def post_email():
    async_send_email.delay('hello world')
    return "should send email..."


@celery.task
def async_send_email(msg: str):
    print('going to send email')
    sleep(3)
    print(f'email was sent: {msg}')
