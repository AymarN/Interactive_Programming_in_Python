###################################################
#Copy and paste the code in codeSkulptor to see how it works
#String list joining problem
#@author (Aymar N.) 
#@version (2020) Version 1

def string_list_join(string_list):
    sep = ""
    return sep.join(string_list)

###################################################
# Test data

print(string_list_join([]))
print(string_list_join(["pig", "dog"]))
print(string_list_join(["spam", " and ", "eggs"]))
print(string_list_join(["a", "b", "c", "d"]))


###################################################
#Output
#pigdog
#spam and eggs
#abcd