# implementation of Spaceship - program template for RiceRocks
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
count_update = 0
started = False


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

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
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
# .ogg versions of sounds are also available, just replace .mp3 by .ogg
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

def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def process_sprite_group(elm_group, canvas):
    """\3.Create a helper function process_sprite_group.This function
    should take a set and a canvas and call the update and draw methods for
    each sprite in the group.
    3.Missiles.4 Modify process_sprite_group to check the return value of update 
    for sprites.If it returns True, remove the sprite from the group. Again,you will
    want to iterate over a copy of the sprite group in process_sprite_group to avoid 
    deleting from the same set over which you are iterating."""
    a_set = set(elm_group)
    for elem in a_set:
        elem.draw(canvas)
        if elem.update():
            elm_group.remove(elem)
                    
def group_collide(group, other_object):
    """\2.Collisions.2 Implement a group_collide helper function.This function should 
    take a set group and a sprite other_object and check for collisions between other_object
    and elements of the group. If there is a collision, the colliding object should be removed 
    from the group.This function should return True or False depending on Whether there was a
    collision."""
    global rock_group, lives
    my_set = set(group)
    for elem in  my_set:
        if elem.collide(other_object):
            rock_group.discard(elem)
            return True
        else:
            return False
    
    
    
def group_group_collide(group_missile, group_rock):
    """\4.Collisions.1 Implement a final helper function group_group_collide that takes two
    groups of object as input.group_group_collide should iterate through the elements of a copy
    of the first group using a for-loop and then call group_collide with each of these elements
    on the second group.group_group_collide should return the number of elements in the first group
    that collide with the second as well as delete these elements in the first group.You may find the 
    discard method for sets to be helpful here."""
    global score
    collision = 0
    another_set = set(group_missile)
    for elm in another_set:
        if group_collide(group_rock,elm):
            collision += 1
            group_missile.discard(elm)
            
    score += collision
    return score

            
# Ship class
class Ship:

    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, self.angle)
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        # update velocity
        if self.thrust:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .1
            self.vel[1] += acc[1] * .1
            
        self.vel[0] *= .99
        self.vel[1] *= .99
         # wrap around
        if self.pos[1] <= 0:
            self.pos[1] += HEIGHT
        elif self.pos[1] >= HEIGHT:
            self.pos[1] -= HEIGHT
        elif self.pos[0] <= 0:
            self.pos[0] += WIDTH
        elif self.pos[0] >= WIDTH:
            self.pos[0] -= WIDTH
        
    def turn_ship(self, leftOrRight):
        if leftOrRight == 1:        
            self.angle_vel = 0.06
        elif leftOrRight == 0:
            self.angle_vel = -0.06
        else:
            self.angle_vel = 0
    
    def thrusters_switch(self, flag):
        if flag == True:
            self.thrust = True
            ship_thrust_sound.play()
        else:
            self.thrust = False
            ship_thrust_sound.rewind()
  
    def shoot(self):
        """\3.Missiles.1 Modify your shoot method of my_ship to create a 
        new missile and add it to the missile_group"""
        global a_missile, missile_group
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)

    def get_position(self):
        return self.pos
        
    def get_radius(self):
        return self.radius
    
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
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)

    def update(self):
        """\3.Missiles.3 Increment the age of the sprite every time update is called
        If the age is greater than or equal to the lifespan of the sprite, then we 
        want to remove it. So, return False meaning we want to keep it if the age is 
        less than the lifespan and True meaning we want to remove it otherwise."""
        # update angle
        self.angle += self.angle_vel
      
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        # wrap around
        if self.pos[1] <= 0:
            self.pos[1] += HEIGHT
        elif self.pos[1] >= HEIGHT:
            self.pos[1] -= HEIGHT
        elif self.pos[0] <= 0:
            self.pos[0] += WIDTH
        elif self.pos[0] >= WIDTH:
            self.pos[0] -= WIDTH  
            
        #on screen age
        self.age += 1
        if self.age >= self.lifespan:
            return True #remove sprite
        else:
            return False #keep sprite
        
    def get_position(self):
        return self.pos
        
    def get_radius(self):
        return self.radius
        
    def collide(self, other_sprite):
        """\ 2.Collisions.1 Add a collide_method to the sprite class. This should take another_object
        as an argument and return true if there is a collision or false otherwise."""
        global lives
        collide = dist(self.pos, other_sprite.get_position())
        if(collide > (self.radius + other_sprite.get_radius())):
            return False
        else:
            print("Collisions detected")
            return True

               
        
