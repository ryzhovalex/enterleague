""" 
Database models logic.
"""

from .model_aliases import *


# source: https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# many-to-many table
players_roles_table = table("players_roles", 
    column("player_id", integer(), foreign_key("player.id"), primary_key=True),
    column("role_id", integer(), foreign_key("role.id"), primary_key=True)
)
players_perks_table = table("players_perks", 
    column("player_id", integer(), foreign_key("player.id"), primary_key=True),
    column("perk_id", integer(), foreign_key("perk.id"), primary_key=True)
)
players_trophies_table = table("players_trophies", 
    column("player_id", integer(), foreign_key("player.id"), primary_key=True),
    column("trophie_id", integer(), foreign_key("trophie.id"), primary_key=True)
)
clubs_trophies_table = table("clubs_trophies", 
    column("club_id", integer(), foreign_key("club.id"), primary_key=True),
    column("trophie_id", integer(), foreign_key("trophie.id"), primary_key=True)
)


class Player(model()):
    __table_args__ = (
        check_constraint("age >= 6 AND age <= 60"),
    )
    id = column(integer(), primary_key=True)
    firstname = column(string(80), nullable=False)
    surname = column(string(80), nullable=False)
    country_id = column(integer(), foreign_key("country.id"), nullable=False) # every Player has only one country 
    age = column(integer(), nullable=False)
    roles = relationship("Role", secondary=players_roles_table, lazy="subquery", backref=backref("players", lazy=True))
    skills = relationship("Skill", backref="player", lazy=True)
    perks = relationship("Perk", secondary=players_perks_table, lazy="subquery", backref=backref("players", lazy=True))
    club_id = column(integer(), foreign_key("club.id"), nullable=False) 


class Country(model()):
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False)
    players = relationship("Player", backref="country", lazy=True)
    clubs = relationship("Club", backref="country", lazy=True)


class Role(model()):
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False)


class Skill(model()):
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False)
    rating = column(integer(), nullable=False)


class Perk(model()):
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False)


class Club(model()):
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False)
    country_id = column(integer(), foreign_key("country.id"), nullable=False) 
    rating = column(integer(), nullable=False)
    budget = column(integer(), nullable=False)
    market_value = column(integer(), nullable=False)
    players = relationship("Player", backref="club", lazy=True)
    trophies = relationship("Trophie", secondary=clubs_trophies_table, lazy="subquery", backref=backref("clubs", lazy=True))
    
    

# class User(model()):
#     id = column(integer(), primary_key=True)
#     name = column(string(80), unique=True, nullable=False)
#     age = column(integer(), nullable=False)

#     # one-to-one connection, because 'uselist=False'
#     account = db.relationship("Account", backref="user", lazy=True, uselist=False)
#     # 'backref="user"' means that by calling 'Account.user' we will get this User instance

#     # one-to-many connection
#     order = db.relationship("Order", backref="user", lazy=True)

#     # many-to-many connection
#     addresses = db.relationship("Address", secondary=user_addresses_table, lazy="subquery", backref=backref("users_residents", lazy=True))
#     # 'secondary' is a pointer to a table with Users and their Addresses

#     def __repr__(self):
#         return "<User %r>" % self.name


# class Account(model()):
#     """ One-to-one with User """
#     id = column(integer(), primary_key=True)
#     user_id = column(integer(), foreign_key("user.id"), nullable=False) # chain Account to owner-user by defining foreign key with User id
#     nickname = column(string(80), nullable=False)


# class Order(model()):
#     """ One-to-many with User (1 user => many orders) """
#     id = column(integer(), primary_key=True)
#     user_id = column(integer(), foreign_key("user.id"), nullable=False) 
#     name = column(string(80), nullable=False)


# class Address(model()):
#     """ Many-to-many with User """
#     id = column(integer(), primary_key=True)
#     name = column(string(80), nullable=False)
