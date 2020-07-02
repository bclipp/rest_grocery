from flask_restful import Resource, reqparse
from models.purchase import PurchaseModel


class Purchase(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "customer_id",
        type=int,
        required=True,
        help="Every purchase needs a customer_id."
    )
    parser.add_argument(
        "items_id",
        type=int,
        required=True,
        help="Every purchase needs an items_id."
    )
    parser.add_argument(
        "store_id",
        type=int,
        required=True,
        help="Every purchase needs a store_id."
    )
    parser.add_argument(
        "date",
        type=str,
        required=True,
        help="Every purchase needs a date."
    )
    parser.add_argument(
        "uccpid",
        type=int,
        required=True,
        help="Every purchase needs a uccpid."
    )

    parser.add_argument(
        "final_cost",
        type=int,
        required=True,
        help="Every purchase needs a final_cost."
    )

    def get(self, uccpid):
        item = PurchaseModel.find_by_uccpid(uccpid)
        if item:
            return item.json()
        return {"message": "Purchase not found"}, 404

    def post(self, uccpid):
        if PurchaseModel.find_by_uccpid(uccpid):
            return (
                {"message": "A purchase with name '{}' already exists.".format(uccpid)},
                400,
            )
        data = Purchase.parser.parse_args()
        purchase = PurchaseModel(uccpid,
                                 data["customer_id"],
                                 data["items_id"],
                                 data["store_id"],
                                 data["date"],
                                 data["final_cost"])
        try:
            purchase.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
        return purchase.json(), 201

    def delete(self, uccpid):
        purchase = PurchaseModel.find_by_uccpid(uccpid)
        if purchase:
            purchase.delete_from_db()
            return {"message": "Purchase deleted."}
        return {"message": "Purchase not found."}, 404

    def put(self, uccpid):
        data = Purchase.parser.parse_args()
        purchase = PurchaseModel.find_by_uccpid(uccpid)
        if purchase:
            purchase.price = data["uccpid"]
        else:
            purchase = PurchaseModel(uccpid,
                                 data["customer_id"],
                                 data["items_id"],
                                 data["store_id"],
                                 data["date"],
                                 data["final_cost"])
        purchase.save_to_db()

        return purchase.json()


class PurchaseList(Resource):
    def get(self):
        return {"purchases": list(map(lambda x: x.json(), PurchaseModel.query.all()))}
