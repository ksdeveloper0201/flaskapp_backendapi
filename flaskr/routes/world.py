from flask import Blueprint, jsonify
from flaskr.exceptions.custom_exception import IsNotFound
from flaskr.responses import api_response
from flaskr.providers.world_provider import WorldProvider

bp = Blueprint("world", __name__)


@bp.route("/", methods=["GET"])
def hello_world():
    return "hello world!"


@bp.route("/city", methods=["GET"])
def get_city():
    """世界の都市情報を取得

    Returns:
        _type_: _description_
    """
    try:
        city_name_list = True
        provider = WorldProvider()
        response = {"message": "Example response"}
        return jsonify(response), 200
    except IsNotFound:
        print(ex)
        return response.not_found()
    except Exception as ex:
        print(ex)
        return api_response.not_find()
