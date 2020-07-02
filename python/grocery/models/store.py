from utils.db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    ll = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    managager_id = db.Column(db.Int(precision=2), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)

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
