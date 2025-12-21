from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "\
        <h1>Hello World!</h1> \
        <p>Welcome to my first Flask App</p> \
        </br> \
        <h2>This is my first Flask application.</h2> \
        <p>Flask is a lightweight WSGI web application framework in Python.</p> \
        "

if __name__ == '__main__':
    app.run(debug=True)