# Hunter inherits from the Pulsator (1st) and the Mobile_Simulton (2nd) class:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    distance = 200
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        self._speed = 5
        Mobile_Simulton.randomize_angle(self)
    
    def update(self,model):
        self.move()
        self.wall_bounce()
        closest = None
        near = model.find(lambda s: isinstance(s,Prey) and Mobile_Simulton.distance(self, s.get_location()) <= Hunter.distance)
        if len(near) != 0:
            closest_distance = min([Mobile_Simulton.distance(self,(n._x, n._y)) for n in near])
            for simulton in near:
                if Mobile_Simulton.distance(self,(simulton._x, simulton._y)) == closest_distance:
                    closest = simulton
            self._angle = atan2(closest._y - self._y, closest._x - self._x)
        Pulsator.update(self,model)