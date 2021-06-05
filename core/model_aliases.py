""" Program with aliases for more comfortable and shorter model building. """

from . import db


def model():
    return db.Model


def column(*args, **kwargs):
    return db.Column(*args, **kwargs)


def integer(*args, **kwargs):
    return db.Integer(*args, **kwargs)


def string(*args, **kwargs):
    return db.String(*args, **kwargs)


def boolean(*args, **kwargs):
    return db.Boolean(*args, **kwargs)


def relationship(*args, **kwargs):
    return db.relationship(*args, **kwargs)


def foreign_key(*args, **kwargs):
    return db.ForeignKey(*args, **kwargs)


def backref(*args, **kwargs):
    return db.backref(*args, **kwargs)


def table(*args, **kwargs):
    return db.Table(*args, **kwargs)


def check_constraint(*args, **kwargs):
    return db.CheckConstraint(*args, **kwargs)

