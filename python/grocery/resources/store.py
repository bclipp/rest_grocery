from flask_restful import Resource, reqparse
from models.customer import CustomerModel


class Customer(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "ll",
        type=str,
        required=True,
        help="Every store needs a latitude-longitude"
    )
    parser.add_argument(
        "address",
        type=float,
        required=True,
        help="Every customer needs a last_name"
    )
    parser.add_argument(
        "managager_id",
        type=int,
        required=True,
        help="Every customer needs an address."
    )

    def get(self, ll):
        item = CustomerModel.find_by_ll(ll)
        if item:
            return item.json()
        return {"message": "Store is  not found"}, 404

    def post(self, ll):
        if CustomerModel.find_by_ll(ll):
            return (
                {"message": "An store with latitude-longitude '{}' already exists.".format(ll)},
                400,
            )
        data = Customer.parser.parse_args()
        item = CustomerModel(ll,
                             data["address"],
                             data["managager_id"])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the store."}, 500
        return item.json(), 201

    def delete(self, ssn):
        store = CustomerModel.find_by_name(ssn)
        if store:
            store.delete_from_db()
            return {"message": "Store deleted."}
        return {"message": "Store not found."}, 404

    def put(self, ll):
        data = Customer.parser.parse_args()
        store = CustomerModel.find_by_name(ll)
        if store:
            store.price = data["ll"]
        else:
            store = CustomerModel(ll,
                                  data["address"],
                                  data["managager_id"])

        store.save_to_db()

        return store.json()


class CustomerList(Resource):
    def get(self):
        return {"customers": list(map(lambda x: x.json(), CustomerModel.query.all()))}
