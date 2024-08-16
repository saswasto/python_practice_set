with open("old.txt") as f:
    content = f.read()
with open("recomended_by_python.txt","w") as f:
    print(f.write(content))