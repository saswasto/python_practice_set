words = ["Donkey", "Monkey", "Tiger", "Lion", "Elephant", "Dog", "Cat", "Rabbit", "Horse", "Cow"]

with open("qs.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))
with open("qs.txt", "w") as f:
    f.write(content)
