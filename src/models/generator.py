"""
Generation engine of players, clubs and events.
"""

import os
import csv
from random import randint

from typing import List

from . import orm

        

def generate_player(
                    *, firstname: str, surname: str, 
                    country: orm.Country, age: int, roles: List[orm.Role], skills: List[orm.Skill], 
                    perks: List[orm.Perk], club: orm.Club, 
                    match_history: orm.PlayerMatchHistory, transfer_history: orm.PlayerTransferHistory, 
                    trophies: List[orm.Trophie],
                    club_salary=0, market_value=0, 
                    followers=0, total_goals=0, total_assists=0, total_blocks=0
                    ) -> orm.Player:

    """ Generate a player with given parameters and returns him. 
    If any of the parameter not given, use random one. """
    if not firstname:
        pass
        # make here query from db table

    # for future to query countries for picking
    # countries = orm.Country.query.all() 




            

            


            