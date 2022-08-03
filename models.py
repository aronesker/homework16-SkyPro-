from functions import db


class UserRole(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(25), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("user_roles.id"), nullable=False)
    phone = db.Column(db.String(16), unique=True, nullable=False)

    role = db.relationship('UserRole')

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'role': self.role.name,
            'phone': self.phone
        }


class Offer(db.Model):
    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    executor = db.relationship('User')
    order = db.relationship('Order')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.order.name,
            'description': self.order.description,
            'price': self.order.price,
            'executors_first_name': self.executor.first_name,
            'executors_last_name': self.executor.last_name,
        }


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(512), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    customer = db.relationship('User', foreign_keys='Order.customer_id')
    executor = db.relationship('User', foreign_keys='Order.executor_id')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'address': self.address,
            'price': self.price,
            'customers_first_name': self.customer.first_name,
            'customers_last_name': self.customer.last_name,
            'executors_first_name': self.executor.first_name,
            'executors_last_name': self.executor.last_name,
        }
