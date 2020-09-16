# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
import math


class Floater(Prey): 
    radius = 5
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,random()*math.pi*2,5)
        self._color = 'red'
    
    def update(self,model):
        change = random()
        if change <= 0.3:
            difference = random()-0.5
            if (self._speed+difference) < 3.0:
                self._speed = 3.0
            if (self._speed+difference) > 7.0:
                self._speed = 7.0
            self.set_velocity(self._speed+difference, self._angle+(random()-0.5))
        
        self.move()
        self.wall_bounce()

    
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill=self._color)