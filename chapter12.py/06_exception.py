try:
    a = int(input("hey give me a number: "))
    print(a)
    
except ValueError as v:
    print("Heyyyy")
    print(v)
    
except Exception as e:
    print(e)
    
print("Thank ypu ")