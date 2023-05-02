import sys
from board import Board

def find_card_location_score(card, board):
    for i, column in enumerate(board):
        for j, value in enumerate(column):
            if value[0] == card[0] and value[1] == card[1]:
                return [i, j]
    for i, value in enumerate(board.freecells):
        if value[0] == card[0] and value[1] == card[1]:
            return [0, 0]
    return [-1, -1] # should never be reached

def find_state_score(board):
    score = 0
    next_cards = []
    for i in board.foundation:
        next_cards.append((i[0], i[1]+1))

    for i in next_cards:
        location = find_card_location_score(i, board)
        score += location[1]
    score = check_freecells_score(board.freecells, score)

def check_freecells_score(freecells, score):
    for i in freecells:
        if i == None:
            return score
    return score * 2


def depth_first_search(board, moves):
    if len(moves) == 6:
        return find_state_score(board), moves
    
    min_score = sys.maxsize
    # tries all moves from the board
    for i, column in enumerate(board.stack):
        # try move, then update board and pass to recursive function
        curr_moves = moves
        curr_card = column[0]
        # try stack, freecells, and foundations individually, then have to iterate through stack moves
        location = board.check_free(curr_card)
        if location:
            updated_board = board.move(curr_card, 0, location)
            curr_moves.append((curr_card, (0, location)))
            curr_score, curr_moves = depth_first_search(updated_board, curr_moves)
            if curr_score < min_score:
                min_score = curr_score
                min_score_moves = curr_moves
            curr_moves.pop()
        
        location = board.check_found(curr_card)
        if location:
            updated_board = board.move(curr_card, 2, location)
            curr_moves.append((curr_card, (2, location)))
            curr_score, curr_moves = depth_first_search(updated_board, curr_moves)
            if curr_score < min_score:
                min_score = curr_score
                min_score_moves = curr_moves
            curr_moves.pop()

        location = board.check_stack(curr_card)


    # tries all moves from the freecells
    for i , entry in enumerate(board.freecells):
        # try move, then updated board and pass to recursive function
        curr_moves = moves
        curr_card = entry
        location = board.check_found(curr_card)
        if location:
            updated_board = board.move(curr_card, 2, location)
            curr_moves.append((curr_card, (2, location)))
            curr_score, curr_moves = depth_first_search(updated_board, curr_moves)
            if curr_score < min_score:
                min_score = curr_score
                min_score_moves = curr_moves
            curr_moves.pop()

    return min_score, min_score_moves