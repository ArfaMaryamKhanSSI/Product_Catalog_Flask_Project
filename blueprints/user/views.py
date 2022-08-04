from http import HTTPStatus
from flask import request
from blueprints.user import user_blueprint
from models.user import User
from datetime import datetime
from flask import Response
import json
from models.token import Token
import jwt


@user_blueprint.route("user/", methods=["GET"], endpoint="get-user")
def user():
    """
    Gets all products from db if no input specified else returns the specified product
    """
    pid = request.args.get('id')
    if pid:
        user_t = User.get_user(pid)
        user_t.date_added = str(user_t.date_added)
        user_dict = user_t.to_dict()
        return Response(json.dumps(user_dict), HTTPStatus.OK)
    user_dict = []
    user_t = User.get_all_users()
    for each_user in user_t:
        each_user.date_added = str(each_user.date_added)
        temp_user = each_user.to_dict()
        user_dict.append(temp_user)
    return Response(json.dumps(user_dict), HTTPStatus.OK)


@user_blueprint.route("user/", methods=["POST"], endpoint="post-user")
def user():
        try:
            body = request.json
            user_t = User()
            user_t.age = body["age"]
            user_t.name = body["name"]
            user_t.is_admin = body["is_admin"]
            user_t.email = body["email"]
            user_t.password = body["password"]
            user_t.date_added = datetime.utcnow()
            user_t.save()

            data = {
                "email": user_t.email,
                "id": user_t.id,
                "is_admin": user_t.is_admin
            }

            Token.encrypt_token(data)
            return Response("Created", HTTPStatus.CREATED)
        except:
            return Response("User could not be added.")


@user_blueprint.route("user/", methods=["DELETE"], endpoint="delete-user")
def user():
        try:
            pid = request.args.get('id')
            user_t = User.delete_user(pid)
            return Response("Deleted", HTTPStatus.OK)
        except:
            return Response("User does not exist.")


@user_blueprint.route("user/", methods=["PUT"], endpoint="put-user")
def user():
    try:
        pid = request.args.get('id')
        user_t = User.get_user(pid)
        body = request.json
        user_t.email = body.get('email', user_t.email)
        user_t.password = body.get('password', user_t.password)
        user_t.age = body.get('age', user_t.age)
        user_t.name = body.get('name', user_t.name)
        user_t.is_admin = body.get('is_admin', user_t.is_admin)
        user_t.save()
        return Response("Updated", HTTPStatus.OK)
    except:
        return Response("Could not update.")
