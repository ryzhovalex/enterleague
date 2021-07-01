""" 
Database models logic.
"""

from .db import Database


db = Database().get()


def model():
    return db.Model


def column(*args, **kwargs):
    return db.Column(*args, **kwargs)


def integer(*args, **kwargs):
    return db.Integer(*args, **kwargs)


def boolean(*args, **kwargs):
    return db.Boolean(*args, **kwargs)


def string(*args, **kwargs):
    return db.String(*args, **kwargs)


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


def text(*args, **kwargs):
    return db.Text(*args, **kwargs)


def dtime(*args, **kwargs): # name 'dtime' used because we may have conflicts with python origin 'datetime'
    return db.DateTime(*args, **kwargs)

    
# source: https://flask-sqlalchemy.palletsprojects.com/en/2.x/model()s/
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
player_match_histories_matches_table = table("player_match_histories_matches", 
    column("player_match_history_id", integer(), foreign_key("player_match_history.id"), primary_key=True),
    column("match_id", integer(), foreign_key("match.id"), primary_key=True)
)
club_match_histories_matches_table = table("club_match_histories_matches", 
    column("club_match_history_id", integer(), foreign_key("club_match_history.id"), primary_key=True),
    column("match_id", integer(), foreign_key("match.id"), primary_key=True)
)
championship_match_histories_matches_table = table("championship_match_histories_matches", 
    column("championship_match_history_id", integer(), foreign_key("championship_match_history.id"), primary_key=True),
    column("match_id", integer(), foreign_key("match.id"), primary_key=True)
)
player_transfer_histories_transfers_table = table("player_transfer_histories_transfers", 
    column("player_transfer_history_id", integer(), foreign_key("player_transfer_history.id"), primary_key=True),
    column("transfer_id", integer(), foreign_key("transfer.id"), primary_key=True)
)
club_transfer_histories_transfers_table = table("club_transfer_histories_transfers", 
    column("club_transfer_history_id", integer(), foreign_key("club_transfer_history.id"), primary_key=True),
    column("transfer_id", integer(), foreign_key("transfer.id"), primary_key=True)
)
season_transfer_histories_transfers_table = table("season_transfer_histories_transfers", 
    column("season_transfer_history_id", integer(), foreign_key("season_transfer_history.id"), primary_key=True),
    column("transfer_id", integer(), foreign_key("transfer.id"), primary_key=True)
)
clubs_matches_table = table("clubs_matches", 
    column("club_id", integer(), foreign_key("club.id"), primary_key=True),
    column("match_id", integer(), foreign_key("match.id"), primary_key=True)
)
championships_types_table = table("championships_types", 
    column("championship_id", integer(), foreign_key("championship.id"), primary_key=True),
    column("championship_type_id", integer(), foreign_key("championship_type.id"), primary_key=True)
)


class NamesCollection(model()):
    __tablename__ = "names_collection"
    id = column(integer(), primary_key=True)
    name_type = column(string(25)) # 'first' or 'sur'
    name = column(string(80))
    proto_countries = column(text())


class ChampionshipsCollection(model()):
    __tablename__ = "championship_collection"
    id = column(integer(), primary_key=True)
    name = column(string(80))
    is_national = column(boolean(), default=False) # for national teams or not
    is_league = column(boolean(), default=False) # is part of country' division or not
    country_id = column(integer(), foreign_key("country.id"), nullable=False) # every Championship has only one country 


class Player(model()):
    __tablename__ = "player"
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
    club_salary = column(integer(), nullable=False)
    market_value = column(integer(), nullable=False)
    followers = column(integer(), nullable=False)
    total_goals = column(integer(), nullable=False)
    total_assists = column(integer(), nullable=False)
    total_blocks = column(integer(), nullable=False) # means all blocks on the net (including not leaded to a goal)
    match_history = relationship("PlayerMatchHistory", backref="player", lazy=True, uselist=False)
    transfer_history = relationship("PlayerTransferHistory", backref="player", lazy=True, uselist=False)
    trophies = relationship("Trophie", secondary=players_trophies_table, backref=backref("players", lazy=True))
    

class Country(model()):
    __tablename__ = "country"
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False, unique=True)
    prototype = column(string(), nullable=False)
    players = relationship("Player", backref="country", lazy=True)
    clubs = relationship("Club", backref="country", lazy=True)
    championships_collection = relationship("ChampionshipsCollection", backref="country", lazy=True)


class Role(model()):
    __tablename__ = "role"
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False)


class Skill(model()):
    __tablename__ = "skill"
    id = column(integer(), primary_key=True)
    player_id = column(integer(), foreign_key("player.id"), nullable=False)
    name = column(string(80), nullable=False)
    rating = column(integer(), nullable=False)


class Perk(model()):
    __tablename__ = "perk"
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False)


class Club(model()):
    __tablename__ = "club"
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False, unique=True)
    country_id = column(integer(), foreign_key("country.id")) 
    country_division = column(integer()) # number of division of home country where club stays at the moment
    rating = column(integer())
    budget = column(integer())
    market_value = column(integer())
    players = relationship("Player", backref="club", lazy=True)
    trophies = relationship("Trophie", secondary=clubs_trophies_table, lazy="subquery", backref=backref("clubs", lazy=True))
    match_history = relationship("ClubMatchHistory", backref="club", lazy=True, uselist=False)
    transfer_history = relationship("ClubTransferHistory", backref="club", lazy=True, uselist=False)
    trainer = column(string(80)) # TODO: create class Trainer and other personal of the club with own statistics

    # all positions in tables where club participates
    standing_teams = relationship("StandingTeam", backref="club", lazy=True)
    

