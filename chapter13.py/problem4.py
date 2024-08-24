def divisible5(n):
    if(n%5  == 0):
        return True
    return False
a = [1, 2, 3455,55,53,625,45664,5545,45,95]
f = list(filter(divisible5, a))
print(f)