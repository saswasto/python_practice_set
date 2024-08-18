class Employee:
    #name = ("Harry")
    language = "Py"
    salary  = ("1000000")
    
    def __init__(self, Name, Salary, Language):
        self.name = Name
        self.salary = Salary
        self.language = Language
        print("The object is created")
    
    def getinfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    def greet(self):
       print("Good Morning, Sir") 

harry = Employee("Harry",1300000,"Python")
print(harry.name, harry.salary, harry.language)