# key handlers to control ship   
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
         my_ship.turn_ship(0)
    elif key == simplegui.KEY_MAP['right']:
         my_ship.turn_ship(1)
    elif key == simplegui.KEY_MAP['up']:
        my_ship.thrusters_switch(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
        
def keyup(key):
    if key == simplegui.KEY_MAP['left']:
        my_ship.turn_ship(-1)
    elif key == simplegui.KEY_MAP['right']:
        my_ship.turn_ship(-1)
    elif key == simplegui.KEY_MAP['up']:
        my_ship.thrusters_switch(False)
        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score, my_ship, rock_group, missile_group
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
   
    if not started and inwidth and inheight:
        lives = 3
        score = 0
        time = 0
        rock_group = set([])
        missile_group = set([])
        soundtrack.rewind()
        soundtrack.play()
        started = True

def draw(canvas):
    global time, started, rock_group, missile_group, lives, score, \
    collision
   
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
   
    # draw UI
    canvas.draw_text("Lives", [50, 50], 22, "White")
    canvas.draw_text("Score", [680, 50], 22, "White")
    canvas.draw_text(str(lives), [50, 80], 22, "White")
    canvas.draw_text(str(score), [680, 80], 22, "White")

    # draw ship and sprites
    my_ship.draw(canvas)

     
    # 1.Multiple Rocks.4 Call the process_sprite_group function on rock_group in
    # the draw handler.
    #5.Finish it off3.When you spawn rocks, you want to make sure they are 
    #some distance away from the ship.Otherwise, you can die when a rock spawns
    #on top of you, which isn't much fun. one single way to achieve this effect
    #to ignore a rock spawn event if the spawned rock is too close to the ship.
    
    process_sprite_group(rock_group, canvas)
    
    # 3.Missiles.2 In the draw handler, use your helper function process_sprite_group to process missile_group
    # While you can now shoot multiple, you will notice that they stick around forever. To fix this,
    # we need to modify the Sprite Class and the process_sprite_group function.
    
    process_sprite_group(missile_group, canvas)
    
    #In the draw handler, use the group_collide helper to determine if the ship hit any of the rocks.
    #If so, decrease the number of lives by one.Note that you could have negative lives at this point.
    if group_collide(rock_group, my_ship):
        lives -= 1
    #Call group_group_collide in the draw handler to detect missile/rock_collisions
    #Increment the score by the number of missile collisions.
    group_group_collide(missile_group, rock_group)

    # update ship and sprites
    my_ship.update()
    
    # Add a code to the draw handler such that if the number of lives become 0 the game
    #is reset and the splash screen appears. In particular set the flag started to False, 
    #destroy all rocks and [[prevent any more rocks for spawning until the game is restarted]]
    if lives == 0:
        started = False
        a_remove_set = set([])
        for rock in rock_group:
            a_remove_set.add(rock)
        rock_group.difference_update(a_remove_set) 
    if started == False:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH / 2 , HEIGHT / 2])
    elif started == True:
        soundtrack.play() 
# timer handler that spawns a rock    
def rock_spawner():
    """\ 1.Remove a_rock and replace it with rock_group.Initialize a rock group to 
    an empty set.Modify your rock_spawner to create a new rock, an instance of sprite
    object and add it to rock_group.
    
    2.Modify your rock spawner to limit the total number of rocks in the game.We suggest
    you limit it to 12. With too many rocks the game becomes less fun and the animation slows
    downs significantly"""
    global rock_group, my_ship
    rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
    rock_avel = random.random() * .2 - .1
    a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info)
    if(len(rock_group) < 12):
        if(dist(a_rock.get_position(),my_ship.get_position()) >= (2.0*(a_rock.get_radius() + my_ship.get_radius()))):
            rock_group.add(a_rock)
            #a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, .1, asteroid_image, asteroid_info)
   
            
# initialize stuff
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
soundtrack.play()
# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, .1, asteroid_image, asteroid_info)


rock_group = set([])
missile_group = set([])

# register handlers
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()