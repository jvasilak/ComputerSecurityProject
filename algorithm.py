
def find_card_location(card_number, board, freecells):
    for i, column in enumerate(board):
        for j, value in enumerate(column):
            if value == card_number:
                return [i, j]
    for i, card in enumerate(freecells):
        if card == card_number:
            return [0, 0]
    return [-1, -1] # should never be reached

def find_state_score(board, freecells, foundation):
    score = 0
    next_cards = []
    for i in foundation:
        next_cards.append(i+1) # i + 1 should be whatever the next card in the suit's difference would be

    for i in next_cards:
        location = find_card_location(i, board, freecells)
        score += location[1]
    score = check_freecells(freecells, score)

def check_freecells(freecells, score):
    for i in freecells:
        if i == 0:
            return score
    return score * 2
