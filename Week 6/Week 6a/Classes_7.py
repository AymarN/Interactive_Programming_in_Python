# Add an draw method for Tile class

#################################################
# Student adds code where appropriate    

import simplegui

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
class Tile:
    #1# pass
    def __init__(self,number,exp, LOCATIONS):
        self.number = number
        self.exp = exp
        self.width = LOCATIONS[0]
        self.height = LOCATIONS[1]
        
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
        return self.exp
    def hide_tile(self):
        self.exp = False
        return self.exp
            
    def get_location(self):
        return self.width, self.height
            
    # draw method for tiles
    def draw_tile(self, canvas):
        if self.exp:
            canvas.draw_text(str(self.number).center(5), [self.width, self.height], 20, 'Red')
        else:
            canvas.draw_polygon([[self.width, 0], [(self.width+self.width), 0], 
                                 [(self.width+self.width), self.height], [self.width, self.height]], 3, 'Blue', 'Green')
            
# draw handler
def draw(canvas):
    tile1.draw_tile(canvas)
    tile2.draw_tile(canvas)
            
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * TILE_WIDTH, TILE_HEIGHT)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)
# create two tiles.make sure to update initializer  
tile1 = Tile(3, True, [0, TILE_HEIGHT])
tile2 = Tile(5, False, [TILE_WIDTH, TILE_HEIGHT])

# get things rolling
frame.start()
     
###################################################
# Resulting frame should display a tile with number 3 (left)
# and a tile with a green back (right)