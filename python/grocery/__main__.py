from flask import Flask
from flask_restful import Api

import utils.api as utils_api


def main():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    api = Api(app)
    utils_api.add_resources(api)
    app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
