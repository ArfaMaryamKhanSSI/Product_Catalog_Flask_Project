from extensions import db
from models.model_mixins import ModelMixins


class Product(db.Model, ModelMixins):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)
