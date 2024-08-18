class tricket:
    def book(self,trainNumber,fro,to):
        print(f"Tricket is booked in train number {trainNumber} from {fro} to {to}")
    def getStatus(self,trainNumber):
        print(f"Train is running on time {trainNumber}")
    def fareinformation(self,trainNumber,fro,to):
        print(f"The fare is 1500 and the train number is {trainNumber} from {fro} to {to}")
a = tricket()
a.book(12.35,"Kolkata","Delhi")
a.getStatus(12.35)
a.fareinformation (12.35,"Kolkata","Delhi")    

'''
for fare price we are using some different method 
but we can also import random module and use randint function to generate random number

from random import randint
print(f"The fare is {randint(1000,5000)} and the train number is {trainNumber} from {fro} to {to}")
we can also use this method to genetrate the random number for fare price
'''