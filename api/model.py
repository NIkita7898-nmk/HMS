from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(80), nullable=False)
    l_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), nullable=True)
    phone_no = db.Column(db.Numeric(10, 0), nullable=True)

    def __repr__(self) -> str:
        return super().__repr__()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.Numeric(10,2), nullable=False)

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_no = db.Column(db.Integer, nullable=False)
    check_in = db.Column(db.DateTime, nullable=False)
    check_out = db.Column(db.DateTime, nullable=False)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_no = db.Column(db.Integer, nullable=False)
    room_type = db.Column(db.String(80), nullable=False)
    room_price = db.Column(db.Numeric(10,2), nullable=False)
    room_availability = db.Column(db.String(80), nullable=False)

class Allocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    check_in_time = db.Column(db.DateTime, nullable=False)
    check_out_time = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Numeric(10,2), nullable=False)
    paid_amount = db.Column(db.Numeric(10,2), nullable=False)
    balance = db.Column(db.Numeric(10,2), nullable=False)
    status = db.Column(db.String(80), nullable=False)
    payment_method = db.Column(db.String(80), nullable=False)
    payment_status = db.Column(db.String(80), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
