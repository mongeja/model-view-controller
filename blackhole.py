# Black_Hole is derived from Simulton only: it updates by finding/removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
from special import Special
import model

#  point is contained in the Black_Hole if the 
#  distance from the center of the Black_Hole to
#   the center of the object is less than the radius of the Black_Hole

class Black_Hole(Simulton):
    radius = 10
    def __init__(self, x,y,width,height):
        Simulton.__init__(self, x,y,width,height)
        self._color = (255, 255, 255)
        
    def contains(self, xy):
        if self.distance(xy) < self.get_dimension()[0] / 2:
            return True
        else:
            return False
    
    def update(self, model):
        simul_eat = set()
#         simul_eat.add(model.find(lambda x: self.contains(x.get_location())))
        for add_simul in model.find(lambda x:isinstance(x,Prey) and self.contains(x.get_location())):
            simul_eat.add(add_simul)
        for simul in simul_eat:
            model.remove(simul)
            if type(simul) == Special:
                model.remove(self)
                return simul_eat
        return simul_eat

    def display(self, canvas):
        canvas.create_oval(self.get_location()[0]-self.get_dimension()[0]/2, self.get_location()[1]-self.get_dimension()[1]/2,
                           self.get_location()[0]+self.get_dimension()[0]/2, self.get_location()[1]+self.get_dimension()[1]/2,
                           fill='black')
        
           
        
    
    
    
