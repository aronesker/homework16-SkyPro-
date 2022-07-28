from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():

        import routes

        #db.drop_all()
        db.create_all()

        import values

        values.add_user_roles(app.config['USER_ROLES_DATA_PATH'])
        values.add_users(app.config['USERS_DATA_PATH'])
        values.add_offers(app.config['OFFERS_DATA_PATH'])
        values.add_orders(app.config['ORDERS_DATA_PATH'])

        return app
