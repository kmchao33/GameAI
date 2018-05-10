
import numpy as np
import matplotlib.pyplot as plt


def move_still_possible(S):
    return not (S[S == 0].size == 0)


def move_at_random(S, p):
    xs, ys = np.where(S == 0)

    i = np.random.permutation(np.arange(xs.size))[0]
    
    S[xs[i], ys[i]] = p

    return S


def move_was_winning_move(S, p):
    if np.max((np.sum(S, axis=0)) * p) == 3:
        return True

    if np.max((np.sum(S, axis=1)) * p) == 3:
        return True

    if (np.sum(np.diag(S)) * p) == 3:
        return True

    if (np.sum(np.diag(np.rot90(S))) * p) == 3:
        return True

    return False


# p is going to win:
# has occupied two places in a line and the other space is empty
def is_going_to_win(S, p):
    if np.max((np.sum(S, axis=0)) * p) == 2:
        return True

    if np.max((np.sum(S, axis=1)) * p) == 2:
        return True

    if (np.sum(np.diag(S)) * p) == 2:
        return True

    if (np.sum(np.diag(np.rot90(S))) * p) == 2:
        return True

    return False


# count how many ways p is going to win:
# p has occupied two places in a line and the other space is empty
# returns number of such combinations
def possible_ways_to_win(S, p):
    n = 0
    
    if np.max((np.sum(S, axis=0)) * p) == 2:
        n += 1

    if np.max((np.sum(S, axis=1)) * p) == 2:
        n += 1

    if (np.sum(np.diag(S)) * p) == 2:
        n += 1

    if (np.sum(np.diag(np.rot90(S))) * p) == 2:
        n += 1

    return n


# first move on one corner
def move_was_first_move_on_corner(S):
    if np.count_nonzero(S) == 1:  # first move
        if S[0, 0] != 0:
            return True
        if S[0, 2] != 0:
            return True
        if S[2, 0] != 0:
            return True
        if S[2, 2] != 0:
            return True

    return False


# relate numbers (1, -1, 0) to symbols ('x', 'o', ' ')
symbols = {1:'x', -1:'o', 0:' '}


# print game state matrix using symbols
def print_game_state(S):
    B = np.copy(S).astype(object)
    for n in [-1, 0, 1]:
        B[B == n] = symbols[n]
    print B


# evaluation function modified from the on from the lecture
# Eval(n,p)=(number of lines where p can win)
# -(number of lines where -p can win)
# exceptions:
# Eval(n,p)=+100 if p wins
# Eval(n,p)=-200 if -p can win next turn, with two possible ways
# Eval(n,p)=-100 if -p can win next turn
# Eval(n,p)=+10 if p has two empty spaces to win next turn
# Eval(n,p)=+5 if it is the first move and p takes a corner
def evaluate_game_state(S, p):
    if move_was_winning_move(S, p):
        return 100
        
    if possible_ways_to_win(S, -p) > 1:
        return -200
    
    if is_going_to_win(S, -p):
        return -100

    if possible_ways_to_win(S, p) > 1:
        return 10
    
    if move_was_first_move_on_corner(S):
        return 5
    
    T1 = np.copy(S)
    T1[T1 == 0] = p
    n1 = num_winning_lines(T1, p)
    
    T2 = np.copy(S)
    T2[T2 == 0] = -p
    n2 = num_winning_lines(T2, -p)
    
    return n1 - n2


# count winning line function from the lecture
# number of p-winning lines
def num_winning_lines(T, p):
    cs = np.sum(T, axis=0) * p  # column sums
    rs = np.sum(T, axis=1) * p  # row sums
    s1 = cs[cs == 3].size
    s2 = rs[rs == 3].size
    s3 = 0
    if np.sum(np.diag(T)) * p == 3:
        s3 = 1 
    s4 = 0
    if np.sum(np.diag(np.rot90(T))) * p == 3:
        s4 = 1
    
    return s1 + s2 + s3 + s4


# p evaluates all free positions on the board
# and selects the one with highest evaluation
def move_with_strategy(S, p):
    xs, ys = np.where(S == 0)
    evaluates = np.array(xs)
    T = np.copy(S)
    
    for i in np.arange(xs.size):
        T[xs[i], ys[i]] = p
        evaluates[i] = evaluate_game_state(T, p)
        T[xs[i], ys[i]] = 0
    
    i = np.random.permutation(np.where(evaluates == evaluates.max())[0])[0]
    
    S[xs[i], ys[i]] = p

    return S


if __name__ == '__main__':
    # initialize 3x3 tic tac toe board
    gameState = np.zeros((3, 3), dtype=int)

    # initialize player number, move counter
    player = 1
    mvcntr = 1

    # initialize flag that indicates win
    noWinnerYet = True

    while move_still_possible(gameState) and noWinnerYet:
        # get player symbol
        name = symbols[player]
        print '%s moves' % name

        if player == 1:
            # let player move with heuristic strategy
            gameState = move_with_strategy(gameState, player)
        else:
            # let player move at random
            gameState = move_at_random(gameState, player)

        # print current game state
        print_game_state(gameState)
        
        # evaluate game state
        if move_was_winning_move(gameState, player):
            print 'player %s wins after %d moves' % (name, mvcntr)
            noWinnerYet = False

        # switch player and increase move counter
        player *= -1
        mvcntr += 1

    if noWinnerYet:
        print 'game ended in a draw'
