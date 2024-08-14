def factorial(i):
    if(i==1 or i==0):
        return 1
    return i*factorial(i-1)

n = int(input("Enter a number: "))
print("factorial of the number is :", factorial(n))