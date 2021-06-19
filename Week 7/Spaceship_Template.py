# @author (Aymar N.) 
# @version (2021) Version 2.0.0

# How to run the program
# Copy and paste the code in codeSkupltor
# https://py2.codeskulptor.org/

# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
FIRING_ANGLE_VEL_INC = 0.03
n = 0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
    
    def set_animated(self, value):
        self.animated = value
  
   
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
#ship_info = ImageInfo([90, 45], [180, 90], 45)

ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        #self.animated = info.set_animated(True)
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        canvas.draw_image(ship_image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):
        """\11.Up to this point, your ship will never slow down. Finally, add friction 
        to the ship's update method as shown in the "Acceleration and Friction" video
        by multiplying each component of the velocity by a number slightly less than 1 during each update."""
        
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # Friction update
        self.pos[0] *= (1 - FIRING_ANGLE_VEL_INC)
        self.pos[1] *= (1 - FIRING_ANGLE_VEL_INC)
        
        #You will need to update the velocity vector by a small fraction of the foward acceleration
        #vector so that the ship does not accelerate too fast.
        self.forward = angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0] += (self.forward[0] / 15)
            self.vel[1] += (self.forward[1] / 15)
      
    def increment_vel(self):
        self.angle_vel += FIRING_ANGLE_VEL_INC
        return self.angle_vel
    
    def decrement_vel(self):
        self.angle_vel -= FIRING_ANGLE_VEL_INC
        return self.angle_vel
    
    def swich_truster(self):
        if self.thrust == False:
            self.thrust = True
            ship_thrust_sound.play()
            print("thurster Activated")
            
    def reverse(self):
        self.vel[0] -= (self.forward[0] / 5)
        self.vel[1] -= (self.forward[1] / 5)
        
    def wrap_around(self):
        """\10.Then, modify the ship's update method such that the ship's position wraps
        around the screen when it goes off the edge(use modular arithmetic!)."""
        
        self.pos[0] = ((self.pos[0] % WIDTH )+ WIDTH) % WIDTH;    
        self.pos[1] = ((self.pos[1] % HEIGHT) + HEIGHT ) % HEIGHT;
        border_x = self.pos[0] #+ self.image_size[0];               #get right and bottom
        border_y = self.pos[1] #+ self.image_size[1];
        
        if(border_x > WIDTH):                               #check if touching right side
            #ctx.drawImage(img, x1 - canW, y1);             # draw left copy
            self.pos[0] = self.pos[0] - WIDTH
            #self.pos[1] = self.pos[1]
            if( border_y > HEIGHT):                         # check if touching bottom
                #ctx.drawImage(img, x1 - canW, y1 - canH);  # draw top copy
                self.pos[0] = self.pos[0] - WIDTH
                self.pos[1] = self.pos[1] - HEIGHT
    
        if(border_y > HEIGHT):
            #ctx.drawImage(img, x1 , y1 - canH);            # draw top copy
            #self.pos[0] = self.pos[0]
            self.pos[1] = self.pos[1] - HEIGHT
        
            
    def shoot(self):
        """\1. Add a shoot method to your ship class. This should spawn a new missile
        For now just replace the old missile in a_missile. The missile's initial position should be
        the tip of your ship's cannon.Its velocity should be the sum of the ship's velocity an a multiple of
        the ship's forward vector."""
        global a_missile
        a_missile = Sprite([(self.pos[0] + (FIRING_ANGLE_VEL_INC * self.image_size[0])), (self.pos[1] +(FIRING_ANGLE_VEL_INC * self.image_size[1]))], [(self.vel[0]+ (3 * self.forward[0])),(self.vel[1]+ (3 * self.forward[1]))], 0, 0, 
                           missile_image, missile_info, missile_sound)
  
        missile_sound.play()                                                                      
    # Sprite class
    
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        """\ 1. Complete the Sprite class by modifying the draw handler to draw the actual image and the update
        handler to make the sprite move and rotate.Rocks do not accelerate or experience friction, so the sprite
        update method should be simpler than the ship update method. Test this by giving a_rock different starting
        parameters and ensuring it behaves as you expect."""
        
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
    def wrap_around(self):
        """\10.Then, modify the ship's update method such that the ship's position wraps
        around the screen when it goes off the edge(use modular arithmetic!)."""
        
        self.pos[0] = ((self.pos[0] % WIDTH )+ WIDTH) % WIDTH;    
        self.pos[1] = ((self.pos[1] % HEIGHT) + HEIGHT ) % HEIGHT;
        border_x = self.pos[0] #+ self.image_size[0];               #get right and bottom
        border_y = self.pos[1] #+ self.image_size[1];
        
        if(border_x > WIDTH):                               #check if touching right side
            #ctx.drawImage(img, x1 - canW, y1);             # draw left copy
            self.pos[0] = self.pos[0] - WIDTH
            #self.pos[1] = self.pos[1]
            if( border_y > HEIGHT):                         # check if touching bottom
                #ctx.drawImage(img, x1 - canW, y1 - canH);  # draw top copy
                self.pos[0] = self.pos[0] - WIDTH
                self.pos[1] = self.pos[1] - HEIGHT
    
        if(border_y > HEIGHT):
            #ctx.drawImage(img, x1 , y1 - canH);            # draw top copy
            #self.pos[0] = self.pos[0]
            self.pos[1] = self.pos[1] - HEIGHT
        
        if(border_x > WIDTH):                               
            self.pos[0] = self.pos[0] - WIDTH
            if( border_y > HEIGHT):                        
                self.pos[0] = self.pos[0] - WIDTH
                self.pos[1] = self.pos[1] - HEIGHT
    
        if(border_y > HEIGHT):
            self.pos[1] = self.pos[1] - HEIGHT
    
