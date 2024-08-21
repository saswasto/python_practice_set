class Employee:
    company = "Microsoft"
    salary = 100000

    def show(self):
        print(f"The Employee works at {self.company} and the salary is {self.salary}")

class Coder:
    company = "Microsoft"  # Added to Coder for compatibility
    language = "Python"
    salary = 100000

    def showcase(self):
        print(f"The Coder works at {self.company} and the salary is {self.salary}")

    def show_language(self):
        print(f"The Coder works at {self.company} and the language is {self.language}")

class Programmer(Employee, Coder):
    company = "Google"
    language = "Java"

    def showcase(self):
        print(f"The Programmer works at {self.company} and the salary is {self.salary}")

    def show_language(self):
        print(f"The Programmer works at {self.company} and the language is {self.language}")

# Create instances
a = Employee()
b = Programmer()

# Call methods on the instances
b.show()  # Inherited from Employee class
b.showcase()  # Overridden in Programmer class
b.show_language()  # Overridden in Programmer class

#print(a.company, b.company)