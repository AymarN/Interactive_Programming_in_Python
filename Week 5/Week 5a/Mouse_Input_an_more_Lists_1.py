# Practise exercices for Mouse and List Methods
# For each mouse click, print the position of the mouse click to the console
# Copy and paste the code in codeSkulptor to see how it works
# @author (Aymar N.) 
# @version (2020) Version 1

import simplegui
import math

# intialize globals
Mouse_list = []
WIDTH = 450
HEIGHT = 300

# define event handler for mouse click, draw
def click(pos):
    remove = []
    Mouse_list = list(pos)
    for msClick in Mouse_list:
        #print("Mouse click x and y position",pos[0],pos[1])
        print("iterate using the index",Mouse_list[Mouse_list.index(msClick)])
        print("iterate over the list",Mouse_list[0],Mouse_list[1])
#   Mouse_list.append([[pos[0],pos[1]])
    
    if remove == []:
        Mouse_list.append(pos)
    else:
        for msClick in remove:
            Mouse_list.pop(Mouse_list.index(msClick))
   
# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
#frame.set_draw_handler(draw)

# start frame
frame.start()


