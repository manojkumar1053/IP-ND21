from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'yo'


@app.route('/')
def candy():
    return 'chocolate'


@app.route('/')
def greeting():
    return 'hello!'

# Running Test Server on Window CMD
# export FLASK_APP=app.py
# flask run --host 0.0.0.0 --port 3000 --reload
