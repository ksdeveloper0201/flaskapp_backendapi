from flask import Blueprint
from flask import Flask
# from flask import render_template8
from app_factory import create_app
# from flaskr.database.database import db

app = Flask(__name__)
create_app(app)

# blueprintの記述

bp = Blueprint("world", __name__)


@bp.route("/", ["GET"])
def hello_world():
    return "hello world!"


@bp.route("/world", ["GET"])
def db_world():
    return "db world!"
# blueprintの記述ここまで


app.register_blueprint(bp)

if __name__ == "__main__":
    app.run()
