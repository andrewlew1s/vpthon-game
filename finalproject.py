# MADE BY ANDREW LEWIS

from vpython import *
import random
from math import *

def random_color():
    """ returns a tuple of (r,g,b) randomly from 0.0 to 1.0
    """
    r = random.uniform(0.0,1.0)
    g = random.uniform(0.0,1.0)
    b = random.uniform(0.0,1.0)
    return (r,g,b)  # a color is a three-element tuple

def make_alien():
    """ makes an alien!
    """
    # ONE OF THE ALIENS HURT HIS NOSE BE NICE

    a = sphere( radius=1, color=vector(0,1,0) )
    b = sphere( radius=0.3, pos= vector(.7,.5,.2), color=vector(1,1,1) )
    c = cone( radius=0.2, pos= vector(.9,.2,.9), color=vector(1,0,0) )
    d = sphere( radius=0.3, pos= vector(.2,.5,.7), color=vector(1,1,1) )
    e = cylinder( pos= vector(0,.9,-.2), axis=vector(.02,.2,-.02),  # the hat!
              radius=.7, color=vector(1,0,1))
    
    alien = compound([a,b,c,d,e])
    alien.pos = vector(-13,-2,1)
    return alien 

def make_alien2():
    """ makes an alien!
    """
    
    a = sphere( radius=1, color=vector(0,1,0) )
    b = sphere( radius=0.3, pos= vector(.7,.5,.2), color=vector(1,1,1) )
    c = cone( radius=0.2, pos= vector(.9,.2,.9), color=vector(1,0,0) ) #another object for a mouth
    d = sphere( radius=0.3, pos= vector(.2,.5,.7), color=vector(1,1,1) )
    e = cylinder( pos= vector(0,.9,-.2), axis=vector(.02,.2,-.02),  # the hat!
              radius=.7, color=vector(1,0,1))

    alien2 = compound([a,b,c,d,e])
    alien2.pos = vector(-13,2,1)
    return alien2   # always use the _frame_, not any of its parts...

def make_alien3():
    """ makes an alien!
    """
    
    a = sphere( radius=1, color=vector(0,1,0) )
    b = sphere( radius=0.3, pos= vector(.7,.5,.2), color=vector(1,1,1) )
    c = cone( radius=0.2, pos= vector(.9,.2,.9), color=vector(1,0,0) ) #another object for a mouth
    d = sphere( radius=0.3, pos= vector(.2,.5,.7), color=vector(1,1,1) )
    e = cylinder( pos= vector(0,.9,-.2), axis=vector(.02,.2,-.02),  # the hat!
              radius=.7, color=vector(1,0,1))

    alien3 = compound([a,b,c,d,e])
    alien3.pos = pos= vector(-13,4,1)
    return alien3   # always use the _frame_, not any of its parts...

def make_alien4():
    """ makes an alien!
    """
    
    a = sphere( radius=1, color=vector(0,1,0) )
    b = sphere( radius=0.3, pos= vector(.7,.5,.2), color=vector(1,1,1) )
    c = cone( radius=0.2, pos= vector(.9,.2,.9), color=vector(1,0,0) ) #another object for a mouth
    d = sphere( radius=0.3, pos= vector(.2,.5,.7), color=vector(1,1,1) )
    e = cylinder( pos= vector(0,.9,-.2), axis=vector(.02,.2,-.02),  # the hat!
              radius=.7, color=vector(1,0,1))

    alien4 = compound([a,b,c,d,e])
    alien4.pos = vector(-13,6,1)
    return alien4   # always use the _frame_, not any of its parts...

