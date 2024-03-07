from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! Is it working?</p>"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
