from flask_sqlalchemy import SQLAlchemy


def create_tables():
    db = SQLAlchemy()
    db.create_all()


def init():
    db = SQLAlchemy()
    return db
