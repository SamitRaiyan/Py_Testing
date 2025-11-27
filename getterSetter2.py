class student:
    def __init__(self,name,age):
        print("Inside the constructor: ")
        self.name = name
        self.age = age
    
    def showDetails(self):
        print(f"Name: {self.name} and Age: {self.age}")
    
    # setter method
    def set_age(self, age):
        self.age = age
    
    # getter method
    def get_age(self):
        return self.age
    
s1 = student("Alice", 21)
s1.showDetails()
s1.set_age(25)
s1.showDetails()
