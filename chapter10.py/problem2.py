from typing import Any


class calculator:
    def __init__ (self, n):
        self.n = n
    def squre(self):
        print(f"The value is {self.n * self.n}")  
    def cube(self):
        print(f"The value of cube is {self.n* self.n * self.n}")
    def squareroot(self):
        print(f"The value of squareroot is {self.n ** 0.5}")
a = calculator(4)
a.squre()
a.cube()
a.squareroot()