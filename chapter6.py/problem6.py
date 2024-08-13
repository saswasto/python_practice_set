mark = int(input("Enter your mark: "))
if (mark <= 100 and mark >= 90):
    print("You got an Ex")
elif(mark <= 89 and mark >= 80):
    print("You got an A")
elif(mark <= 79 and mark >= 70):
    print("You got an B")
elif(mark <= 69 and mark >= 60):
    print("You got an C")
elif(mark <= 59 and mark >= 50):
    print("You got an D")
else:
    print("You failed")