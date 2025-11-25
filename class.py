class Person:
  name = "Samit"
  occupation = "Software Developer"
  savings = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "abc"
a.occupation = "Accountant"

b.name = "def"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()