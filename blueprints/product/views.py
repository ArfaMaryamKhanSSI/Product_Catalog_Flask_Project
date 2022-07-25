from http import HTTPStatus

from flask import request
from blueprints.product import product_blueprint
from models.product import Product
from datetime import datetime
from flask import Response
import json

@product_blueprint.route("product/", methods=["GET", "POST"])
def product():
    if request.method == "GET":
        name = request.args.get('name')
        product = Product.get_product(name=name)
        product.date_added = str(product.date_added)
        product_dict = product.to_dict()
        return Response(json.dumps(product_dict), HTTPStatus.OK)
    if request.method == "POST":
        body = request.json
        product = Product()
        product.price = body["price"]
        product.name = body["name"]
        product.date_added = datetime.utcnow()
        product.save()
        return Response("Created", status=HTTPStatus.CREATED)
