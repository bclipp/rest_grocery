from resources.item import Item, ItemList
from resources.customer import Customer, CustomerList


def add_resources(api):
    api.add_resource(Item, "/item/<string:name>")
    api.add_resource(ItemList, "/items")
    api.add_resource(Customer, "/customer/<string:name>")
    api.add_resource(CustomerList, "/customers")
    return api
