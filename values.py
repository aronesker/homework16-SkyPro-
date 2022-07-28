import json
from functions import db
import models
from sqlalchemy.sql import exists
import re
from datetime import datetime


DATE_PATTERN = re.compile(r"\d{2}/\d{2}/\d{4}")


def load_data(file_path):
    """
    Загружает содержимое файла
    :param file_path: путь к файлы
    :return: данные из файла
    """
    with open(file_path) as file:
        content = json.load(file)

    return content


def add_user_roles(data_path):
    """
    Загружает данные в таблицу "roles"
    :param data_path: путь к файлу с данными
    """
    data_content = load_data(data_path)

    for role in data_content:

        if db.session.query(exists().where(models.UserRole.id == role['id'])) is False:
            new_role = models.UserRole(**role)  # id=role['id'], name=role['name']
            db.session.add(new_role)

    db.session.commit()


def add_users(data_path):
    """
    Загружает данные в таблицу "users"
    :param data_path: путь к файлу с данными
    """
    data_content = load_data(data_path)

    for user in data_content:

        if db.session.query(models.User).filter(models.User.id == user['id']).first() is None:
            new_role = models.User(**user)
            db.session.add(new_role)

    db.session.commit()


def add_offers(data_path):
    """
        Загружает данные в таблицу "offers"
        :param data_path: путь к файлу с данными
    """
    data_content = load_data(data_path)

    for offer in data_content:

        if db.session.query(models.Offer).filter(models.Offer.id == offer['id']).first() is None:
            new_role = models.Offer(**offer)
            db.session.add(new_role)

    db.session.commit()


def add_orders(data_path):
    """
        Загружает данные в таблицу "orders"
        :param data_path: путь к файлу с данными
    """
    data_content = load_data(data_path)

    for order in data_content:

        for field_name, field_value in order.items():
            if isinstance(field_value, str) and re.search(DATE_PATTERN, field_value):
                order[field_name] = datetime.strptime(field_value, '%m/%d/%Y').date()

        if db.session.query(models.Order).filter(models.Order.id == order['id']).first() is None:
            new_role = models.Order(**order)
            db.session.add(new_role)

    db.session.commit()

