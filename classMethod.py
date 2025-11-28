# class method used as an alternative constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split('-')
        return cls(name, int(age))

person1 = Person.from_string("John Doe-30")
print("Name:",person1.name)  # Output: John Doe
print("Age:",person1.age)   # Output: 30