from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Pemo says, it's cool, man!"
