from flask_sqlalchemy import SQLAlchemy


def init():
    db = SQLAlchemy()
    return db
