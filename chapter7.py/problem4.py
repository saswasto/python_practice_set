i = int(input("Enter a number: "))
for j in range(1,i):
    if(i%j==0):
      print(f"{i} is a prime number")
      break
else:
  print(f"{i} is not a prime number")