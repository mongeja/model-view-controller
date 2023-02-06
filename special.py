#Special is derived from the Ball class, it acts like a ball however it is orange,
#and is slightly larger than a ball and moves faster. It also self destructs on any
#non prey so when it is eaten, it eats the predator
from ball import Ball

class Special(Ball):
    radius = 6
    def __init__(self,x,y,speed,angle,color):
        Ball.__init__(self,x,y,speed,angle,color)
    
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius, self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill='orange')
    
    
        