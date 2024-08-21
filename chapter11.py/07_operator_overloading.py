class Number:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, other):
        if isinstance(other, Number):
            return self.n + other.n
        return self.n + other

n = Number(1)
m = Number(2)
print(n + m) 