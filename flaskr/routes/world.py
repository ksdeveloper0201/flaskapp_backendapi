from flask import Blueprint

bp = ("world", __name__)


@bp.route("/", ["GET"])
def hello_world():
    return "hello world!"


@bp.route("/world", ["GET"])
def db_world():
    return "db world!"
