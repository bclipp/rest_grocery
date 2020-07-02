from utils.db import db


class PurchaseModel(db.Model):
    __tablename__ = "purchases"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    items_id = db.Column(db.Integer)
    store_id = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    uccpid = db.Column(db.Integer)
    final_cost = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))

    store = db.relationship("StoreModel")
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    item = db.relationship("ItemModel")
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    customer = db.relationship("CustomerModel")

    def __init__(self,
                 customer_id,
                 items_id,
                 store_id,
                 date,
                 uccpid,
                 final_cost):
        self.customer_id = customer_id
        self.items_id = items_id
        self.store_id = store_id
        self.date = date,
        self.uccpid = uccpid,
        self.final_cost = final_cost

    def json(self):
        return {"customer_id": self.customer_id,
                "items_id": self.items_id,
                "store_id": self.store_id,
                "date": self.date,
                "uccpid": self.uccpid,
                "final_cost": self.final_cost
                }

    @classmethod
    def find_by_uccpid(cls, uccpid):
        return cls.query.filter_by(uccpid=uccpid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
