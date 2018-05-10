import numpy as np
import matplotlib.pyplot as plt
import sys

symbols = {1:'x', -1:'o', 0:' '}

def parse_arguments():
    length_of_argv = len(sys.argv)
    if length_of_argv > 2:
        print "Usage: python main.py [-p, -h]"
        exit(1)
    elif length_of_argv == 2:
        if sys.argv[1] == "-p" or sys.argv[1] == "-h":
            return sys.argv[1]
        else:
            print "Usage: python main.py [-p, -h]"
            exit(1)
    else:
        return ""


'''
Description: 
    analyze the winner's move of a game

Parameters: 
    list_of_lines: the log of single game
    winner: who wins

Return: 
    array: all moves the winner takes in this game
    num_of_moves: number of moves the winner takes
'''
def analyze_moves_of_a_game(list_of_lines, winner): # winner: -1 if o wins, 1 if x wins
    array = np.zeros((3,3), dtype=int)
    num_of_moves = 0
    
    # only examine the final state of game 
    length_of_list = len(list_of_lines)
    for i in xrange(3,0,-1):
        elements = list_of_lines[length_of_list-i].split("'")
        for j in xrange(0,3):
            if (elements[(2*j)+1] == symbols[winner]):
                array[3-i][j] += 1
                num_of_moves += 1
    
    return array, num_of_moves

if __name__ == '__main__':
    version_of_game = parse_arguments()
    file_name = "./log/game_log.txt"
    if (version_of_game == "-p"):
        file_name = "./log/p_game_log.txt"
    if (version_of_game == "-h"):
        file_name = "./log/h_game_log.txt"
    
    with open(file_name, 'r') as f:
        # count the positions of moves player o and x take
        o_statistics = np.zeros((3,3), dtype=int)
        x_statistics = np.zeros((3,3), dtype=int)
        
        o_win = 0
        x_win = 0
        num_of_draw = 0
        num_of_games = 0
        
        lines_in_a_game = []
        sum_of_moves = [0, 0]
        
        '''
        Each time we load one line from log.txt file. 
        Those lines recording the same game will be stored in lines_in_a_game[].
        Whenever we detect the ending of game, we analyze lines_in_a_game[] and further empty it.
        '''
        for line in f:
            words = line.split(' ')
            if (words[0] == 'player'): # game over and there's a winner
                num_of_games += 1
                if (words[1] == 'o'):
                    o_win += 1
                    o_moves_array, num_of_o_moves = analyze_moves_of_a_game(lines_in_a_game, -1)
                    o_statistics += o_moves_array
                    sum_of_moves[0] += num_of_o_moves
                elif (words[1] == 'x'):
                    x_win += 1
                    x_moves_array, num_of_x_moves = analyze_moves_of_a_game(lines_in_a_game, 1)
                    x_statistics += x_moves_array
                    sum_of_moves[1] += num_of_x_moves                
                else:
                    print "Unknown format:", line
                    exit(1)
                    
                lines_in_a_game = []
                
            elif (words[0] == 'game'): # game over in a draw
                num_of_games += 1
                num_of_draw += 1
                lines_in_a_game = []
            else: # game still on
                lines_in_a_game.append(line)
                
    x_probability = np.zeros((3,3), dtype=float)
    o_probability = np.zeros((3,3), dtype=float)
    if (sum_of_moves[1] != 0):
        x_probability = np.divide(x_statistics, float(sum_of_moves[1]))
    if (sum_of_moves[0] != 0):
        o_probability = np.divide(o_statistics, float(sum_of_moves[0]))
    
    if version_of_game == "":
        print "version: original\n"
    if version_of_game == "-p":
        print "version: probabilistic\n"
    if version_of_game == "-h":
        print "version: heuristic\n"    
        
    print "Num of games:", num_of_games, "\nNum of draw:", num_of_draw, "\nO wins", o_win, "\nX wins", x_win
    
    print "\no statistics:\n", o_probability, "\n"
    print "\nx statistics:\n", x_probability, "\n" 
    
    # plot the result
    values = []
    values.extend((x_win, o_win, num_of_draw))
    ind = np.arange(3)
    fig, ax = plt.subplots()
    ax.bar(ind, values, 0.3, align='center')
    plt.xticks(ind, ('x wins', 'o wins', 'draw'))
    plt.ylabel('games')
    for i in range(3):
        plt.text(x = ind[i], y = values[i], s = str(values[i]), size=12)
    plt.show()
    
    if version_of_game == "":
        np.savetxt("./prob/x_prob.txt", x_probability)
        np.savetxt("./prob/o_prob.txt", o_probability)          