from os import getenv
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET')
app.config['UPLOAD_FOLDER'] = getenv('UPLOADS_FOLDER')
app.config['MAX_CONTENT_LENGTH'] = 10 * 1000 * 1000


@app.route('/')
def get_home():
    return "Hello Caesar"
