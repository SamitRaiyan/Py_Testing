class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("abc", "Developer")
b = Person("def", "HR") 
a.info()
b.info()
# print(a.name)
# a.name = "def"
# a.occ = "HR"
# a.info()