# Probabilistic Strategy for Tic Tac Toe

implement a probabilistic strategy for Tic Tac Toe

## Usage

### running "tic-tac-toe.py", "tic_tac_toe_probabilistic.py" and "tic_tac_toe_heuristic.py"

tic-tac-toe.py is the original version, making a move uniformly at random. And in tic_tac_toe_probabilistic.py (tic_tac_toe_heuristic.py), we make a move according to the probablistic(heuristic) strategy.

To run them, use 
```
python tic-tac-toe.py
python tic_tac_toe_probabilistic.py
python tic_tac_toe_heuristic.py
```


### running write_log_file.py

write_log_file.py writes the log of entire tournament to an output file. You can also specify the number of game plays in this tournament and the tic-tac-toe version in the command line. 
The default version is the original version.

To run it, use
```
python write_log_file.py [-p, -h] <NumberOfGamePlays=1000> 

optional argument:
-p, -h : run the probabilistic or heuristic version of tic tac toe

default version: 
original version, i.e. run "python write_log_file.py <NumberOfGamePlays=1000>"
```
And the output file will be put in ./log/ folder and named game_log.txt, p_game_log.txt or h_game_log.txt, depending on the version of tic tac toe. 

### running main.py

main.py loads the game log file and further creates a statistic of auspicious positions on the tic tac toe board. Two output files will be created to store the normalized statistics if the original version of game is chosen. 

To run main.py, use
```
Usage: python main.py [-p, -h]

optional argument:
-p, -h : load the log file of the probabilistic or heuristic version of tic tac toe

default version of game log: 
original version, i.e. run "python main.py"
```
Two output files, x_prob.txt and o_prob.txt, will be put inside ./prob/ folder. 
