class Student:
    s = 1
    
    @classmethod
    def show(cls):
        print("The class attribute is:", cls.s)
    
    def __init__(self):
        self._name = None
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Student()
e.a=45

e.name = "Sumon biswas"

print(e.name)

e.show()
