# How to run the program
# Copy and paste the code in codeSkupltor
# https://py2.codeskulptor.org/

# Testing template for the Card class
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


#################################################
# Student should insert the implementation of the Card class here

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class

class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []
        #self.Hand = [Card(SUITS[i], SUITS[j])for i in SUITS for j in RANKS]
        
    def __str__(self):
        # return a string representation of a hand
        s = ""
        for i in range(len(self.hand)):
            s += str(self.hand[i])
        return s
    
    def add_card(self, card):
        # add a card object to a hand
        #self.card = Card(suit, rank)
        self.hand.append(card)
        return self.hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        my_item = ""
        my_value = ""
        for item in self.hand:
            my_item += str(item)
        for k, v in VALUES.items():
            for e, value in enumerate(my_item):
                #print value
                if(k == value):
                    my_value += k
            if k in my_value:
                hand_value += v
                #print hand_value
        if(my_value.find('A') == -1):
            return hand_value
        elif((hand_value + 10) <= 21):
            return (hand_value + 10)
        else:
            return hand_value
                    
    def draw(self, canvas, pos):
        #pass # draw a hand on the canvas, use the draw method for cards
        position = pos
        for c in self.hand:
            card = Card(c[0],c[1])
            card.draw(canvas, pos)
        
                        
class Deck:
    def __init__(self):
        self.i = 0
        self.j = 0               
        self.deck = [[self.i,self.j]for self.i in SUITS for self.j in RANKS]
               
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        my_deal = self.deck.pop()
        # deal a card object from the deck
        return str(my_deal[0])+str(my_deal[1]) 
        #return str(self.deck.pop()[0])+str(self.deck.pop()[1])
        
    def __str__(self):
        """return a string representation of a hand"""
        s = ""
        for item in self.deck:
            s += str(item[0])+ str(item[1])+" "
        return s
    
my_deck = Deck() 
A_player = Hand()
A_dealer = Hand()
blackJack_Table = [A_player, A_dealer, my_deck]
    
#define event handlers for buttons
def deal():
    global outcome, in_play, blackJack_Table
    blackJack_Table[2].shuffle()
    blackJack_Table[1].add_card(blackJack_Table[2].deal_card())
    blackJack_Table[1].add_card(blackJack_Table[2].deal_card())
    blackJack_Table[0].add_card(blackJack_Table[2].deal_card())
    blackJack_Table[0].add_card(blackJack_Table[2].deal_card())
    in_play = True
    

def hit():
    """replace with your code below if the hand is in play, hit the player """
    """if busted, assign a message"""
    global outcome, in_play, blackJack_Table
    outcome = " HIT OR STAND ?"
    
    if(blackJack_Table[0].get_value <= 21):
        blackJack_Table[0].add_card(blackJack_Table[2].deal_card())
    else:
        print "You have busted"
        
    return blackJack_Table
        
       
def stand():
    """replace with your code below if hand is in play, repeatedly hit dealer"""
    """until his hand has value 17 or more assign a message to outcome,"""
    """update in_play and score"""
    global outcome, blackJack_Table,score
    outcome = " NEW DEAL ?"        
    while(blackJack_Table[1].get_value < 17):
             hit()
        
    #if the dealer busts
    if((blackJack_Table[1].get_value() > blackJack_Table[0].get_value()) and (blackJack_Table[0].get_value() == 21)):
        print "The dealer is busted"
    else:
        if(blackJack_Table[0].get_value() <= blackJack_Table[1].get_value()):
            print "The player wins"
            score +=1
        else:
            print "The dealer wins ties"
            score -=1
            
    return blackJack_Table

# draw handler   
  
def draw(canvas):
    """test to make sure that card.draw works, replace with your code below"""
    global blackJack_Table
    canvas.draw_text('BLACKJACK',(250,550), 18, 'Black', 'serif')
    canvas.draw_text('PLAYER',(50,70), 18, 'Black', 'serif')
    canvas.draw_text('DEALER',(50,280), 18, 'Black', 'serif')
    canvas.draw_text('SCORE :',(380,250), 18, 'Black', 'serif')
    canvas.draw_text(str(score),(450,250), 18, 'Black', 'serif')
    canvas.draw_text(outcome,(350,280), 18, 'Black', 'serif')
    
    
    blackJack_Table[0].draw(canvas, [CARD_SIZE[0], CARD_SIZE[1]])
    blackJack_Table[1].draw(canvas, [CARD_SIZE[0], CARD_SIZE[1]*3])
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
      
