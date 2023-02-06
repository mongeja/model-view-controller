# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


# from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random, randint


class Floater(Prey):
    radius = 5

        
        
    def __init__(self,x,y,speed,angle,color):
        Prey.__init__(self, x,y,10,10,angle,speed)
        self._x       = x
        self._y       = y
        self._speed   = speed
        self._angle   = angle
        self._color   = color
        self._thirty_percent = set()
        for num in range(1,31):
            self._thirty_percent.add(num)
    
    def update(self, model):
        if randint(1,100) in self._thirty_percent:
            valuefive = randint(-5,5) * .1
            self._speed +=valuefive
            if self._speed <3:
                self._speed = 3
            elif self._speed >7:
                self._speed = 7
            valueran = randint(-5,5) * .1
            self._angle +=valueran
        self.move()
        self.wall_bounce()
    
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='red')