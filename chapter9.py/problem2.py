import random
def game():
    print("you are playing the game ")
    score =  random.randint(1, 62)
    print("your score: ")
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if hiscore == "":
            hiscore = int(hiscore)
        else:
            hiscore = 0 
    print(f"yourscore:{score}")
    if (score > hiscore or hiscore == 0):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
           # print("you have just broken the highscore")

    return score

game()