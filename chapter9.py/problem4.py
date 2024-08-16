word = "Donkey"
with open("qs.txt", "r") as f:
    content = f.read()
contentNew = content.replace(word, "######")

with open("qs.txt", "w") as f:
    f.write(contentNew)
