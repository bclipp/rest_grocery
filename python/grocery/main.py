from flask import Flask
from flask_restful import Api

import utils.db as utils_db
from resources.manager import ManagerRegister

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
    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    app.run(host='0.0.0.0', debug=True)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    main()
