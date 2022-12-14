from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World - Docker in VS Code!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# The if __name__ == '__main__': statement is boilerplate code that's very often used in Python to invoke the main function of a file. 