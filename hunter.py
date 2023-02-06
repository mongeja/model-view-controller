# Hunter is derived from the Mobile_Simulton/Pulsator classes: it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from special import Special
from mobilesimulton import Mobile_Simulton
from math import atan2
import model


class Hunter(Pulsator,Mobile_Simulton):
    distance_to_kill = 200
    def __init__(self, x, y, width, height):
        Pulsator.__init__(self, x, y, width, height)
        self._speed = 5
        self._angle = model.random_angle()
    
    def update(self, model):
        simul_eat = set()
        for add_simul in model.find(lambda x:isinstance(x,Prey) and self.contains(x.get_location())):
            simul_eat.add(add_simul)
            self.change_dimension(1,1)
            self._counter = 0
            
        for simul in simul_eat:
            model.remove(simul)
            if type(simul) == Special:
                model.remove(self)
                return simul_eat
            
        if simul_eat == set():
            self._counter += 1
            
        if self._counter == self.time_between_meals:
            self.change_dimension(-1, -1)
            if self.get_dimension()[0] == 0:
                model.remove(self)
            self._counter = 0
            
        closee = 200
        hold_var = None
        for set_spd in model.find(lambda x:isinstance(x,Prey) and self.distance(x.get_location())<self.distance_to_kill):
            if self.distance(set_spd.get_location()) < closee:
                closee = self.distance(set_spd.get_location())
                hold_var = set_spd
        if hold_var != None:
            self._angle = atan2(hold_var.get_location()[1] - self.get_location()[1], hold_var.get_location()[0] - self.get_location()[0])
        self.move()
        
        
        return simul_eat
