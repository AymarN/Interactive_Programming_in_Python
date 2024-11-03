
# python interpreter
# Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
# @Author(Aymar Sedami NAHUM)
# @Version(11/01/2024)

from collections import OrderedDict
import random

class RPSLS:

    def __init__(self, player_number, comp_number):

        self.player_number  = player_number
        self.comp_number = comp_number
    
    # Step 1. and  Step 2.
    def name_to_number(self):
        """ From a helper function that converts name into a number to a dict"""
      
        self.dict_name_to_number = OrderedDict()
        self.dict_name_to_number["rock"] = 0
        self.dict_name_to_number["paper"] = 1
        self.dict_name_to_number["scissors"] = 2
        self.dict_name_to_number["lizard"] = 3
        self.dict_name_to_number["spock"] = 4
    
        #for key in dict_name_to_number.items():
        #print(key)
    
        return self.dict_name_to_number
    
    # Step 3.
    def rpsls_first_part(self):
        """ A method that returns the player choice"""
        
        self.choices = ["ROCK", "PAPER", "SPOCK", "LIZARD", "SCISSORS"]
        print(" ")
        print("Dear Player")
        print("Choose between those five : ")
        print("rock, spock, paper, lizard, scissors")
    
        self.player_choice = input(" ")
    
        print("")
        print(self.player_choice)
    
    # then compute the number
    
        try:
        
            if self.choices.index(self.player_choice.upper()) == -1:
                print("That choice is not in the list.")
                
            for k , v in self.name_to_number().items():
                if k == self.player_choice:
                    self.player_number  = self.name_to_number()[k]
                    print("The player_number is : " + str(self.player_number ))
    # v1                     
        except ValueError as e:
            print("That choice is not allowed, try one more time :")
            self.player_choice = input(" ")
            
    # Step 4.
    def rpsls_second_part(self):
        """ A method that returns the computer choice"""
        
        print(" ")
        print(" The computer guess is : ")
        self.comp_number = random.randrange(5)
        for value in self.name_to_number().values():
            if self.comp_number == value : 
                print(self.comp_number)
                return self.comp_number
    
    # Spep 5.
    def rpsls_last_part(self):
        """ A method that returns the winner"""
        print(" ")
    
        if((self.comp_number - self.player_number) == 0):
            print ("That is a tie. Try again ")
    
        if(self.comp_number > self.player_number):
            if(self.comp_number- self.player_number  <= 2):
                print ("The computer wins. ")
            #elif:
            else:
                print(" You wins !!! ")
        
        elif(self.player_number  > self.comp_number):
            if(self.player_number  - self.comp_number <= 2):
                print(" You wins !!! ")
            #elif:
            else:
                print(" The computer wins. ")
                
    def __str__(self):
        
        self.instructions = " RPSLS, each choice wins against the preceding two choices and loses"
        self.instructions = self.instructions + " RPSLS, each choice wins against the preceding two choices and loses"
        self.instructions = self.instructions + " against the following two choices. "
        self.expandedList = " • 0 — rock • 1 — Spock • 2 — paper • 3 — lizard • 4 — scissors "
        
        return "\n" + self.instructions + "\n" + self.expandedList
                

Game_RPLS = RPSLS(0, 0)
print(Game_RPLS)
Game_RPLS.name_to_number()
Game_RPLS.rpsls_first_part()
Game_RPLS.rpsls_second_part()
Game_RPLS.rpsls_last_part()

                    




    
    
   