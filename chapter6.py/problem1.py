a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))
d = int(input("Enter the number 4: "))

if(a>b and a>c and a>d):
    print("The number 1 is the largest number")
elif(b>a and b>c and b>d):
    print("The number 2 is the largest number")
elif(c>b and c>a and c>d):
    print("The number 3 is the largest number")
elif(d>b and d>c and d>a):
    print("The number 4 is the largest number")