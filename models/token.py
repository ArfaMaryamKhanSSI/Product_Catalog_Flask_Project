from extensions import db
from models.model_mixins import ModelMixins
from models.user import User
import datetime
import jwt

SECRET_KEY = "python_jwt"


class Token(db.Model, ModelMixins):
    id = db.Column(db.Integer, primary_key=True)
    jwt_token = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    @classmethod
    def get_token(cls, pid):
        response = cls.query.get(pid)
        return response.jwt_token

    @classmethod
    def get_all_tokens(cls):
        response = cls.query.all()
        return response

    @classmethod
    def delete_token(cls, pid):
        response = cls.query.get(pid)
        response.delete()

    @classmethod
    def encrypt_token(cls, data):
        encode_data = jwt.encode(payload=data, key=SECRET_KEY, algorithm="HS256")
        token_t = Token()
        token_t.jwt_token = encode_data
        token_t.user_id = data["id"]

        token_t.save()

    @classmethod
    def decrypt_token(cls, token):
        decode_data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms="HS256")
        return decode_data





