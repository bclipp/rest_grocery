from flask import Flask
from flask_restful import Api

import utils.db as utils_db
from resources.managers import Manager, ManagerList
# from resources.items import items
# from resources.customers import customers
# from resources.purchases import purchases
# from resources.stores import stores


def main():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    api = Api(app)
    # by id or list them all
    # for all
    api.add_resource(Manager, "/managers/<int:id>")
    api.add_resource(ManagerList, "/managers/")
    # api.add_resource(items, "/items/<string:name>")
    # api.add_resource(customers, "/customers/<string:name>")
    # api.add_resource(purchases, "/purchases/<string:name>")
    # api.add_resource(stores, "/stores/<string:name>")
    db = utils_db.init()
    db.init_app(app)
    app.run(host='0.0.0.0', debug=True)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    main()
