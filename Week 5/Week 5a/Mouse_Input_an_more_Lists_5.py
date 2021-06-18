###################################################
#Complete the given program template to produce a program that fills the canvas 
#with a 10x10 grid of touching balls of the given size
#@author (Aymar N.) 
#@version (2021) Version 1

# How to run the program
# Copy and paste the code in codeSkupltor
# https://py2.codeskulptor.org/

import simplegui
ball_pos = [20,20]
ball_color = "Red"
BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS

# define draw
def draw(canvas):
    for i in range(WIDTH/BALL_RADIUS):
        for j in range(HEIGHT/BALL_RADIUS):
            canvas.draw_circle([(ball_pos[0])*i,(ball_pos[1])*j], BALL_RADIUS, 1, "Black", ball_color)
                      
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()
