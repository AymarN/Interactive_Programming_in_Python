# Challenge based on Demonstration of a magnifier on a map
#without drawing the image centered at the last mouse click
# Copy and paste the code in codeSkulptor to see how it works
# @author (Aymar N.) 
# @version (2020) Version 1

import simplegui

# 1667x1667 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("https://snipboard.io/NGSdmc.jpg")

# Scaling factor
SCALE = 3

# Size of magnifier pane and initial center
MAG_SIZE = 120
#mag_pos = [(image.get_width() // 3)// 2, (image.get_height() // 3)// 2]

# Event handlers
# Move magnifier to clicked position
def click(pos):
        global mag_pos
        mag_pos = list(pos)

# Draw map and magnified region
def draw(canvas):
    # Draw map
    if((image.get_width()!= 0) and (image.get_height() !=0)):
        #canvas.draw_image(image, [image.get_width() // 2, image.get_height() // 2], [image.get_width(), image.get_height()], 
                #mag_pos, [image.get_width() // 3, image.get_height() // 3])
        canvas.draw_image(image, 
                [image.get_width() // 2, image.get_height() // 2], [image.get_width(), image.get_height()], 
                [(image.get_width() // 3) // 2, (image.get_height() // 3)// 2], [image.get_width() // 3, image.get_height() // 3])

        # Draw magnifier
        mag_pos = [(image.get_width() // 3)// 2, (image.get_height() // 3)// 2]
        map_center = [SCALE * mag_pos[0], SCALE * mag_pos[1]]
        map_rectangle = [MAG_SIZE, MAG_SIZE]
        mag_center = [(image.get_width() // 3)// 2, (image.get_height() // 3)// 2]
        mag_rectangle = [MAG_SIZE, MAG_SIZE]
        canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)
    
# Create frame for scaled map
frame = simplegui.create_frame("Image magnifier", image.get_width() // 3, image.get_height() // 3)

# register even handlers
frame.set_mouseclick_handler(click)    
frame.set_draw_handler(draw)

# Start frame
frame.start(),