from resources.item import Item, ItemList
from resources.customer import Customer, CustomerList
from resources.purchase import Purchase, PurchaseList


def add_resources(api):
    api.add_resource(Item, "/item/<string:isbn>")
    api.add_resource(ItemList, "/items")
    api.add_resource(Customer, "/customer/<string:ssn>")
    api.add_resource(CustomerList, "/customers")
    api.add_resource(Purchase, "/purchase/<string:id>")
    api.add_resource(PurchaseList, "/purchase")
    return api
