#Modifying computer team code to have a human player
#To use this class, use setMove before you call anything that calls Move on this player

class HumanPlayer(PlayerDef):

    def __init__(self):
        PlayerDef.__init__(self)
        self.team_name = "Human"
        self.strategy_name = "Insight"
        self.strategy_description = "Millennia of Evolution"
        self.storedMove = "r"

    def move(self, op):
        return self.storedMove

    def setMove(self, move):
        self.storedMove = move

    def reset(self):
        self.score = 0
        self.move_history = ''


