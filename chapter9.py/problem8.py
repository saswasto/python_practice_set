with open("this.txt") as f:
    content = f.readlines()
with open("that_copy.txt", "w") as f:
    for line in content:
        f.write(line)
