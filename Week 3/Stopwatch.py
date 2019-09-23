# template for "Stopwatch: The Game"
import time
import simplegui
# define global variables
n = 0
WIDTH = 300
HEIGTH = 300
interval = 100
total_stop = 0
success_stop = 0
message = "0:00.0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    A = t // 600
    number =  t // 10
    amount_second = number %60
    B = amount_second // 10
    C = amount_second % 10
    D = t % 10
    return str(A)+":"+str(B)+str(C)+"."+str(D)  
    

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()

def Stop():
    timer.stop()
    global total_stop
    global success_stop
    total_stop += 1
    if n % 10 == 0:
        success_stop = success_stop + 1
    
def Reset():
    if timer.is_running():
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
    

# define event handler for timer with 0.1 sec interval
def tick():
    global n, message
    n += 1
    message = format(n)
    

# define draw handler
def draw(canvas):
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
timer = simplegui.create_timer(interval, tick)
# start frame
frame.start()




# Please remember to review the grading rubric

