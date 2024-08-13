a = int(input("Enter the marks in bangla: "))
b = int(input("Enter the marks in english: "))
c = int(input("Enter the marks in math: "))
d = int(input("Enter the marks in science: "))
total_persentance = (100*(a+b+c+d))/400
if(total_persentance>=40 and a>=33 and b>=33 and c>=33 and d>=33):
    print("You are passed",total_persentance)
else:
    print("You are failed",total_persentance)