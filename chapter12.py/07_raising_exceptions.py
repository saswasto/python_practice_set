a = int(input("Enter a number:"))
b = int(input("Enter second number:"))
if b == 0:
    raise ZeroDivisionError("Division by zero is not allowed")
else:
    print(f"The division {a/b} is {a/b}")