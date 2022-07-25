from flask import request
from blueprints.product import product_blueprint
from models.product import Product
from datetime import datetime


@product_blueprint.route("product/", methods=["GET", "POST"])
def product():
    if request.method == "GET":

        return "hello from GET product"
    if request.method == "POST":
        body = request.json
        product = Product()
        product.price = body["price"]
        product.name = body["name"]
        product.date_added = datetime.utcnow()
        product.save()
        return "success"
