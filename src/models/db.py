""" SQLAlchemy database representation """

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class Database:
    """ Singleton database class. If create more than one instance, throw an error. """
    instance = None
    db = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
            cls.db = SQLAlchemy()
        return cls.instance 

    @classmethod
    def migrate(cls, app):
        # source: https://github.com/miguelgrinberg/flask-migrate
        migrate = Migrate(app, cls.db)

    @classmethod
    def get(cls):
        return cls.db

    @classmethod
    def init_app(cls, app):
        cls.db.init_app(app) 

    @classmethod
    def add(cls, entity):
        cls.db.session.add(entity)

    @classmethod
    def commit(cls):
        cls.db.session.commit()


    
