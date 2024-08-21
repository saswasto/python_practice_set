class Employee:
   salary = 10000
   _increment = 5  # Use a private variable for increment storage

   @property
   def salaryAfterIncrement(self):
      return self.salary + self.salary * (self.increment / 100)

   @property
   def increment(self):
      return self._increment

   @increment.setter
   def increment(self, salary):
      self._increment = ((salary / self.salary) - 1) * 100

e = Employee()
print(e.salaryAfterIncrement)

