import sys
import subprocess

def parse_arguments():
    length_of_argv = len(sys.argv)
    if length_of_argv > 3:
        print "Usage: python write_log_file.py [-p, -h] <NumberOfGamePlays=1000> "
        exit(1)
    elif length_of_argv == 3:
        return sys.argv[1], int(sys.argv[2])
    elif length_of_argv == 2:
        if sys.argv[1] == "-p":
            return "-p", 1000
        elif sys.argv[1] == "-h":
            return "-h", 1000
        else:
            return "", int(sys.argv[1])
    else:
        return "", 1000

if __name__ == '__main__':
    version_of_game, number_of_games = parse_arguments()
    file_name = "./log/game_log.txt"
    py_script = "tic-tac-toe.py"
    if (version_of_game == "-p"):
        file_name = "./log/p_game_log.txt"
        py_script = "tic_tac_toe_probabilistic.py"
    if (version_of_game == "-h"):
        file_name = "./log/h_game_log.txt"
        py_script = "tic_tac_toe_heuristic.py"    
    with open(file_name, 'w') as f:
        for i in xrange(0, number_of_games):
            subprocess.call(["python", py_script], stdout=f)