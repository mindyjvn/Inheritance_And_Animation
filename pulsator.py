# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter = 30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._color = 'black'
        self._time_between_meals = 0
        
    def update(self,model):
        removed = Black_Hole.update(self,model)
        if len(removed) != 0:
            self._width += len(removed)
            self._height += len(removed)
            self._time_between_meals = 0
        elif len(removed) == 0:
            self._time_between_meals += 1
            if self._time_between_meals == Pulsator.counter:
                self._time_between_meals = 0
                self._width -= 1
                self._height -= 1
                if self._width == 0:
                    model.remove(self)
        return removed
