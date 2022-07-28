import models
from functions import db
from flask import current_app as app, jsonify


@app.route('/users', methods=['GET'])
def get_users():
    users = db.session.query(models.User).all()

    return jsonify([user.serialize() for user in users])