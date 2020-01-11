# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    """ initialize global variables""" 
    global secret_number
    global n
    print "New Game. Guess the number [0-100]"
    secret_number = random.randrange(0,100)
    n=7

# define event handlers for control panel
def range100():
    """button that changes the range to [0,100) and starts a new game""" 
    global secret_number
    global n
    secret_number = random.randrange(0,100)
    n = 7
    print ""
    print "New game. Choose between [0-100]"
    
def range1000():
    """button that changes the range to [0,1000) and starts a new game"""     
    global secret_number
    global n
    secret_number = random.randrange(0,1000)
    n = 10
    print ""
    print "New game.Choose between [0-1000]"
      
def input_guess(guess):
    """Event handler prints out the input String guess message """
    global n
    global secret_number
    message = int(guess)
         
    if n > 0:
        if message == secret_number:
            print "Guess was",message
            print "Correct"
            new_game()
        elif message < secret_number:
            print "Guess was",message
            print "Higher"
            n-=1
            print "Guess reamaining",n
            
        elif message > secret_number:
            print "Guess was",message
            print "Lower"
            n-=1
            print "Guess reamaining",n
            
    else:
        print "there is no guess remaining"
        print "The Secret number was",secret_number
        new_game()
    
# create frame
frame = simplegui.create_frame('Guess the number', 400, 400)
# register event handlers for control elements and start frame
button2 = frame.add_button('Range is [0,100]', range100, 150)
button3 = frame.add_button('Range is [0,1000]', range1000, 150)
# input field with the handler input_guess
the_input = frame.add_input('enter guesses', input_guess, 150)
frame.start()

# call new_game 
new_game()

#always remember to check your completed program 
#against the grading rubric