from http import HTTPStatus
from flask import request
from blueprints.token import token_blueprint
from models.token import Token
from datetime import datetime
from flask import Response
import json


@token_blueprint.route("token/", methods=["GET"], endpoint="get-token")
def token():
    """
    Gets all products from db if no input specified else returns the specified product
    """
    pid = request.args.get('id')
    if pid:
        token_t = Token.get_token(pid)
        token_dict = token_t.to_dict()
        return Response(json.dumps(token_dict), HTTPStatus.OK)
    token_dict = []
    token_t = Token.get_all_tokens()
    for each_token in token_t:
        token_temp = each_token.to_dict()
        token_dict.append(token_temp)
    return Response(json.dumps(token_dict), HTTPStatus.OK)


@token_blueprint.route("token/", methods=["DELETE"], endpoint="delete-token")
def token():
    try:
        pid = request.args.get('id')
        token_t = Token.delete_token(pid)
        return Response("Deleted", HTTPStatus.OK)
    except:
        return Response("Token does not exist.")

# {
#     "age": 20,
#     "name": "Arfa",
#     "email":"arfa@gmail.com",
#     "password":"abc123",
#     "is_admin": true
# }