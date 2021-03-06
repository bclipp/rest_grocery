from utils.db import db


class CustomerModel(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    ssn = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80), nullable=False)

    def __init__(self, ssn, first_name, last_name, address, phone_number):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number

    def json(self):
        return {"ssn": self.ssn,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "address": self.address,
                "phone_number": self.phone_number}

    @classmethod
    def find_by_ssn(cls, ssn):
        return cls.query.filter_by(name=ssn).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
