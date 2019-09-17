# Rock-paper-scissors-lizard-Spock template

import random

def name_to_number(name):
    
    if name=="rock":
        name = 0
        return name
    elif name=="Spock":
        name = 1
        return name
    elif name=="paper":
        name = 2
        return name
    elif name=="lizard":
        name = 3
        return name
    elif name=="scissors":
        name = 4
        return name
    else:
        return "Error wrong string"
    

  
def number_to_name(number):
    if number==0:
        number = "rock"
        return number
    elif number==1:
        number = "Spock"
        return number
    elif number==2:
        number = "paper"
        return number
    elif number==3:
        number = "lizard"
        return number
    elif number==4:
        number = "scissors"
        return number
    else:
        return "Error wrong number"
    
  
    

def rpsls(player_choice): 
    # print a blank line to differents games
    print("")
    # print out the message for the player's choice
    print "Player chooses",player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    computer = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    CPU = number_to_name(computer)
    # print out the message for computer's choice
    print "Computer chooses",CPU
    # compute difference of comp_number and player_number modulo five
    compute = (computer - player_number)%5
    # use if/elif/else to determine winner, print winner message
    if(computer == player_number):
        print "Player and computer tie!"
    elif(compute == 3 or compute == 4):
        print "Computer wins!"
    elif(compute == 1 or compute == 2):
        print "Player wins!"
    else:
        print "Error"
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


