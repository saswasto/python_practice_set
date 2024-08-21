class animals():
    #def lion(self):
    pass
    #    print("Lion is the king of the jungle")
class pets(animals):
    #def cat(self):
      pass
      #  print("Cat is a pet animal")
class dogs(pets):
    @staticmethod
    def bark():
        print("Dog is a pet animal")
d = dogs()
d.bark()