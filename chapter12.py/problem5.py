n = int(input("Enter the number: "))

table =[n*i for i in range (1,11)]
with open("table.txt", "w") as f:
    f.write(str(table)+ "\n")