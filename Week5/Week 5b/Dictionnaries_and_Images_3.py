# Image debugging problem
# Copy and paste the code in codeSkulptor to see how it works
# @author (Aymar N.) 
# @version (2020) Version 1

import simplegui

# load test image
test_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png")
test_image_size = [135, 164]
test_image_center = [test_image_size[0] //2, test_image_size[1] //2]

# draw handler
def draw(canvas):
    canvas.draw_image(test_image, test_image_center, test_image_size, 
                      test_image_center, test_image_size)

# create frame and register draw handler    
frame = simplegui.create_frame("Test image", test_image_size[0], test_image_size[1])

# register enev handlers
frame.set_draw_handler(draw)

# start frame
frame.start()