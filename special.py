# Special inherits from the Black_Hole (1st) and the Mobile_Simulton (2nd) class:
#   updating/displaying like its Black_Hole base, but also moving in the shape
#   of a diamond, like its Mobile_Simultion base. When it eats a simulton, there is 
#   a 50% chance it shifts 30 pixels to the horizontally (25% left, 25% right)
#   and a 50% chance it shifts 5 pixels vertically (25% up, 25% down).


from blackhole import Black_Hole
from mobilesimulton import Mobile_Simulton
import random


class Special(Black_Hole, Mobile_Simulton):
    cycles = 0
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._speed = 5
        self._angle = 0
        self._color = 'yellow'
    
    def update(self,model):
        self.cycles += 1
        self.move()
        self.wall_bounce()
        if self.cycles % 10 == 0:
            self._angle += 36
        removed = Black_Hole.update(self,model)
        direction = random.random()
        if len(removed) > 0:
            if direction <= 0.25:
                self._x -= 30
            elif direction <= 0.5:
                self._x += 30
            elif direction <= 0.75:
                self._y -= 30
            elif direction <= 1:
                self._y += 30
            