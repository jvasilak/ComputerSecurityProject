import subprocess
import copy
from algorithm import *
from getStacks import *
from board import *

pid = 26308
stacks = getStacks(pid)
suits = [" of Clubs", "of Diamonds", "of Hearts", "of Spades"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "Kings"]
locations = ["freecell", "stack", "foundation"]

board = Board()
board.stack = stacks
moves = list()
moves2 = list()
old_board = copy.deepcopy(board)
print("Computing Moves...")

score, moves = depth_first_search(board, moves)
for i in moves:
    board = board.move(i[0], i[1][0], i[1][1])
print("Computing again...")
score, moves2 = depth_first_search(board, moves2)
moves = moves + moves2
print(score, moves)
print(board.freecell, board.foundation, "\n", board.stack)

'''
while len(moves) > 0:
    curr_move = moves[0]
    moves = moves[1:]
    print("Move the ", , " to ", ".")
    print("Move the ", , " to ", " row ", ".")
'''