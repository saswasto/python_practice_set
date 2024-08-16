p = open("text1.txt")
st = p.readline()
if ("twinkle" in st):
    print("Twinkle is present in the file")
else:
    print("Twinkle is not present in the file")
print(st)
p.close()