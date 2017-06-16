from math import *

class Vector2(tuple):
    def __new__(typ, x=0.0, y=0.0):
        n = tuple.__new__(typ,(int(x),int(y)))
        n.x = x
        n.y = y
        return n

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    @classmethod
    def from_points(cls, P1, P2):
        return cls( P2[0] - P1[0], P2[1] - P1[1] )

    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )

    def normalize(self):
        magnitude = self.get_magnitude()
        if magnitude != 0:
            self.x /= magnitude
            self.y /= magnitude