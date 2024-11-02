from collections import OrderedDict
import random

player_number  = 0
comp_number = 0

# python interpreter
# Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32

# @Author(Aymar Sedami NAHUM)
# @Version(11/01/2024)

# Step 1. and  Step 2.
def name_to_number():

    """ From a helper function that converts name into a number to a dict"""
    
    dict_name_to_number = OrderedDict()
    dict_name_to_number["rock"] = 0
    dict_name_to_number["paper"] = 1
    dict_name_to_number["scissors"] = 2
    dict_name_to_number["lizard"] = 3
    dict_name_to_number["spock"] = 4
    
    #for key in dict_name_to_number.items():
    #    print(key)
    
    return dict_name_to_number
    
# Step 3.
def rpsls_first_part():
    global player_number
    choices = ["ROCK", "PAPER", "SPOCK", "LIZARD", "SCISSORS"]
    print(" ")
    
    print("Dear Player")
    print("Choose between those five : ")
    print("rock, spock, paper, lizard, scissors")
    
    player_choice = input(" ")
    
    print("")
    print(player_choice)
    
    # then compute the number
    
    try:
    
        for k , v in name_to_number().items():
            if choices.index(player_choice.upper()) == -1:
                print("That choice is not in the rpsls list")
            
    except ValueError as e:
    
        print("That choice is not allowed")
        
    for k , v in name_to_number().items():
        if k == player_choice:
            player_number  = name_to_number()[k]
            print("player_number  : " + str(player_number ))
            return player_number 
                    
rpsls_first_part()

# Step 4.
def rpsls_second_part():
    global comp_number
    print(" ")
    print(" The computer guess is : ")
    comp_number = random.randrange(5)
    for value in name_to_number().values():
        if comp_number == value : 
            print(comp_number)
            return comp_number
    
rpsls_second_part()

# Spep 5.
def rpsls_last_part():
    global comp_number
    global player_number

    print(" ")
    
    if((comp_number - player_number) == 0):
        print ("That is a tie. Try again ")
    
    if(comp_number > player_number):
        if(comp_number - player_number  <= 2):
            print ("The computer wins. ")
        #elif:
        else:
            print(" You wins !!! ")
        
    elif(player_number  > comp_number):
        if(player_number  - comp_number <= 2):
            print(" You wins !!! ")
        #elif:
        else:
            print(" The computer wins. ")
                     
rpsls_last_part() 




    
    
   