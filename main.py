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
print("Computing Moves...")

#score, moves = depth_first_search(board, moves)


while not board.win():
    curr_moves = list()
    score, curr_moves = depth_first_search(board, curr_moves)
    moves = moves + curr_moves
    for i in curr_moves:
        board = board.move(i[0], i[1][0], i[1][1])

while len(moves) > 0:
    curr_move = moves[0]
    moves = moves[1:]
    if curr_move[1][1] != 1:
        print("Move the", values[curr_move[0][1]-1], suits[curr_move[0][0]], "to", locations[curr_move[1][0]], ".")
    else:
        row = curr_move[1][1] + 1
        print("Move the", values[curr_move[0][1]-1], suits[curr_move[0][0]], "to", locations[curr_move[1][1]], "row", row, ".")
    input("Press enter to continue...")

print("Congratulations! You won!")