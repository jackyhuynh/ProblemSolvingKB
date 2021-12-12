from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

"""
Python decorator: 
"""
# if __name__= "__main__":
