import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([0, -1, 1])

print("Welcome to the game of Snake, Water, and Gun! Here you can enter (s for snake, w for water, g for gun)")

youstr = input("Enter your choice: ")

youDict = {"s": 1, "g": 0, "w": -1}
reverseDict = {1: "snake", 0: "gun", -1: "water"}
you = youDict[youstr]
print(f"Computer chose {reverseDict[computer]}")
print(f"You chose {reverseDict[you]}")

if(computer == you):
    print("It's a tie!")
elif (computer == -1 and you ==1 ):
    print("You win!")
elif (computer == 0 and you == -1):
    print("you win!")
elif (computer == 1 and you == 0):
    print("You win!")
elif (computer == 0 and you == 1):
    print("You lose!")
elif (computer == -1 and you == 0):
    print("You lose!")
elif (computer == 1 and you == -1):
    print("You lose!")
else:
    print("something went wrong")