#####
# Original by
# Computer Science and Software Engineering
# PLTW AP CS Principles
# (c)2014 Project Lead The Way, Inc.
# Edited by Colin Wakefield & Jett Kaspar
#####
from Player_def import PlayerDef
import random

class Team2(PlayerDef):

    def __init__(self):
        PlayerDef.__init__(self)
        #max
        self.team_name = "TheFern"
        self.strategy_name = "Rand it up "
        self.strategy_description = "randomly picking between 3 options"

    '''
           write code here
    '''
    def move(self, op):

        # gets your opponent's move history and score
        OMH = op.move_history
        OS = op.score
        # gets yourmove history and score
        YMH = self.move_history
        YS = self.score

        rand = random.randint(1, 3)
        if rand == 1:
            return "r"
        elif rand == 2:
            return "p"
        else:
            return "s"