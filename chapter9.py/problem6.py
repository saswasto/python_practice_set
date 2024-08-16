with open("log.text.html")as f:
    content = f.read()
if ("python"in content):
    print("Python is in the content.")
else:
    print("python is not in the content.")
