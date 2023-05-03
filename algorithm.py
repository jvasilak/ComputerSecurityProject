import sys
from board import Board

def find_card_location_score(card, board):
    for i, column in enumerate(board.stack):
        for j, value in enumerate(column):
            if value[0] == card[0] and value[1] == card[1]:
                return [i, j]
    for i, value in enumerate(board.freecell):
        if value == None:
            continue
        if value[0] == card[0] and value[1] == card[1]:
            return [0, 0]
    return [-1, -1] # should never be reached

def find_state_score(board):
    score = 0
    next_cards = []
    for i, card in enumerate(board.foundation):
        if not card:
            next_cards.append((i, 1))
        else:
            next_cards.append((card[0][0], card[0][1]+1))

    for i in next_cards:
        location = find_card_location_score(i, board)
        score += location[1]
    score = check_freecells_score(board.freecell, score)
    return score

def check_freecells_score(freecells, score):
    for i in freecells:
        if i == None:
            return score
    return score * 2


def depth_first_search(board, moves):

    if len(moves) == 6:
        return find_state_score(board), moves
    
    min_score = sys.maxsize
    min_score_moves = list()
    # tries all moves from the board
    for i, column in enumerate(board.stack):
        # try move, then update board and pass to recursive function
        if not column:
            continue
        curr_moves = moves.copy()
        curr_card = column[-1]
        # try stack, freecells, and foundations individually, then have to iterate through stack moves
        location = board.check_free(curr_card)
        if location != None:
            updated_board = board.move(curr_card, 0, location)
            #curr_moves = moves + [(curr_card, (0, location))]
            curr_moves.append((curr_card, (0, location)))
            curr_score, updated_moves = depth_first_search(updated_board, curr_moves)
            if curr_score < min_score and len(updated_moves) == 6:
                #print("Score: ", curr_score, " Moves: ", updated_moves)
                min_score = curr_score
                min_score_moves = updated_moves
            if curr_moves:
                curr_moves.pop()

        location = board.check_found(curr_card)
        if location != None:
            updated_board = board.move(curr_card, 2, location)
            #curr_moves = moves + [(curr_card, (2, location))]
            curr_moves.append((curr_card, (2, location)))
            curr_score, updated_moves = depth_first_search(updated_board, curr_moves)
            if curr_score < min_score and len(updated_moves) == 6:
                #print("Score: ", curr_score, " Moves: ", updated_moves)
                min_score = curr_score
                min_score_moves = updated_moves
            if curr_moves:
                curr_moves.pop()

        location = board.check_stack(curr_card)
        for i in location:
            if not i:
                continue
            updated_board = board.move(curr_card, 1, i)
            #curr_moves = moves + [(curr_card, (2, i))]
            curr_moves.append((curr_card, (2, i)))
            curr_score, updated_moves = depth_first_search(updated_board, curr_moves)
            if curr_score < min_score and len(updated_moves) == 6:
                #print("Score: ", curr_score, " Moves: ", updated_moves)
                min_score = curr_score
                min_score_moves = updated_moves
            if curr_moves:
                curr_moves.pop()


    # tries all moves from the freecells
    for i , entry in enumerate(board.freecell):
        # try move, then updated board and pass to recursive function
        if not entry:
            continue
        curr_moves = moves.copy()
        curr_card = entry
        location = board.check_found(curr_card)
        if location != None:
            updated_board = board.move(curr_card, 2, location)
            #curr_moves = moves + [(curr_card, (2, location))]
            curr_moves.append((curr_card, (2, location)))
            curr_score, updated_moves = depth_first_search(updated_board, curr_moves)
            if curr_score < min_score and len(updated_moves) == 6:
                #print("Score: ", curr_score, " Moves: ", updated_moves)
                min_score = curr_score
                min_score_moves = updated_moves
            if curr_moves:
                curr_moves.pop()

        location = board.check_stack(curr_card)
        for i in location:
            updated_board = board.move(curr_card, 1, i)
            #curr_moves = moves + [(curr_card, (2, i))]
            curr_moves.append((curr_card, (2, i)))
            curr_score, updated_moves = depth_first_search(updated_board, curr_moves)
            if curr_score < min_score and len(updated_moves) == 6:
                #print("Score: ", curr_score, " Moves: ", updated_moves)
                min_score = curr_score
                min_score_moves = updated_moves
            if curr_moves:
                curr_moves.pop()
    #print("FScore: ", min_score, " FMoves: ", min_score_moves)
    return min_score, min_score_moves