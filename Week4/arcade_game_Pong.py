# @author (Aymar N.) 
# @version (2021) Version 2.0.0

# How to run the program
# Copy and paste the code in codeSkupltor
# https://py2.codeskulptor.org/

# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
vel = 4

ball_line_width = 1
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-1, -1]  # pixels per tick
time = 0
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel, paddle2_vel = 0, 0
score1, score2 = 0, 0

def paddle1_faster():
    global paddle1_vel, vel
    paddle1_vel += vel
    
def paddle2_faster():
    global paddle2_vel, vel
    paddle2_vel += vel
    
def paddle1_slower():
    global paddle1_vel, vel
    paddle1_vel -= vel
    
def paddle2_slower():
    global paddle2_vel, vel
    paddle2_vel -= vel

inputs = {
    'up': paddle2_slower, 
    'down': paddle2_faster,
    'w': paddle1_slower,
    's': paddle1_faster
}

def spawn_ball(direction):
    """\ 2.Add code that spawns a ball in the middle of the table
    5.Add randomization to the velocity."""
    
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    # The velocity of the ball should be upwards.
    ball_vel[1] = - random.randrange(1, 3)
    #Towards the right while direction is right.
    if direction == "RIGHT":
        ball_vel[0] = (random.randrange(2, 4)) 
    #Towards the left while direction is right.   
    if direction == "LEFT":
        ball_vel[0] = - (random.randrange(2, 4))
       
             
# define event handlers
def new_game():
    """\ 3.Add a call to spawn_ball in new_game which starts a game of Pong 
    14. Add code to new_game which resets the score before calling spawn_ball. """
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2 
    score1, score2 = 0, 0
    spawn_ball("RIGHT")
    
def draw(canvas):
    """global variables which contain the vertical velocities of the paddles"""
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel  
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
     
    # 4. change the code such that the ball collides with and bounces off of
    # the top and bottom walls
    if (ball_pos[1] + BALL_RADIUS + ball_line_width >= HEIGHT) or \
    (ball_pos[1] - BALL_RADIUS - ball_line_width <= 0):
        ball_vel[1] = - ball_vel[1]
    
    # update ball
    ball_pos[0] +=  ball_vel[0]
    ball_pos[1] +=  ball_vel[1]   
       
    # 1.Add code to the program template that draws a ball moving across
    # a pong table.
    canvas.draw_circle(ball_pos, BALL_RADIUS, ball_line_width, 'White', 'White')
    # update paddle's vertical position, keep paddle on the screen
    
    # 8.Add code that alters the values of these vertical positions via an update
    # in the draw handler.In the template, the variables were paddle1_vel and paddle2_vel
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and \
    paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and \
    paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
        #print paddle2_pos - HALF_PAD_HEIGHT
        
    # 7.Add code that draws the left and right paddles in their 
    # respective gutters
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT], \
                         [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], \
                         [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], \
                         [0, paddle1_pos + HALF_PAD_HEIGHT]], 1, 'White', 'White')
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], \
                         [WIDTH, paddle2_pos - HALF_PAD_HEIGHT], \
                         [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], \
                         [WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 1, 'White', 'White')
    
    # 6.Add code to the draw handler that tests whether the ball [collides] with
    # the left and the right gutters. Remember the gutters are ... the width of
    # the paddle.
    
    if (ball_pos[0] + BALL_RADIUS + ball_line_width >= WIDTH - PAD_WIDTH):
        #change your collision code for the left and right gutters in step 6 to check
        #whether the ball is actually striking a paddle when it touches a gutter.
        #12.increase the velocity of the ball by 10% each time it strikes a paddle.
        
        if ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT and \
        ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = - 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
        #6.when the ball touches a gutter, use either spawn_ball(LEFT)|spawn_ball(RIGHT)
        #to respawn.
        #13.Each time the ball strikes the left or the right gutter
        #the opposite player receives a point and the ball is respawned appropriately.
        
        else:
            score1 += 1
            spawn_ball("LEFT")
    if (ball_pos[0] - BALL_RADIUS - ball_line_width <= PAD_WIDTH):
        if ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT and \
        ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = - 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1] 
        else:
            score2 += 1
            spawn_ball("RIGHT")
            
    # print ball_vel[0]
    # 13. Add scoring to the game.
    canvas.draw_text(str(score1), (WIDTH/4, HEIGHT/4), 50, 'White')
    canvas.draw_text(str(score2), (WIDTH*3/4, HEIGHT/4), 50, 'White')
    
def keydown(key):
    """\9. Update the values of these two vertical velocities using key handlers
    q and a keys control the constant vertical velocity of the left paddle
    up and down keys control the constant vertical velocity of the right paddle"""
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i]()
    
def keyup(key):
    """\9. Update the values of these two vertical velocities using key handlers
    q and a keys control the vertical velocity of the left paddle
    up and down keys control the vertical velocity of the right paddle."""
    global paddle1_vel, paddle2_vel
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            paddle1_vel = 0
            paddle2_vel = 0
            
   
    # create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
# 14.Add a "Restart" button that calls new_game to reset the score and relaunch the ball
new_game = frame.add_button('Restart', new_game, 100)

# start frame
#new_game()
frame.start()
