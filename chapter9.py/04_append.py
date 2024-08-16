st = "Hey sasoto how are you?"

f = open("myfile1.txt", "a")

f.write(st)

f.close()
# the modified version of the code above is below
with open("myfile1.txt", "a") as f:
    print(f.read())
# Here we don't need to close the file, as the with statement will automatically close the file once the block of code is executed.