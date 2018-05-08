# Probabilistic Strategy for Tic Tac Toe

implement a probabilistic strategy for Tic Tac Toe

## Usage

### running tic-tac-toe.py and m_tic_tac_toe.py

tic-tac-toe.py is the original version, making a move uniformly at random. But in m_tic_tac_toe.py, we make a move according to the probabilities we obtain from running tic-tac-toe.py

To run them, use 
```
python tic-tac-toe.py
python m_tic_tac_toe.py
```


### running write_log_file.py

write_log_file.py is used to write the log of entire tournament to a file. You can also specify the number of game plays in this tournament and the tic-tac-toe version in the command line. 

To run it, use
```
python write_log_file.py <NumberOfGamePlays=1000> <VersionOfTicTacToe=tic-tac-toe.py>
```
And the output file will be named game_log.txt (or m_game_log.txt), depending on which version of tic tac toe you use. 

### running main.py

main.py analyzes the game_log.txt (or m_game_log.txt) and further creates a statistic of auspicious positions on the tic tac toe board. At last, the normalized statistic data is saved in the output file.

To run main.py, use
```
python main.py 
```
To store the normalized statistic data of player x and player o, two output files, x_prob.txt and o_prob.txt, will be created. 
