# template for "Stopwatch: The Game"
import time
import simplegui
# define global variables
n = 0
WIDTH = 300
HEIGTH = 300
#timer interval
interval = 100
total_stop = 0
success_stop = 0
message = "0:00.0"

def format(time_in_seconds):
    """ helper function format that converts time """
    """ in tenths of seconds into formatted string A:BC.D """
    # A ten of minutes 
    A = time_in_seconds // 600
    Intermediate_Operation =  time_in_seconds // 10
    amount_of_seconds = Intermediate_Operation %60
    # B Unity of minutes
    B = amount_of_seconds  // 10
    # C ten of seconds
    C = amount_of_seconds  % 10
    # D unity of seconds
    D = time_in_seconds % 10
    return str(A)+":"+str(B)+str(C)+"."+str(D)  
      
def Start():
    """Event handler to start the timer"""
    timer.start()

def Stop():
    """Event handler to Stop the timer"""
    timer.stop()
    global total_stop
    global success_stop
    total_stop += 1
    if n % 10 == 0:
        success_stop = success_stop + 1
    
def Reset():
    """Event handler to reset the timer"""
    #if timer.is_running():
    timer.stop()
    global n,message
    global total_stop
    global success_stop
    n = 0
    message = "0:00.0"
    total_stop=0
    success_stop=0
    
def display():
    global success_stop
    global total_stop
    return str(success_stop)+"/"+str(total_stop)
    
def tick():
    """event handler for timer with 0.1 sec interval"""
    global n, message
    n += 1
    message = format(n)
    
def draw(canvas):
    """Canvas Event handler which draws the current time"""
    global n
    global message
    canvas.draw_text(message, [WIDTH // 2, HEIGTH // 2], 35, 'Gray')
    canvas.draw_text(display(), [250, 20], 25, 'Gray')
      
# create frame
frame = simplegui.create_frame("STOPWATCH", WIDTH, HEIGTH)
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)

# register event handlers
frame.set_draw_handler(draw)
# format function called while registering the timer
timer = simplegui.create_timer(interval, tick)
# start frame
frame.start()
# Please remember to review the grading rubric


