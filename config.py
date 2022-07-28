import os.path

DATA_BASE_DIR = 'data'


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USER_ROLES_DATA_PATH = os.path.join(DATA_BASE_DIR, 'users_roles.json')
    USERS_DATA_PATH = os.path.join(DATA_BASE_DIR, 'users.json')
    OFFERS_DATA_PATH = os.path.join(DATA_BASE_DIR, 'offers.json')
    ORDERS_DATA_PATH = os.path.join(DATA_BASE_DIR, 'orders.json')