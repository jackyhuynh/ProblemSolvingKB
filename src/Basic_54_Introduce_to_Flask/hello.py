from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye():
    return 'Bye, World!'


@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"


@app.route('/<path:name>')
def greet1(name):
    return f"Hello {name}!"


@app.route('/username/<path:name>'/'<int:number>')
def greet2(name):
    return f"Hello {name}!"


"""
Python decorator:
decorator is a wrapper function that give a function another functionality
"""
if __name__ == "__main__":
    app.run(debug=True)  #  turn on the debug mode