def main():
    """ this is the main function, including all of the data objects 
        and the "event loop," which is the while True: loop that will
        become vPython's "time stream" :-)
    """
    # floor
    floor = box(length=80, height=30, width=.5, pos= vector(0,0,0), color=vector(0,2,0))

    # goals 
    goal1 = box(length=1.5, height=20,width=10, pos= vector(40,0,5), color=vector(1,1,1))
    goal2 = box(length=1.5, height=20,width=10, pos= vector(-40,0,5), color=vector(1,1,1))

    alien = make_alien()
    alien.vel = vector(0,0,0)
    alien2 = make_alien2()
    alien2.vel = vector(0,0,0)
    alien3 = make_alien3()
    alien3.vel = vector(0,0,0)
    alien4 = make_alien4()
    alien4.vel = vector(0,0,0)

    ball = sphere( radius=1, pos= vector(10,0,1), color=vector(1,0.7,0.2) )
    ball.vel = vector(0,0,0)
    ball2 = sphere( radius=1, pos= vector(3,0,1), color=vector(1,2,0.2) )
    ball2.vel = vector(0,0,0)
    ball3 = sphere( radius=1, pos= vector(0,1,2), color=vector(1,2,0.2) )
    ball3.vel = vector(0,0,0)
    
    gravity = 9.8
    RATE = 30                # the number of times the while loop runs each second
    dt = 1.0/(1.0*RATE)      # the time step each time through the while loop
    scene.autoscale = False  # avoids changing the view automatically
    
    while True:    # this is the "physics loop": each loop is one step in time, dt
        rate(RATE)
        count=0
        # maximum # of times per second the while loop runs 

        # +++ start of UPDATE SECTION - update all positions here, every time step

        ball.pos = ball.pos + ball.vel*dt
        ball2.pos = ball2.pos + ball2.vel*dt
        ball3.pos = ball3.pos + ball3.vel*dt
        alien.pos = alien.pos + alien.vel*dt
        alien2.pos = alien2.pos + alien2.vel*dt
        alien3.pos = alien3.pos + alien3.vel*dt
        alien4.pos = alien4.pos + alien4.vel*dt
        
        # +++ end of UPDATE SECTION - be sure new objects are updated appropriately!

        # +++ start of COLLISION SECTION - check for collisions + do the "right" thing

        # BALL BOUNDARIES
        
        if ball.pos.z < floor.pos.z:  # w0 has the smallest x value
            ball.pos.z = floor.pos.z  # make sure we stay in bounds
            ball.vel.z = -1.0 * ball.vel.z 
        
        if ball.pos.z > 15:
            ball.vel.z = ball.vel.z - gravity
        
        if ball.pos.y > 15:
            ball.vel.y = ball.vel.y - gravity

        if ball.pos.y <-15:
            ball.vel.y = ball.vel.y + gravity
        
        if ball.pos.x <-40:
            ball.vel.x = ball.vel.x + gravity
        
        if ball.pos.x >41:
            ball.vel.x = ball.vel.x - gravity
        
        #ball2

        if ball2.pos.z < floor.pos.z:  # w0 has the smallest x value
            ball2.pos.z = floor.pos.z  # make sure we stay in bounds
            ball2.vel.z = -1.0 * ball.vel.z 
        
        if ball2.pos.z > 15:
            ball2.vel.z = ball.vel.z - gravity
        
        if ball2.pos.y > 15:
            ball2.vel.y = ball.vel.y - gravity

        if ball2.pos.y <-15:
            ball2.vel.y = ball.vel.y + gravity
        
        if ball2.pos.x <-40:
            ball2.vel.x = ball.vel.x + gravity
        
        if ball2.pos.x >41:
            ball2.vel.x = ball.vel.x - gravity

        #ball3
        
        if ball3.pos.z < floor.pos.z:  # w0 has the smallest x value
            ball3.pos.z = floor.pos.z  # make sure we stay in bounds
            ball3.vel.z = -1.0 * ball.vel.z 
        
        if ball3.pos.z > 15:
            ball3.vel.z = ball.vel.z - gravity
        
        if ball3.pos.y > 15:
            ball3.vel.y = ball.vel.y - gravity

        if ball3.pos.y <-15:
            ball3.vel.y = ball.vel.y + gravity
        
        if ball3.pos.x <-40:
            ball3.vel.x = ball.vel.x + gravity
        
        if ball3.pos.x >41:
            ball3.vel.x = ball.vel.x - gravity

        # BOUNDS FOR ALIEN 1

        if alien.pos.z < floor.pos.z:  # w0 has the smallest x value
            alien.pos.z = floor.pos.z  # make sure we stay in bounds
            alien.vel.z = -1.0 * alien.vel.z 
                
        if alien.pos.z > 15:
            alien.vel.z = alien.vel.z - gravity
           
        if alien.pos.y > 15:
            alien.vel.y = alien.vel.y - gravity        

        if alien.pos.y <-15:
            alien.vel.y = alien.vel.y + gravity
            
        if alien.pos.x <-40:
            alien.vel.x = alien.vel.x + gravity
            
        if alien.pos.x >41:
            alien.vel.x = alien.vel.x - gravity 
        
        # BOUNDS FOR ALIEN 2

        if alien2.pos.z < floor.pos.z:  # w0 has the smallest x value
            alien2.pos.z = floor.pos.z  # make sure we stay in bounds
            alien2.vel.z = -1.0 * alien2.vel.z 
        
        if alien2.pos.z > 15:
            alien2.vel.z = alien2.vel.z - gravity
        
        if alien2.pos.y > 15:
            alien2.vel.y = alien2.vel.y - gravity 
        
        if alien2.pos.y <-15:
            alien2.vel.y = alien2.vel.y + gravity

        if alien2.pos.x <-40:
            alien2.vel.x = alien2.vel.x + gravity
        
        if alien2.pos.x >41:
            alien2.vel.x = alien2.vel.x - gravity 
           
        # BOUNDS FOR ALIEN 3

        if alien3.pos.z < floor.pos.z:  # w0 has the smallest x value
            alien3.pos.z = floor.pos.z  # make sure we stay in bounds
            alien3.vel.z = -1.0 * alien3.vel.z 
        
        if alien3.pos.z > 15:
            alien3.vel.z = alien3.vel.z - gravity
        
        if alien3.pos.y > 15:
            alien3.vel.y = alien3.vel.y - gravity 
        
        if alien3.pos.y <-15:
            alien3.vel.y = alien3.vel.y + gravity

        if alien3.pos.x <-40:
            alien3.vel.x = alien3.vel.x + gravity
        
        if alien3.pos.x >41:
            alien3.vel.x = alien3.vel.x - gravity 
        
        # BOUNDS FOR ALIEN 4

        if alien4.pos.z < floor.pos.z:  # w0 has the smallest x value
            alien4.pos.z = floor.pos.z  # make sure we stay in bounds
            alien4.vel.z = -1.0 * alien4.vel.z 
        
        if alien4.pos.z > 15:
            alien4.vel.z = alien4.vel.z - gravity
        
        if alien4.pos.y > 15:
            alien4.vel.y = alien4.vel.y - gravity 
        
        if alien4.pos.y <-15:
            alien4.vel.y = alien4.vel.y + gravity

        if alien4.pos.x <-40:
            alien4.vel.x = alien4.vel.x + gravity
        
        if alien4.pos.x >41:
            alien4.vel.x = alien4.vel.x - gravity 
            
        #radius determine where it is - hit + height how far back
        
        if ball.pos.x + ball.radius <= goal1.pos.x + 1.5 and ball.pos.x + ball.radius >= goal1.pos.x - 1.5:
            if ball.pos.z + ball.radius <= goal1.pos.z + 5 and ball.pos.z + ball.radius >= goal1.pos.z - 5:
                if ball.pos.y + ball.radius  >= goal1.pos.y - 10 and ball.pos.y + ball.radius <= goal1.pos.y + 10:
                    ball.vel = vector(0,0,0)
                    print('You lose!') #if ball goes in user's goal
            
        if ball.pos.x + ball.radius <= goal2.pos.x + 1.5 and ball.pos.x + ball.radius >= goal2.pos.x - 1.5:
            if ball.pos.z + ball.radius <= goal2.pos.z + 5 and ball.pos.z + ball.radius >= goal2.pos.z - 5:
                if ball.pos.y + ball.radius  >= goal2.pos.y - 10 and ball.pos.y + ball.radius <= goal2.pos.y + 10:
                    if ball2.pos.x + ball2.radius <= goal2.pos.x + 1.5 and ball2.pos.x + ball2.radius >= goal2.pos.x - 1.5:
                        if ball2.pos.z + ball2.radius <= goal2.pos.z + 5 and ball2.pos.z + ball2.radius >= goal2.pos.z - 5:
                            if ball2.pos.y + ball2.radius  >= goal2.pos.y - 10 and ball2.pos.y + ball2.radius <= goal2.pos.y + 10:
                                if ball3.pos.x + ball3.radius <= goal2.pos.x + 1.5 and ball3.pos.x + ball3.radius >= goal2.pos.x - 1.5:
                                    if ball3.pos.z + ball3.radius <= goal2.pos.z + 5 and ball3.pos.z + ball3.radius >= goal2.pos.z - 5:
                                        if ball3.pos.y + ball3.radius  >= goal2.pos.y - 10 and ball3.pos.y + ball3.radius <= goal2.pos.y + 10:
                                            ball.vel = vector(0,0,0)
                                            print("You win!") #if all three in goal            
        
        if ball2.pos.x + ball2.radius <= goal2.pos.x + 1.5 and ball2.pos.x + ball2.radius >= goal2.pos.x - 1.5:
            if ball2.pos.z + ball2.radius <= goal2.pos.z + 5 and ball2.pos.z + ball2.radius >= goal2.pos.z - 5:
                if ball2.pos.y + ball2.radius  >= goal2.pos.y - 10 and ball2.pos.y + ball2.radius <= goal2.pos.y + 10:
                    ball2.vel = vector(0,0,0) #ball2 in goal

        
        if ball3.pos.x + ball3.radius <= goal2.pos.x + 1.5 and ball3.pos.x + ball3.radius >= goal2.pos.x - 1.5:
            if ball3.pos.z + ball3.radius <= goal2.pos.z + 5 and ball3.pos.z + ball3.radius >= goal2.pos.z - 5:
                if ball3.pos.y + ball3.radius  >= goal2.pos.y - 10 and ball3.pos.y + ball3.radius <= goal2.pos.y + 10:
                    ball3.vel = vector(0,0,0) #ball3 in goal
        
        if ball.pos.x + 1 >= alien.pos.x - 1 and ball.pos.x - 1 <= alien.pos.x +1:
            if ball.pos.y + 1 >= alien.pos.y - 1 and ball.pos.y -1 <= alien.pos.y +1:
                if alien.pos.z + 1 >= ball.pos.z - 1 and alien.pos.z -1 <= ball.pos.z +1:
                    ball.vel.x += gravity +1
                    alien.vel.x -= gravity #if ball hits the alien
           
        if ball.pos.x + 1 >= alien2.pos.x - 1 and ball.pos.x - 1 <= alien2.pos.x +1:
            if ball.pos.y + 1 >= alien2.pos.y - 1 and ball.pos.y -1 <= alien2.pos.y +1:
                if alien2.pos.z + 1 >= ball.pos.z - 1 and alien2.pos.z -1 <= ball.pos.z +1:
                    ball.vel.x += gravity +1
                    alien2.vel.x -= gravity #if ball hits the alien2
        
        if ball.pos.x + 1 >= alien3.pos.x - 1 and ball.pos.x - 1 <= alien3.pos.x +1:
            if ball.pos.y + 1 >= alien3.pos.y - 1 and ball.pos.y -1 <= alien3.pos.y +1:
                if alien3.pos.z + 1 >= ball.pos.z - 1 and alien3.pos.z -1 <= ball.pos.z +1:
                    ball.vel.x += gravity +1
                    alien3.vel.x -= gravity #if ball hits the alien3
        
        if ball.pos.x + 1 >= alien4.pos.x - 1 and ball.pos.x - 1 <= alien4.pos.x +1:
            if ball.pos.y + 1 >= alien4.pos.y - 1 and ball.pos.y -1 <= alien4.pos.y +1:
                if alien4.pos.z + 1 >= ball.pos.z - 1 and alien4.pos.z -1 <= ball.pos.z +1:
                    ball.vel.x += gravity +1
                    alien4.vel.x -= gravity #if ball hits the alien4
        
        if ball.pos.x + 1 >= ball2.pos.x - 1 and ball.pos.x - 1 <= ball2.pos.x +1:
            if ball.pos.y + 1 >= ball2.pos.y - 1 and ball.pos.y -1 <= ball2.pos.y +1:
                if ball2.pos.z + 1 >= ball.pos.z - 1 and ball2.pos.z -1 <= ball.pos.z +1:
                    ball.vel.x += gravity +1
                    ball2.vel.x -= gravity #if ball hits ball2 
        
        if ball.pos.x + 1 >= ball3.pos.x - 1 and ball.pos.x - 1 <= ball3.pos.x +1:
            if ball.pos.y + 1 >= ball3.pos.y - 1 and ball.pos.y -1 <= ball3.pos.y +1:
                if ball3.pos.z + 1 >= ball.pos.z - 1 and ball3.pos.z -1 <= ball.pos.z +1:
                    ball.vel.x += gravity +1
                    ball3.vel.x -= gravity #if ball hits ball3
        
        if ball2.pos.x + 1 >= ball3.pos.x - 1 and ball2.pos.x - 1 <= ball3.pos.x +1:
            if ball2.pos.y + 1 >= ball3.pos.y - 1 and ball2.pos.y -1 <= ball3.pos.y +1:
                if ball2.pos.z + 1 >= ball3.pos.z - 1 and ball2.pos.z -1 <= ball3.pos.z +1:
                    ball2.vel.x += gravity +1
                    ball3.vel.x -= gravity
                    ball3.vel.y += gravity
                    ball3.vel.z += gravity #if ball2 hits ball3
   
        if alien.pos.x > -100: #fly aliens, fly!
            alien.vel.x += random.randint(0,2)
            alien.vel.y += random.randint(0,2)
            alien.vel.z += random.randint(0,2)
            alien2.vel.x -= random.randint(0,2)
            alien2.vel.y -= random.randint(0,2)
            alien2.vel.z -= random.randint(0,2)
            alien3.vel.x += random.randint(0,2)
            alien3.vel.y += random.randint(0,2)
            alien3.vel.z += random.randint(0,2)
            alien4.vel.x += random.randint(0,2)
            alien4.vel.y += random.randint(0,2)
            alien4.vel.z += random.randint(0,2)

        # +++ end of COLLISION SECTION

        # +++ start of KEYBOARD SECTION - check for keypresses here + handle them

        if scene.visible:   # any keypress to be handled?
            s = keysdown()
            print("You pressed the key", s)  
            # Key presses to give the ball velocity (in the x-z plane)
            dx = .5; dz = .5   # easily-changeable values
            if 'left' in s: ball.vel += vector(-dx,0,0)#X AXIS
            if 'right' in s: ball.vel += vector(dx,0,0)
            if 'a' in s: ball.vel += vector(0,0,dz)#Z AXIS
            if 'z' in s: ball.vel += vector(0,0,-dz)
            if 'up' in s: ball.vel += vector(0,+dz,0) #Y AXIS
            if 'down' in s: ball.vel += vector(0,-dz,0)
        # space to stop everything
            if ' ' in s:  # space to stop things
                ball.vel = vector(0,0,0)
                alien.vel = vector(0,0,0)

        # +++ end of KEYBOARD SECTION - check for keypresses here + handle them

# things start here!
if __name__ == "__main__":
    main()

