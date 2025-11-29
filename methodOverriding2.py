class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):  # Overriding the 'speak' method
        print("Woof! Woof!")

# Create objects
generic_animal = Animal()
my_dog = Dog()

# Call the 'speak' method
generic_animal.speak()  # Output: Generic animal sound
my_dog.speak()         # Output: Woof! Woof!