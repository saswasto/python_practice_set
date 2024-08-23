l = [3, 513,53,44,890]
'''
index = 0
for item in l:
    print(f"Index {index} has value {item}")
    index += 1
'''
# This can be simplified using enumerate function.
for index, item in enumerate(l):
    print(f"Index {index} has value {item}")