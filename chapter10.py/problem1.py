class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, salary, location):
        self.name = name
        self.salary = salary
        self.location = location

p = Programmer("harry", 10000000, "kolkata")

print(p.name, p.salary, p.location)
