from config import DevConfig
from flask import Flask
from extensions import db
from blueprints.product.views import product_blueprint
from blueprints.user.views import user_blueprint
from blueprints.token.views import token_blueprint
from models.user import User
from models.product import Product
from sqlalchemy.schema import DropTable

def create_app(config_class=DevConfig):
    """
    Creates app with given config class
    :param config_class:
    :return: flask app object
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register Blueprints
    app.register_blueprint(product_blueprint, url_prefix='/api/v1/')
    app.register_blueprint(user_blueprint, url_prefix='/api/v1/')
    app.register_blueprint(token_blueprint, url_prefix='/api/v1/')

    # Boot up app extensions.
    extensions(app)
    # try:
    #     DropTable(User)
    # except Exception as e:
    #     print(e)

    # Register models
    with app.app_context():
        #db.drop_all()
        db.create_all()
    return app


def extensions(current_app):
    """
    Register 0 or more extensions (mutates the app passed in).
    :param current_app: Flask application instance
    :return: None
    """
    db.init_app(current_app)


app = create_app()


@app.route('/')
def home():
    return('Hollo')


if __name__ == '__main__':
    app.run(debug=True)
