from math import sqrt

class Vector:

    def __init__(self, o = (0,0,0), d = (0,0,0)):
        self.o = o
        self.d = d

    def __add__(self, other):
        o = self.o
        d = tuple([other.d[i]+self.d[i]-other.o[i]-self.o[i] for i in range(3)])
        return self.__class__(o, d)

    def __sub__(self, other):
        o = self.o
        d = tuple([other.d[i]-self.d[i]-other.o[i]-self.o[i] for i in range(3)])
        return self.__class__(o, d)

    def __mul__(self, other):
        if type(other) in (Vector, str):
            raise TypeError
        o = self.o
        d = tuple([(self.d[i]-self.o[i])*other+self.o[i] for i in range(3)])
        return self.__class__(o, d)

    def __truediv__(self, other):
        if type(other) in (Vector, str):
            raise TypeError
        o = self.o
        d = tuple([(self.d[i] - self.o[i]) / other + self.o[i] for i in range(3)])
        return self.__class__(o, d)

    def __str__(self):
        return str(self.o)+str(self.d)

    def magn(self):
        sum = 0
        for i in range(3):
            sum += pow(self.d[i] - self.o[i], 2)
        return sqrt(sum)

    def norm(self):
        return self/self.magn()

    def dot(self, other):
        sum = 0
        for i in range(3):
            sum += (self.d[i] - self.o[i])*(other.d[i] - other.o[i])
        return sum