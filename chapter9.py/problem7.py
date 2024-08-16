
with open("log.text.html")as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    content = line
    if ("python"in line):
      print(f"yes python is present. Line number = {lineno}")
      break
    lineno += 1
else:
    print("python is not in the Lines.")