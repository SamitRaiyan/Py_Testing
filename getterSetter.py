class MyClass: # defining a class
  def __init__(self, value):
      self._value = value
    
  def show(self): 
    print(f"Value is {self._value}")
    
  @property # works as getter.
  def ten_value(self):
      return 10* self._value
    
  @ten_value.setter # works as setter
  def ten_value(self, new_value):
      self._value = new_value/10

obj = MyClass(10) # creating an object of the class
print(obj.ten_value) # accessing the property using getter 
obj.ten_value = 67 # setting the property using setter
print(obj.ten_value) # accessing the property using getter
obj.show() # calling the method to show the value