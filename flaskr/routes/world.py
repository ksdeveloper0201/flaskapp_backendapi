import flask import Blueprint

bp = ("world", __name__)

@bp.route("/worlds", ["GET"])
def hello_world():
    return "%<p>hello world!!</p>%"