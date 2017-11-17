#####
# Original by
# Computer Science and Software Engineering
# PLTW AP CS Principles
# (c)2014 Project Lead The Way, Inc.
# Edited by Colin Wakefield & Jett Kaspar
#####
class PlayerDef(object):

    def __init__(self):

        self.team_name = 'Default'  # Only 10 chars displayed.
        self.strategy_name = 'Default Strat Name'
        self.strategy_description = 'Default description'

        self.score = 0
        self.move_history = ""

    def move(self,op):
        raise NotImplementedError("Beep Boop Error")

    def reset(self):
        self.score = 0
        self.move_history = ''