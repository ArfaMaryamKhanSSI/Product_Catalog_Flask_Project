from extensions import db
from models.model_mixins import ModelMixins
from models.token import Token


class Product(db.Model, ModelMixins):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)

    @classmethod
    def get_product(cls, pid):
        response = cls.query.get(pid)
        return response

    @classmethod
    def get_all_products(cls):
        response = cls.query.all()
        return response

    @classmethod
    def delete_product(cls, pid):
        response = cls.query.get(pid)
        response.delete()




