###################################################
#Copy and paste the code in codeSkulptor to see how it works
#Day to number problem
#@author (Aymar N.) 
# @version (2020) Version 1

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
