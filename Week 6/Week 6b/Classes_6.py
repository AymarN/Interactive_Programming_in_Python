# Solution 6
   
class Tile:
    def __init__(self,number,exp):
        self.number = number
        self.exp = exp
        
    def __str__(self):
        s = "Number is " +str(self.number) +" ,"
        s+= " exposed is " + str(self.exp)
        return s
        
    def get_number(self):
        return self.number
    
    def is_exposed(self):
        return self.exp
    
    def expose_tile(self):
         self.exp = True
    
    def hide_tile(self):
         self.exp = False
            
    
my_tile = Tile(3, True)
your_tile = Tile(4, False)
  
##################################################################
# Testing code

print my_tile
print my_tile.get_number()
print my_tile.is_exposed()
my_tile.hide_tile()
print my_tile.is_exposed()
my_tile.expose_tile()
print my_tile.is_exposed()

print your_tile
print your_tile.get_number()
print your_tile.is_exposed()
your_tile.hide_tile()

print your_tile.is_exposed()
your_tile.expose_tile()
print your_tile.is_exposed()

#################################################################





