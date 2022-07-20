from crypt import methods

from flask import request
from blueprints.product import product_blueprint

@product_blueprint.route("product/", methods= ["GET", "POST"])
def product():
    if request.method == "GET":
        return "hello from GET product"
    if request.method == "POST":
        return "hello from POST product"
