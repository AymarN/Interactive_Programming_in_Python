# @author (Aymar N.) 
# @version (2021) Version 2.0.0

# How to run the program
# Copy and paste the code in codeSkupltor
# https://py2.codeskulptor.org/

# implementation of card game - Memory
import simplegui
import random
#import copy

WIDTH = 800
HEIGHT = 100
deck_Card,The_Game,exposed_List= [], [], []
card_index, index_Card1, index_Card2, turn_counter = 0, 0, 0, 0

# helper function to initialize globals
 
def new_game():
    """ Model the Deck of cards used in memory"""
    global state, deck_Card, turn_counter
    ListA = []
    ListB = []
    state = 0
    turn_counter = 0
    for i in range(8):
        ListA.append(i+1)
        ListB.append(i+1)
    #At the start of the game
    deck_Card = ListA + ListB
    # Shuffle the Deck
    random.shuffle(deck_Card)
    for item in deck_Card:
        exposed_List.append(False)
        #print (deck_Card[deck_Card.index(item)]), 
         
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global click_Handler, deck_Card , exposed_List, card_index, index_Card1
    global state, index_Card2, turn_counter 
    click_Handler = list(pos)
    
    if state == 0:
        for item in deck_Card:
            card_index = click_Handler[0]/ 50
            index_Card1 = card_index
            if(exposed_List[card_index] == False or exposed_List[card_index] == True):
                exposed_List[card_index] = True
            
        state = 1
        print "state1"
        return card_index
    elif state == 1:
        for item in deck_Card:
            card_index = click_Handler[0]/ 50
            index_Card2 = card_index
            if exposed_List[card_index] == False:
                exposed_List[card_index] = True
            
        state = 2
        print "state2"
        return card_index
    else:
        polygon = [((50 * (index_Card1)), 0), ((50 *(index_Card1+1)), 0), ((50 * (index_Card1+1)), 100), ((50 * (index_Card1)), 100)]
        if deck_Card[index_Card1] == deck_Card[index_Card2]:
            exposed_List[index_Card1] = True
            exposed_List[index_Card2] = True
            print "deck card 1",deck_Card[index_Card1]
            print "deck card 2",deck_Card[index_Card2]
            turn_counter +=1
            label.set_text("Turns = " + str(turn_counter))
        else:
            exposed_List[index_Card1] = False
            exposed_List[index_Card2] = False
        for item in deck_Card:
            card_index = click_Handler[0]/ 50
            index_Card1 = card_index
            if exposed_List[card_index] == False:
                exposed_List[card_index] = True
        
        state = 1
        print "state1"
        
        return card_index, state
  
# cards are logically 50x100 pixels in size    
def draw(canvas):
    """ Write a draw handler that iterates through the Deck """
    """ The result should be an horizontal sequence of evenly space numbers """
    global deck_Card , The_Game, exposed_List
    global card_index, index_Card1, index_Card2, state 
    my_index = 0
    for i in range(len(deck_Card)):
        polygon = [((50 * (i)), 0), ((50 *(i+1)), 0), ((50 * (i+1)), 100), ((50 * (i)), 100)]
        canvas.draw_text(str(deck_Card[i]).center(4), [(50 * i), 100], 35, 'Red')
        canvas.draw_polygon(polygon, 3, 'Blue', 'Green')
        
    for j in range(len(exposed_List)): 
        if exposed_List[card_index] == True:
            canvas.draw_polygon([((50 * (card_index)), 0), ((50 *(card_index+1)), 0), ((50 * (card_index+1)), 100), ((50 * (card_index)), 100)], 3, 'Blue', 'White')
            canvas.draw_text(str(deck_Card[card_index]).center(4), [(50 * card_index), 100], 35, 'Red')
            return exposed_List
        
        elif exposed_List[card_index] == False:
            exposed_List[card_index] = False
            return exposed_List
    
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.set_canvas_background("White")
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
label.set_text(str(turn_counter))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric


