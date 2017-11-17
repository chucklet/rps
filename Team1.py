#####
# Original by
# Computer Science and Software Engineering
# PLTW AP CS Principles
# (c)2014 Project Lead The Way, Inc.
# Edited by Colin Wakefield & & Jett Kaspar
#####
from Player_def import PlayerDef
import random

class Team1(PlayerDef):

    def __init__(self):
        PlayerDef.__init__(self)
        self.team_name = "TeamDog"
        self.strategy_name = "return s"
        self.strategy_description = "Scissors all the time"

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
        return "s"


