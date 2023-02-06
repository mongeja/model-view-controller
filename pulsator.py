# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from prey import Prey
from special import Special
import model



class Pulsator(Black_Hole):
    time_between_meals = 30
    def __init__(self, x, y, width, height):
        Black_Hole.__init__(self, x, y, width, height)
        self._counter = 0
    
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
        return simul_eat