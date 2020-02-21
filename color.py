from vector import Vector

color_table = {'r':(1,0,0),
               'g':(0,1,0),
               'b':(0,0,1),
               'y':(1,1,0),
               'c':(0,1,1),
               'p':(1,0,1),
               'k':(0,0,0),
               'w':(1,1,1)}

class Color(Vector):

    def __init__(self, d=(0,0,0)):
        self.o = (0, 0, 0)
        self.d = d

    def set_as(self, color):
        print(color_table[color])
        self.d = color_table[color]
        return self