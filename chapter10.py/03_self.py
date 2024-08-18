class Employee:
    #name = ("Harry")
    language = "Py"
    salary  = ("1000000")
    def getinfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    def greet(self):
       print("Good Morning, Sir") 

harry = Employee()
harry.language = "Java" # This will create a new instance attribute.
harry.greet()
harry.getinfo()
#Employee.getinfo(harry)
#print(harry.language, harry.salary)
