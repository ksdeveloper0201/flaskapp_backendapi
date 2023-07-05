from flask import Flask, make_response


def api_response(response, status_code):
    response.status_code = status_code
    response.headers["Content-Type"] = "application/json;charset=UTF8"
    return response


def success(body):
    response = make_response(body)
    return api_response(response=response, status_code=200)


def handle_exception(error):
    error_response = make_response(str(error))
    return api_response(error_response, response=404)
