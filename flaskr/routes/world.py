from flask import Blueprint

bp = Blueprint("world", __name__)


@bp.route("/", methods=["GET"])
def hello_world():
    return "hello world!"


@bp.route("/world", methods=["GET"])
def db_world():
    return "db world!"
