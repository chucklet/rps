#####
# Original by
# Computer Science and Software Engineering
# PLTW AP CS Principles
# (c)2014 Project Lead The Way, Inc.
# Edited by Colin Wakefield & Jett Kaspar
#####
import random
import Player_def
import Team0 , Team1 , Team2
import os

all_files = [Player_def, Team0, Team1, Team2]
for k in all_files:
    reload(k)

modules = [Team0.Team0(), Team1.Team1(), Team2.Team2()]

# TODO: Make print look nice and pick a winner

'''
inputs: Modules

return : The scores for each player and the moves for each player

objective : simulate the players playing each other is a game rock, paper , scissors

'''
def run(modules):

    zeros_list = [0] * len(modules)  # to initialize each player's head-to-head scores
    scores = [zeros_list[:] for module in modules]  # Copy it or it's only 1 list
    moves = [zeros_list[:] for module in modules]  # Copy it or it's only 1 list

    #number of rounds change if you want to
    rounds = 150 #random.randint(100,200)


    for first_team_index in range(len(modules)):
        for second_team_index in range(first_team_index):
            player1 = modules[first_team_index]
            player2 = modules[second_team_index]
            for k in range(rounds):
                # print player1, player2
                round_evalulator(player1, player2)

            scores[first_team_index][second_team_index] = (player1.score) #/ float(len(player1.move_history))  # int division not an issue
            moves[first_team_index][second_team_index] = player1.move_history
            # Redundant, but record this for the other player, from their perspective
            scores[second_team_index][first_team_index] = (player2.score) #/ float(len(player2.move_history))
            moves[second_team_index][first_team_index] = player2.move_history

            player1.reset()
            player2.reset()

        # Playing yourself doesn't do anything
        scores[first_team_index][first_team_index] = 0
        moves[first_team_index][first_team_index] = ''
    return scores, moves

'''
Input player1 , player2

Output None

Objective : simulate the rounds for the

'''
def round_evalulator(player1, player2):
    move1 = player1.move(player2)
    move2 = player2.move(player1)

    player1.move_history += move1
    player2.move_history += move2

    TIE = 0
    WIN = 10
    LOSS = -10

    play = move1 + move2
    if play == 'rs':
        player1.score += WIN
        player2.score += LOSS
    elif play == 'pr':
        player1.score += WIN
        player2.score += LOSS
    elif play == 'sp':
        player1.score += WIN
        player2.score += LOSS
    elif play == 'rp':
        player1.score += LOSS
        player2.score += WIN
    elif play == 'ps':
        player1.score += LOSS
        player2.score += WIN
    elif play == 'sr':
        player1.score += LOSS
        player2.score += WIN
    elif move1 == move2:
        player1.score += TIE
        player2.score += TIE
    else:
        player1.score += LOSS
        player2.score += LOSS


def capitalize(history1, history2):
    '''Accept two strings of equal length.
    Return the same two strings but capitalizing the opponent of 'c' each round.
    '''
    caphistory1, caphistory2 = '', ''
    for i in range(len(history1)):
        p1 = history1[i]
        p2 = history2[i]
        if p1 == 'c':
            p2 = p2.upper()
        if p2 in 'cC':
            p1 = p1.upper()
        caphistory1 += p1
        caphistory2 += p2
    return caphistory1, caphistory2

def PrintFile(fname):
    '''Printes the contence of a file.
    Returns None
    '''
    with open(fname, 'r') as fin:
        print fin.read()






def make_section1(modules, scores):
    '''
    ----------------------------------------------------------------------------
    Section 1 - Player vs. Player
    ----------------------------------------------------------------------------
    A column shows pts/round earned against each other player:
                P0    P1
    vs. P0 :     0   100
    vs. P1 :  -500     0
    TOTAL  :  -500   100
    '''
    # First line
    section1 = '-' * 80 + '\nSection 1 - Player vs. Player\n' + '-' * 80 + '\n'
    section1 += 'Each column shows pts/round earned against each other player:\n'
    # Second line
    section1 += '        '
    for i in range(len(modules)):
        section1 += '{:>7}'.format('P' + str(i))
    section1 += '\n'
    # Add one line per team
    for index in range(len(modules)):
        section1 += 'vs. P' + str(index) + ' :'
        for i in range(len(modules)):
            section1 += '{:>7}'.format(scores[i][index])
        section1 += '\n'

    # Last line
    section1 += 'TOTAL  :'
    for index in range(len(modules)):
        section1 += '{:>7}'.format(sum(scores[index]))
    return section1 + '\n'


def make_section2(modules, scores):
    '''
    ----------------------------------------------------------------------------
    Section 2 - Leaderboard
    ----------------------------------------------------------------------------
    Average points per round:
    Team name (P#):  Score       with strategy name
    Champ10nz (P0):   100 points with Loyal
    Rockettes (P1):  -500 points with Backstabber
    '''
    section2 = '-' * 80 + '\nSection 2 - Leaderboard\n' + '-' * 80 + '\n'
    section2 += 'Average points per round:\n'
    section2 += 'Team name (P#):  Score      with strategy name\n'

    # Make a list of teams' 4-tuples
    section2_list = []
    for index in range(len(modules)):
        section2_list.append((modules[index].team_name,
                              'P' + str(index),
                              str(sum(scores[index]) / len(modules)),
                              str(modules[index].strategy_name)))
    section2_list.sort(key=lambda x: int(x[2]), reverse=True)

    # Generate one string per team
    # Rockettes (P1):  -500 points with Backstabber
    for team in section2_list:
        team_name, Pn, n_points, strategy_name = team
        section2 += '{:<10}({}): {:>10} points with {:<40}\n'.format(team_name[:10], Pn, n_points, strategy_name[:40])
    return section2


