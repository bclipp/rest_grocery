from utils.db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    isbn = db.Column(db.Int(precision=2), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship("StoreModel")

    def __init__(self, name, price, store_id, isbn):
        self.name = name
        self.price = price
        self.store_id = store_id
        self.isbn = isbn

    def json(self):
        return {"name": self.name,
                "price": self.price,
                "store_id": self.store_id,
                "isbn": self.isbn
                }

    @classmethod
    def find_by_isbn(cls, isbn):
        return cls.query.filter_by(isbn=isbn).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