#####################################################
# Test code

c1 = Card("S", "A")
print c1
print c1.get_suit(), c1.get_rank()
print type(c1)

c2 = Card("C", "2")
print c2
print c2.get_suit(), c2.get_rank()
print type(c2)

c3 = Card("D", "T")
print c3
print c3.get_suit(), c3.get_rank()
print type(c3)


###################################################
# Output to console
#SA
#S A
#<class '__main__.Card'>
#C2
#C 2
#<class '__main__.Card'>
#DT
#D T
#<class '__main__.Card'>

###################################################
# Test code

c1 = Card("S", "A")
c2 = Card("C", "2")
c3 = Card("D", "T")
print c1, c2, c3
print type(c1), type(c2), type(c3)

test_hand = Hand()
print test_hand

test_hand.add_card(c1)
print test_hand

test_hand.add_card(c2)
print test_hand

test_hand.add_card(c3)
print test_hand

print type(test_hand)


###################################################
# Output to console
# note that the string representation of a hand will 
# vary based on how you implemented the __str__ method

#SA C2 DT
#<class '__main__.Card'> <class '__main__.Card'> <class '__main__.Card'>
#Hand contains 
#Hand contains SA 
#Hand contains SA C2 
#Hand contains SA C2 DT 
#<class '__main__.Hand'>

###################################################
# Test code

test_deck = Deck()
print test_deck
print type(test_deck)

c1 = test_deck.deal_card()
print c1
print type(c1)
print test_deck

c2 = test_deck.deal_card()
print c2
print type(c2)
print test_deck

test_deck = Deck()
print test_deck
test_deck.shuffle()
print test_deck
print type(test_deck)

c3 = test_deck.deal_card()
print c3
print type(c3)
print test_deck


###################################################
# Output to console
# output of string method for decks depends on your implementation of __str__
# note the output of shuffling is randomized so the exact order of cards
# need not match

#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK 
#<class '__main__.Deck'>
#DK
#<class '__main__.Card'>
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ 
#DQ
#<class '__main__.Card'>
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ 
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK 
#Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 H5 
#<class '__main__.Deck'>
#H5
#<class '__main__.Card'>
#Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 

###################################################
# Test code

c1 = Card("S", "A")
c2 = Card("C", "2")
c3 = Card("D", "T")
c4 = Card("S", "K")
c5 = Card("C", "7")
c6 = Card("D", "A")

test_hand = Hand()
print test_hand
print test_hand.get_value()

test_hand.add_card(c2)
print test_hand
print test_hand.get_value()

test_hand.add_card(c5)
print test_hand
print test_hand.get_value()

test_hand.add_card(c3)
print test_hand
print test_hand.get_value()

test_hand.add_card(c4)
print test_hand
print test_hand.get_value()

test_hand = Hand()
print test_hand
print test_hand.get_value()

test_hand.add_card(c1)
print test_hand
print test_hand.get_value()

test_hand.add_card(c6)
print test_hand
print test_hand.get_value()

test_hand.add_card(c4)
print test_hand
print test_hand.get_value()

test_hand.add_card(c5)
print test_hand
print test_hand.get_value()

test_hand.add_card(c3)
print test_hand
print test_hand.get_value()

###################################################
# Output to console
# note that the string representation of a hand may vary
# based on your implementation of the __str__ method

#Hand contains 
#0
#Hand contains C2 
#2
#Hand contains C2 C7 
#9
#Hand contains C2 C7 DT 
#19
#Hand contains C2 C7 DT SK 
#29
#Hand contains 
#0
#Hand contains SA 
#11
#Hand contains SA DA 
#12
#Hand contains SA DA SK 
#12
#Hand contains SA DA SK C7 
#19
#Hand contains SA DA SK C7 DT 
#29