# define keyhandlers to control firing_angle

def keydown(key):
    global my_ship
    if simplegui.KEY_MAP["up"] == key:
        my_ship.swich_truster() 
    elif simplegui.KEY_MAP["left"] == key:
        my_ship.decrement_vel()
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.increment_vel()
    elif simplegui.KEY_MAP["space"] == key: 
        my_ship.shoot()
    elif simplegui.KEY_MAP["down"] == key: 
        my_ship.reverse()
                                                                             

def keyup(key):
    global my_ship
    if simplegui.KEY_MAP["up"] == key:
        my_ship.thrust = False
        ship_thrust_sound.rewind()
        print("thurster deactivated")
    elif simplegui.KEY_MAP["left"] == key:
        my_ship.increment_vel()
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.decrement_vel()
    elif simplegui.KEY_MAP["space"] == key:                                                                        
        missile_sound.rewind()
   
        
def draw(canvas):
    global time
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text("LIVES"+"   "+str(lives), [(WIDTH * 4/5), HEIGHT // 4], 35, 'Gray')
    canvas.draw_text("SCORE "+str(score), [(WIDTH *4/5), HEIGHT // 5], 35, 'Gray')
    
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
    
    # Wrap_around
    my_ship.wrap_around()
    a_rock.wrap_around()
            
def rock_spawner():
    """timer handler that spawns a rock"""
    """event handler for timer with 1 sec interval"""
    global a_missile
    global n, a_rock
    n += 1
    a_rock = Sprite([(WIDTH / 3 * n), (HEIGHT / 3 * n)], [1, 1], 0, 0.05, asteroid_image, asteroid_info)
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
# Experiment with different positions and angles

my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([random.randint(0, WIDTH), random.randint(0, HEIGHT)], [random.randint(0, 3), random.randint(0,3)], 0, (random.randrange(0, 14)/ 10.0), asteroid_image, asteroid_info) 
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
a_missile = Sprite([(my_ship.image_size[0]+ my_ship.image_center[0]), (my_ship.image_size[1]+ my_ship.image_center[1])], [-1,1], 0, 0, missile_image, missile_info, missile_sound)


# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()



