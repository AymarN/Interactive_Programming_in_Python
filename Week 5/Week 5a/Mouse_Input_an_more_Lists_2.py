
###################################################
# Copy and paste the code in codeSkulptor to see how it works
# Circle clicking problem
# @author (Aymar N.) 
# @version (2020) Version 1

import simplegui
import math

# define global constants
RADIUS = 20
RED_POS = [50, 100, "Red"]
GREEN_POS = [150, 100, "Green"]
BLUE_POS = [250, 100, "Blue"]

# define helper function
def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define mouseclick handler
def click(pos):
    global GREEN_POS,RED_POS,BLUE_POS
    if dist([GREEN_POS[0],GREEN_POS[1]],pos) < RADIUS:
        GREEN_POS[2] = "Green" 
    if dist([RED_POS[0],RED_POS[1]],pos) < RADIUS:
        RED_POS[2] = "Red"
    if dist([BLUE_POS[0],BLUE_POS[1]],pos) < RADIUS:
        BLUE_POS[2] = "Blue"
          

# define draw
def draw(canvas):
    canvas.draw_circle([RED_POS[0],RED_POS[1]], RADIUS, 1, "Red",RED_POS[2])
    canvas.draw_circle([GREEN_POS[0],GREEN_POS[1]], RADIUS, 1, "Green",GREEN_POS[2])
    canvas.draw_circle([BLUE_POS[0],BLUE_POS[1]], RADIUS, 1, "Blue", BLUE_POS[2])
    
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()

###################################################
# Sample output

#Clicked red ball
#Clicked green ball
#Clicked blue ball
#Clicked green ball
#Clicked red ball
#Clicked green ball
#Clicked blue ball
