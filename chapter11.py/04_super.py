class employee:
    def __init__(self):
        print("Employee Constructor")
    a = 10
class programmer(employee):
    def __init__(self):
        print("Programmer Constructor")
    b = 20
class manager(programmer):
    def __init__(self):
        super().__init__() 
        print("manager Constructor")   
    c = 30
# o = employee()
# print(o.a)
# o = programmer()
# print(o.a, o.b)
o = manager()
print(o.a, o.b, o.c)