def make_reports(modules, scores, moves):
    section0 = make_section0(modules, scores)
    section1 = make_section1(modules, scores)
    section2 = make_section2(modules, scores)

    section3 = []
    for index in range(len(modules)):
        section3.append(make_section3(modules, moves, scores, index))
    return section0, section1, section2, section3


def make_section0(modules, scores):
    '''
    Produce the following string:
    ----------------------------------------------------------------------------
    Section 0 - Line up
    ----------------------------------------------------------------------------
    Player 0 (P0): Team name 0, Strategy name 0,
         Strategy 0 description
    Player 1 (P1): Team name 1, Strategy name 1,
         Strategy 1 description
    '''
    section0 = '-' * 80 + '\n'
    section0 += 'Section 0 - Line up\n'
    section0 += '-' * 80 + '\n'
    for index in range(len(modules)):
        section0 += 'Player ' + str(index) + ' (P' + str(index) + '): '
        section0 += str(modules[index].team_name) + ', ' + str(modules[index].strategy_name) + '\n'
        strategy_description = str(modules[index].strategy_description)
        # Format with 8 space indent 80 char wide
        while len(strategy_description) > 1:
            newline = strategy_description[:72].find('\n')
            if newline > -1:
                section0 += ' ' * 8 + strategy_description[:newline + 1]
                strategy_description = strategy_description[newline + 1:]
            else:
                section0 += ' ' * 8 + strategy_description[:72] + '\n'
                strategy_description = strategy_description[72:]
    return section0



def make_section3(modules, moves, scores, index):
    '''Return a string with information for the player at index, like:
    ----------------------------------------------------------------------------
    Section 3 - Game Data for Team Colloid c=-500 b=-250 C=0 B=+100
    ----------------------------------------------------------------------------
    -133 pt/round: Colloid (P6) "Collude every 3rd round"
    -233 pt/round: 2PwnU (P8) "Betray, then alternate"
    bBcBbCbBcBbCbBcBbCbBcBbCbBcBbCbBcBbCbBcBbCbBcBbCbBcBbCbBcBbCbBcBbCbBcBbCbBcB
    bcBcbCbcbcbCBcbcbCBcbcbCBcbcbCBcbcbCBcbcbCBcbcbCBcbcbCBcbcbCBcbcbCBcbcbCBcbc
    '''
    section3 = '-' * 80 + '\nSection 3 - Game Data for Team '
    section3 += modules[index].team_name + '\n'
    section3 += '-' * 80 + '\n'
    # Make 4 lines per opponent
    for opponent_index in range(len(modules)):
        if opponent_index != index:
            # Line 1
            section3 += str(scores[index][opponent_index])
            section3 += ' pt/round: ' + modules[index].team_name + '(P'
            section3 += str(index) + ') "' + modules[index].strategy_name + '"\n'
            # Line 2
            section3 += str(scores[opponent_index][index])
            section3 += ' pt/round: ' + modules[opponent_index].team_name + '(P'
            section3 += str(opponent_index) + ') "' + modules[opponent_index].strategy_name + '"\n'
            # Lines 3-4
            hist1, hist2 = capitalize(moves[index][opponent_index], moves[opponent_index][index])
            while len(hist1) > 1:
                section3 += hist1[:80] + '\n'
                section3 += hist2[:80] + '\n\n'
                hist1 = hist1[80:]
                hist2 = hist2[80:]
            section3 += '-' * 80 + '\n'
    return section3


def make_code_string(modules):
    '''Returns a string of the code from each file.
    '''
    code = '-' * 80 + '\n'
    code += 'Code of each player\'s algorithm\n'
    code = '-' * 80 + '\n'
    for index in range(len(modules)):
        players_code_filename = str(modules[index]).split(' ')[1].replace('\'', '')
        directory = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(directory, players_code_filename)
        players_code_file = open(filename + '.py', 'r')
        code += '-' * 80 + '\n'
        code += players_code_filename
        code += '-' * 80 + '\n'
        code += ''.join(players_code_file.readlines())
    return code


def copy_template():
    '''Transfer code in team0.py to team1.py though team14.py
    '''
    directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(directory, 'team0.py'), 'r') as sourcefile:
        source = sourcefile.readlines()
    for i in range(1, 15):
        target = 'team' + str(i) + '.py'
        filename = os.path.join(directory, target)
        with open(filename, 'w') as target_file:
            target_file.write(''.join(source))


def post_to_api():
    pass


def post_to_local_html():
    pass


def post_to_file(string, filename='tournament.txt', directory=''):
    '''Write output in a txt file.
    '''
    # Use the same directory as the python script
    if directory == '':
        directory = os.path.dirname(os.path.abspath(__file__))
        # Name the file tournament.txt
    filename = os.path.join(directory, filename)
    # Create the file for the round-by-round results
    filehandle = open(filename, 'w')
    filehandle.write(string)


if __name__ == "__main__":
    scores, moves = run(modules)
    #print scores
    #print moves
    #make_it_pretty(modules, scores, moves)
    section0, section1, section2, section3 = make_reports(modules, scores, moves)
    #code = make_code_string(modules)
    # On screen, include the first three out of four sections of the report.
    print(section0 + section1 + section2)
    # To file output, store all teams' code and all teams' section 3 reports.
    post_to_file(section0 + section1 + section2 + ''.join(section3))
    #make_section1()
    #PrintFile("tourney.txt")
    #print len("vs. Team0    ")
