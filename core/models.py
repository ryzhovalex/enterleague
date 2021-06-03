""" 
Database models logic.
"""
from . import db


# CONSTRAINT EXAMPLE: https://www.youtube.com/watch?v=lnfrcHdE_HI
# check = db.Column(db.Integer, db.CheckConstraint("check<5"))

# source: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# many-to-many table
user_addresses_table = db.Table("user_addresses", 
    db.Column("address_id", db.Integer, db.ForeignKey("address.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # one-to-one connection, because 'uselist=False'
    account = db.relationship("Account", backref="user", lazy=True, uselist=False)
    # 'backref="user"' means that by calling 'Account.user' we will get this User instance

    # one-to-many connection
    order = db.relationship("Order", backref="user", lazy=True)

    # many-to-many connection
    addresses = db.relationship("Address", secondary=user_addresses_table, lazy="subquery", backref=db.backref("users_residents", lazy=True))
    # 'secondary' is a pointer to a table with Users and their Addresses

    def __repr__(self):
        return "<User %r>" % self.name


class Account(db.Model):
    """ One-to-one with User """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False) # chain Account to owner-user by defining foreign key with User id
    nickname = db.Column(db.String(80), nullable=False)


class Order(db.Model):
    """ One-to-many with User (1 user => many orders) """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False) 
    name = db.Column(db.String(80), nullable=False)


class Address(db.Model):
    """ Many-to-many with User """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
