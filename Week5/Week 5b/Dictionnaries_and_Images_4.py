# Image positioning problem
# Copy and paste the code in codeSkulptor to see how it works
# @author (Aymar N.) 
# @version (2020) Version 1

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300
img_pos = [WIDTH // 2, HEIGHT // 2]

# load test image
test_image = simplegui.load_image("https://snipboard.io/eqSEJN.jpg")
test_image_size = [95,93]
test_image_center = [test_image_size[0] // 2, test_image_size[1]// 2]

# mouseclick handler
def click(pos):
    global img_pos
    img_pos= list(pos)


# draw handler
def draw(canvas):
    canvas.draw_image(test_image, test_image_center, test_image_size, 
            img_pos, test_image_size)


# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)

# register enev handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)    


# start frame
frame.start()
        
                               