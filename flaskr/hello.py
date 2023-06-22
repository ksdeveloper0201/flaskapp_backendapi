from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"


@app.route("/kiyo")
def hello_kiyo():
    return "<p>Hello, kiyo!</p>"


@app.route("/<name>")
def hello(name):
    return f"<p>Hello, {name}!</p>"


@app.route("/index")
def hello_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
