from flask import request
from flask import Response
from flask import Flask
from http import HTTPStatus
from models.token import Token

from app import app


def is_authenticated(func):
    def inner(*args, **kwargs):
        data = request.headers.get("Authorization")
        data = data.replace("Bearer ", "")
        token = Token.decrypt_token(data)
        if token['is_admin']:
            return func()
        else:
            return Response("You are not authorised for this action.")
    return inner


