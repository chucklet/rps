# Editing RPS_Runner to be more modular
# And to work with future GUI


# \/\/\/\/\/\/\/Be sure to set TeamX below\/\/\/\/\/\/\/

import _tkinter
import Player_def
import Team2, HumanPlayer

all_files = [Player_def, Team2, HumanPlayer]
for k in all_files:
    reload(k)

modules = [Team2.Team2(), HumanPlayer.HumanPlayer()]

#^^^^^SET THREE INSTANCES OF TeamX ABOVE TO THE TEAM NAME OF THE COMPUTER TEAM BEFORE RUNNING^^^^^

def winner(player1, player2):
    """Returns an int representing the winner of the round,
        and adds the moves to both player's move history
        0 = tie, 1 = 1st arg win, 2 = 2nd arg win, -1 = ERROR"""
    move1 = player1.move(player2)
    move2 = player2.move(player1)

    player1.move_history += move1
    player2.move_history += move2

    play = move1 + move2
    if play == 'rs':
        winner = 1
    elif play == 'pr':
        winner = 1
    elif play == 'sp':
        winner = 1
    elif play == 'rp':
        winner = 2
    elif play == 'ps':
        winner = 2
    elif play == 'sr':
        winner = 2
    elif move1 == move2:
        winner = 0
    else:
        raise ValueError("Invalid Play... something is wrong.")
        winner = -1
    return play

#TODO: Make Gui

"""
Basic program outline:
Design gui
- has reset button if the computer team wants to reset human's move history
- Has image of computer on left, Human on the other
- Three buttons under human side for RPS
- Round/Play counter at the top
- When the player chooses a button:
  > Display a gif on each side of hand shake
  > call humanPlayer.setMove(move)
  > display winner(player1, player2)
  > fix round counters and stuff
- At the end of three rounds with three wins each:
- Display a winning screen
"""