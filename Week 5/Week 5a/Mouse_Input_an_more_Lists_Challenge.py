###################################################
#Copy and paste the code in codeSkulptor to see how it works
# Polyline drawing problem
#@author (Aymar N.) 
#@version (2020) Version 1

import simplegui
import math
WIDTH = 300
HEIGHT = 200
polyline = []
POLYLINE_COLOR = "red"
POINT_RADIUS = 4
remove = []

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    remove = []
    global polyline, polyline_color
    
    if remove == []:
        polyline.append(pos)
    else:
        for points in remove:
            polyline.pop(polyline.index(points))
        
# button to clear canvas
def clear():
    global polyline
    polyline = []

# define draw
def draw_handler(canvas):
    for i,points in enumerate(polyline):
        if (i == 0):
            canvas.draw_circle(points, POINT_RADIUS, 1,"Black", POLYLINE_COLOR)
            first_point = points
            print("points",first_point)
        if (i == 1):
            canvas.draw_circle(points, POINT_RADIUS, 1,"Black", POLYLINE_COLOR)
            second_point = points
            print("points",first_point,second_point)
            canvas.draw_line(first_point, second_point, 3, 'black')
        if (i == 2):
            canvas.draw_circle(points, POINT_RADIUS, 1,"Black", POLYLINE_COLOR)
            third_point = points
            canvas.draw_line(second_point, third_point, 3, 'black')
        if (i == 3):
            canvas.draw_circle(points, POINT_RADIUS, 1,"Black", POLYLINE_COLOR)
            fourth_point = points
            canvas.draw_line(third_point, fourth_point, 3, 'black')
        if (i == 4):
            canvas.draw_circle(points, POINT_RADIUS, 1,"Black", POLYLINE_COLOR)
            fifth_point = points
            canvas.draw_line(fourth_point, fifth_point, 3, 'black')
    
# create frame
frame = simplegui.create_frame("Echo click", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# Register handlers
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw_handler)
frame.add_button("Clear", clear)

# start frame
frame.start()