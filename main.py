import subprocess
from algorithm import *
from getStacks import *
from board import *

pid = 11584
stacks = getStacks(pid)
print(stacks)


board = Board()
board.stack = stacks
moves = list()
score, moves = depth_first_search(board, moves)
print(score)
print(moves)