# Black_Hole inherits from only Simulton, updating by finding/removing
#   any Prey-derived class whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        self._color = 'black'
        
    def contains(self,xy):
        return Simulton.distance(self,xy) < Black_Hole.radius
    
    def update(self,model):
        model.add(self)
        removed = set()
        for p in model.find(lambda x: isinstance(x,Prey)):
            if self.contains((p._x, p._y)):
                removed.add(p)
                model.remove(p)
        return removed
    
    def display(self,canvas):
        canvas.create_oval(self._x-(self._width/2), self._y-(self._height/2),
                                self._x+(self._width/2), self._y+(self._height/2),
                                fill=self._color)
    
    
