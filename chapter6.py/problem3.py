p1 = "Make a lots of money" 
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this" 
message = input("Enter your message: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comments is a spam message")
else:
    print("This comments is not a spam message")