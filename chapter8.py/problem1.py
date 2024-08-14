a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
def greatest(a,b,c):
    if a > b and b> c:
        return a
    elif b > a and a > c:
        return b
    else:
        return c
print(greatest(a,b,c))