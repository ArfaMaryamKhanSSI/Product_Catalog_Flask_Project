from http import HTTPStatus
from flask import request
from blueprints.product import product_blueprint
from models.product import Product
from datetime import datetime
from flask import Response
import json
from blueprints.utils import is_authenticated


@product_blueprint.route("product/", methods=["GET"], endpoint="get-product")
def product():
    """
    Gets all products from db if no input specified else returns the specified product
    """
    pid = request.args.get('id')
    if pid:
        product_t = Product.get_product(pid)
        product_t.date_added = str(product_t.date_added)
        product_dict = product_t.to_dict()
        return Response(json.dumps(product_dict), HTTPStatus.OK)
    product_dict = []
    product_t = Product.get_all_products()
    for each_prod in product_t:
        each_prod.date_added = str(each_prod.date_added)
        prod = each_prod.to_dict()
        product_dict.append(prod)
    return Response(json.dumps(product_dict), HTTPStatus.OK)


@product_blueprint.route("product/", methods=["POST"], endpoint="post-product")
@is_authenticated
def product():
    body = request.json
    product_t = Product()
    product_t.price = body["price"]
    product_t.name = body["name"]
    product_t.date_added = datetime.utcnow()
    product_t.save()
    return Response("Created", HTTPStatus.CREATED)


@product_blueprint.route("product/", methods=["DELETE"], endpoint="delete-product")
@is_authenticated
def product():
    pid = request.args.get('id')
    product_t = Product.delete_product(pid)
    return Response("Deleted", HTTPStatus.OK)


@product_blueprint.route("product/", methods=["PUT"], endpoint="put-product")
@is_authenticated
def product():
    pid = request.args.get('id')
    product_t = Product.get_product(pid)
    body = request.json
    product_t.price = body.get('price', product_t.price)
    product_t.name = body.get('name', product_t.name)
    product_t.save()
    return Response("Updated", HTTPStatus.OK)


# {
#     "age": 20,
#     "name": "Arfa",
#     "email":"arfa@gmail.com",
#     "password":"abc123",
#     "is_admin": true
# }

# {
#     "price": 260,
#     "name": "Wafers"
# }


#usdt
#dates guy pays XD
#plots