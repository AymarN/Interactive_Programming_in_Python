# @author (Aymar N.) 
# @version (2021) Version 2.0.0

# How to run the program
# Copy and paste the code in codeSkupltor
# https://py2.codeskulptor.org/


# Rock-paper-scissors-lizard-Spock template
import random

def name_to_number(name):
    """a helper function that converts name into a number"""
    
    if name=="rock":
        name = 0
        return name
    elif name=="paper":
        name = 1
        return name
    elif name=="scissors":
        name = 2
        return name
    elif name=="lizard":
        name = 3
        return name
    elif name=="Spock":
        name = 4
        return name
    else:
        return "Error wrong string"
    

def number_to_name(number):
    """converts a number into its matching String"""
    if number==0:
        number = "rock"
        return number
    elif number==1:
        number = "paper"
        return number
    elif number==2:
        number = "scissors"
        return number
    elif number==3:
        number = "lizard"
        return number
    elif number==4:
        number = "Spock"
        return number
    else:
        return "Error wrong number"
    
  
def rpsls(player_choice):
    """ Generates the computer's guess and print a message """
    """ Determines and prints out the winner """
    # print a blank line to differents games
    print("")
    # print out the message for the player's choice
    print "Player chooses",player_choice
    # convert the player's choice to player_number
    #using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using 
    #random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using
    #the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses",comp_choice
    # compute difference of comp_number and 
    #player_number modulo five
    compute = (comp_number - player_number)%5
    # use if/elif/else to determine winner, 
    #print winner message
    if(comp_number == player_number):
        print "Player and computer tie!"
    elif(compute == 3 or compute == 4):
        print "Computer wins!"
    elif(compute == 1 or compute == 2):
        print "Player wins!"
    else:
        print "Error"
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR 
#SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against 
#the grading rubric