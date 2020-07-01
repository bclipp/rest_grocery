from flask_restful import Resource, reqparse
from models.customer import CustomerModel


class Customer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "first_name",
        type=float,
        required=True,
        help="Every customer needs a first_name"
    )
    parser.add_argument(
        "last_name",
        type=float,
        required=True,
        help="Every customer needs a last_name"
    )
    parser.add_argument(
        "address",
        type=int,
        required=True,
        help="Every customer needs an address."
    )
    parser.add_argument(
        "phone_number",
        type=int,
        required=True,
        help="Every customer needs a phone_number."
    )
    parser.add_argument(
        "ssn",
        type=int,
        required=True,
        help="Every customer needs a ssn."
    )

    def get(self, id):
        item = CustomerModel.find_by_id(id)
        if item:
            return item.json()
        return {"message": "Customer not found"}, 404

    def post(self, ssn):
        if CustomerModel.find_by_ssn(ssn):
            return (
                {"message": "An item with ssn '{}' already exists.".format(ssn)},
                400,
            )
        data = Customer.parser.parse_args()
        item = CustomerModel(ssn,
                             data["first_name"],
                             data["last_name"],
                             data["address"],
                             data["phone_number"])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
        return item.json(), 201

    def delete(self, name):
        item = CustomerModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "Item deleted."}
        return {"message": "Item not found."}, 404

    def put(self, name):
        data = Customer.parser.parse_args()

        item = CustomerModel.find_by_name(name)

        if item:
            item.price = data["price"]
        else:
            item = CustomerModel(name, **data)

        item.save_to_db()

        return item.json()


class CustomerList(Resource):
    def get(self):
        return {"items": list(map(lambda x: x.json(), CustomerModel.query.all()))}
