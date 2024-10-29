###################################################
#Day to number problem
#@author (Aymar N.) 
# @version (2021) Version 1

# How to run the program
# Copy and paste the code in codeSkupltor
# https://py2.codeskulptor.org/

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

###################################################

# define day to number
def day_to_number(day):
    return day_list.index(day)

# Test data
print(day_to_number("Sunday"))
print(day_to_number("Monday"))
print(day_to_number("Tuesday"))
print(day_to_number("Wednesday"))
print(day_to_number("Thursday"))
print(day_to_number("Friday"))
print(day_to_number("Saturday"))

###################################################
# Sample output
