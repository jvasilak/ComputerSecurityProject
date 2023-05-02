import copy

''' cards are as follows: (suit, value)
suit: 0-3 with values 
0: Clubs
1: Diamonds
2: Hearts
3: Spades

order in foundation
club
spade
heart
diamond



Values: 
    1 = ace 
    13 = king
keeps the values in line with number


'''
class Board:

    def __init__(self):
        self.freecell = [None, None, None, None]
        self.stack = [[],[],[],[],[],[],[],[]]
        self.foundation = [[],[],[],[]]

    '''def __init__(self, board):
        self.freecell = board.freecell
        self.stack = board.stack
        self.foundation = board.foundation'''

    def check_free(self, card):
        for i in range(len(self.freecell)):
            if not self.freecell[i]:
                return i
        return None


    def check_found(self, card):
        suit, value = card[0], card[1]
        if (value == 1 and not self.foundation[suit]) or (self.foundation[suit] and value == (self.foundation[suit][-1] + 1)):
            return suit
        return None

    def check_stack(self, card):
        yield from (index for index, stack in enumerate(self.stack) if stack and self.check_stack_ok(card, stack[-1]) or not stack)

    @staticmethod
    def check_stack_ok(card1, card2):
        color = 1 if card1[0] == 1 or card1[0] == 2 else 0
        color2 = 1 if card2[0] == 1 or card2[0] == 2 else 0
        value = card1[1]
        value2 = card2[1]

        if color == color2:
            return False
        elif value == value2 - 1:
            return True
        else:
            return False
        

    def win(self):
        done = 0
        for suit in range(4):
            if self.foundation[0] and self.foundation[0][-1][1] == 13:
                done += 1
        
        return True if done == 4 else False
    
    def card_index(self, card):
        if card in self.freecell:
            return(0,self.freecell.index(card))
        else:
            return(1, next((i for i,stack in enumerate(self.stack) if card in stack),None))
    

    def remove(self,card):
        location, index = self.card_index(card)

        if location == 0:
            self.freecell[index]=None
        else:
            self.stack[index].pop()

    def move(self, card, location, index):

        new_board = copy.deepcopy(self)
        new_board.remove(card)
        
        if location == 0:
            new_board.freecell[index] = card
        elif location == 1:
            new_board.stack[index].append(card)
        else:
            new_board.foundation[index].append(card)
        return new_board



