from flask_restful import Resource, reqparse
from models.item import ItemModel


class Purchase(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "customer_id",
        type=float,
        required=True,
        help="Every item needs a price."
    )
    parser.add_argument(
        "items_id",
        type=int,
        required=True,
        help="Every item needs an isbn."
    )
    parser.add_argument(
        "store_id",
        type=int,
        required=True,
        help="Every item needs a store_id."
    )
    parser.add_argument(
        "date",
        type=int,
        required=True,
        help="Every item needs a store_id."
    )

    def get(self, isbn):
        item = ItemModel.find_by_isbn(isbn)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, isbn):
        if ItemModel.find_by_isbn(isbn):
            return (
                {"message": "An item with name '{}' already exists.".format(isbn)},
                400,
            )
        data = Item.parser.parse_args()
        item = ItemModel(isbn,
                         data["name"],
                         data["price"],
                         data["store_id"])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
        return item.json(), 201

    def delete(self, isbn):
        item = ItemModel.find_by_name(isbn)
        if item:
            item.delete_from_db()
            return {"message": "Item deleted."}
        return {"message": "Item not found."}, 404

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item:
            item.price = data["price"]
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json()


class PurchaseList(Resource):
    def get(self):
        return {"purchases": list(map(lambda x: x.json(), ItemModel.query.all()))}
