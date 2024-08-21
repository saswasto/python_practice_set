class student:
    s = 1
    @classmethod
    def show(cls):
        print("The class attribute is: ", cls.s)
e = student()
e.a = 45
e.show()