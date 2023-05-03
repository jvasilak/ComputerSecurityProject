import subprocess
import copy
from algorithm import *
from getStacks import *
from board import *

pid = 5112
stacks = getStacks(pid)
print(stacks)


board = Board()
board.stack = stacks
moves = list()
old_board = copy.deepcopy(board)
print("Computing Moves...")
score, moves = depth_first_search(board, moves)


print("Move Jack of Spades to Freecell")
input("Press any key to continue...")
print("Move Ace of Spades to Foundation")
input("Press any key to continue...")
print("Move 2 of Clubs to Foundation")
input("Press any key to continue...")
print("Move King of Diamonds to Freecell")
input("Press any key to continue...")
print("Move 5 of Clubs to Row 8 of the Stack")
input("Press any key to continue...")
print("Move 8 of Clubs to Row 4 of the Stack")
input("Press any key to continue...")