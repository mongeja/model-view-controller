import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update
import random, math

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from program5 import ball
from simulton import Simulton
from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
balls       = set()
kind_str = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls
    running     = False
    cycle_count = 0
    balls       = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False 


#step just one update in the simulation
def step ():
    global running
    running = True
    update_all()
    running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global kind_str
    kind_str = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if kind_str == "Ball":
        balls.add( Ball(x,y,5,random_angle(),(0,0,255)))
    elif kind_str == "Floater":
        balls.add(Floater(x,y,5,random_angle(), (255,0,0)))
    elif kind_str == 'Hunter':
        balls.add(Hunter(x,y,20,20))
    elif kind_str == "Black_Hole":
        balls.add(Black_Hole(x, y, 20, 20))
    elif kind_str == "Pulsator":
        balls.add(Pulsator(x, y, 20, 20))
    elif kind_str == "Remove":
        for to_remove in find(lambda z: z.contains((x,y))):
            remove(to_remove)
    elif kind_str == "Special":
        balls.add(Special(x,y,10,random_angle(),(255,127,80)))
    
def random_angle():
    return random.random()*math.pi*2


#add simulton s to the simulation
def add(s):
    global balls
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global balls
    balls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    newset = set()
    for simul in balls:
        if isinstance(simul, Simulton):
            if p(simul):
                newset.add(simul)
    return newset


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in set(balls):
            b.update(model)


#delete every simulton being simulated from the canvas; then call display for every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")
