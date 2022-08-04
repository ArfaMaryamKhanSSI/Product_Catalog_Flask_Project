from extensions import db
from models.model_mixins import ModelMixins


class User(db.Model, ModelMixins):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)

    @classmethod
    def get_user(cls, pid):
        response = cls.query.get(pid)
        return response

    @classmethod
    def get_all_users(cls):
        response = cls.query.all()
        return response

    @classmethod
    def delete_user(cls, pid):
        response = cls.query.get(pid)
        response.delete()
