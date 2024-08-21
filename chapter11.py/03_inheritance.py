class employee:
    a = 10
class programmer(employee):
    b = 20
class manager(programmer):
    c = 30
o = employee()
print(o.a)
o = programmer()
print(o.a, o.b)
o = manager()
print(o.a, o.b, o.c)