class PlayerMatchHistory(model()):
    __tablename__ = "player_match_history"
    id = column(integer(), primary_key=True)
    player_id = column(integer(), foreign_key("player.id"), nullable=False)
    matches = relationship("Match", secondary=player_match_histories_matches_table, lazy="subquery", backref=backref("player_match_histories", lazy=True))


class ClubMatchHistory(model()):
    __tablename__ = "club_match_history"
    id = column(integer(), primary_key=True)
    club_id = column(integer(), foreign_key("club.id"), nullable=False)
    matches = relationship("Match", secondary=club_match_histories_matches_table, lazy="subquery", backref=backref("club_match_histories", lazy=True))


class ChampionshipMatchHistory(model()):
    __tablename__ = "championship_match_history"
    id = column(integer(), primary_key=True)
    championship_id = column(integer(), foreign_key("championship.id"), nullable=False)
    matches = relationship("Match", secondary=championship_match_histories_matches_table, lazy="subquery", backref=backref("championship_match_histories", lazy=True))


class PlayerTransferHistory(model()):
    __tablename__ = "player_transfer_history"
    id = column(integer(), primary_key=True)
    player_id = column(integer(), foreign_key("player.id"), nullable=False)
    transfers = relationship("Transfer", secondary=player_transfer_histories_transfers_table, lazy="subquery", backref=backref("player_transfer_histories", lazy=True))


class ClubTransferHistory(model()):
    __tablename__ = "club_transfer_history"
    id = column(integer(), primary_key=True)
    club_id = column(integer(), foreign_key("club.id"), nullable=False)
    transfers = relationship("Transfer", secondary=club_transfer_histories_transfers_table, lazy="subquery", backref=backref("club_transfer_histories", lazy=True))


class SeasonTransferHistory(model()):
    __tablename__ = "season_transfer_history"
    id = column(integer(), primary_key=True)
    season_id = column(integer(), foreign_key("season.id"), nullable=False)
    transfers = relationship("Transfer", secondary=season_transfer_histories_transfers_table, lazy="subquery", backref=backref("season_transfer_histories", lazy=True))


class Match(model()):
    """ 
    Match contains several sets. 
    Note that the match' score counts in sets, and now always best-of-5, i.e clubs plays until 3 winned sets of one of them. 
    """
    __tablename__ = "match"
    id = column(integer(), primary_key=True)
    ended = column(boolean(), default=False)
    clubs = relationship("Club", secondary=clubs_matches_table, lazy="subquery", backref=backref("matches", lazy=True))
    score = column(string(80), default="0-0") # club with index 0 stays left in score view
    sets = relationship("Set", backref="match", lazy=True)


class Set(model()):
    """ Set now always lasts to 25 scored points of any club """
    __tablename__ = "set"
    id = column(integer(), primary_key=True)
    match_id = column(integer(), foreign_key("match.id"), nullable=False)
    ended = column(boolean(), default=False)
    score = column(string(80), default="0-0") 


class Transfer(model()):
    __tablename__ = "transfer"
    id = column(integer(), primary_key=True)


class Trophie(model()):
    __tablename__ = "trophie"
    id = column(integer(), primary_key=True)
    championship_id = column(integer(), foreign_key("championship.id"), nullable=False)
    name = column(string(150), nullable=False)


class Championship(model()):
    __tablename__ = "championship"
    id = column(integer(), primary_key=True)
    season_id = column(integer(), foreign_key("season.id"))
    name = column(string(150))
    type = relationship("ChampionshipType", secondary=championships_types_table, lazy="subquery", backref=backref("championships", lazy=True))
    standings = relationship("StandingTeam", backref="championship", lazy=True)
    trophie = relationship("Trophie", backref="championship", lazy=True, uselist=False)
    is_league = column(boolean(), default=False) # True if part of a league (country' division)


class ChampionshipType(model()):
    """ 
    Options:
    - playoff
    - table
    """
    __tablename__ = "championship_type"
    id = column(integer(), primary_key=True)
    name = column(string(80), nullable=False)


class StandingTeam(model()):
    __tablename__ = "standing_team"
    id = column(integer(), primary_key=True)
    championship_id = column(integer(), foreign_key("championship.id"), nullable=False)
    club_id = column(integer(), foreign_key("club.id"), nullable=False)
    position = column(integer(), nullable=False)
    matches = column(integer(), nullable=False)
    wins = column(integer(), nullable=False)
    loses = column(integer(), nullable=False)
    draws = column(integer(), nullable=False)
    goals_for = column(integer(), nullable=False)
    goals_against = column(integer(), nullable=False)
    points = column(integer(), nullable=False)


class Season(model()):
    __tablename__ = "season"
    id = column(integer(), primary_key=True)
    simulation_id = column(integer(), foreign_key("simulation.id"), nullable=False)
    championships = relationship("Championship", backref="season", lazy=True)


class Simulation(model()):
    __tablename__ = "simulation"
    id = column(integer(), primary_key=True)
    seasons = relationship("Season", backref="simulation", lazy=True)





    
    
