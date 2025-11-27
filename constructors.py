class Person: # defining a class named Person

  def __init__(self, name, occ): # constructor with parameters name and occ
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("abc", "Developer") # here a is an object of class Person
b = Person("def", "HR")  # here b is another object of class Person
a.info() # used to create info about person a
b.info() # used to create info about person b
# print(a.name)
# a.name = "def"
# a.occ = "HR"
# a.info()