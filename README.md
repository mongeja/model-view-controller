# model-view-controller
#The Mobile_Simulton base class stores the angle (in radians) and speed (in pixels/update) of every mobile object in the simulation (and inherits the information controlled by the Simulton class). It includes methods to query and update this information.

#The Prey base class is an ancestor of every class that produces "edible" objects; it contains only code to call __init__ for Mobile_Simultons (it base class).

#The Ball and Floater classes represent balls (traveling in straight lines) and floaters (travelling more eratically) that traverse the simulation canvas. They are both subclasses (and thus instances) of Prey so they can be "eaten" by Black_Holes, Pulsators, Hunters.

#The Black_Hole class represents a stationary object that eats (removes from the simulation) any Prey object whose center becomes contained its perimeter.

#The Pulsator class represents a special kind of Black_Hole: one that gets bigger (as it eats Prey) and smaller (as it starves); if it gets too small (starves for too long) it dies: removes itself from the simulation.

#The Hunter class represents a special kind of Pulsator: one that is mobile (hence its two base classes), and moves towards the closest Prey that it can see (there are limits to its vision).

#The application allows the user to place different kinds of objects (called simultons), into a simulation and watch them interact.
