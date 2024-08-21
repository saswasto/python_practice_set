class Employee:
    company ="microsoft"
    def show(self):
        print(f"The Employee name is {self.name} and the salary is {self.salary}")
'''
class manager:
    company = "Google"
    def showcase(self):
        print(f"The Manager name is {self.name} and the salary is {self.salary}")
    def language(self):
        print(f"The manager name is {self.name} and the language is {self.language}")
'''
# Inheritance class
class manager(Employee):
    company = "Google"
    def showcase(self):
        print(f"The Manager name is {self.name} and the salary is {self.salary}")
    def language(self):
        print(f"The manager name is {self.name} and the language is {self.language}")
a= Employee()
b = manager()
print(a.company, b.company)