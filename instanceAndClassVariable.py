class Employee:
  companyName = "Apple" # it is a class variable
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name
    self.raise_amount = 0.02
    Employee.noOfEmployees +=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")


emp1 = Employee("ABC")
emp1.raise_amount = 0.3 # it is an instance variable
emp1.companyName = "Apple BD" 
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("DFE")
emp2.companyName = "Nestle"
emp2.showDetails()
# the upper two lines will be turned into one line as below
# Employee.showDetails(emp2)

emp3 = Employee("XYZ")
emp3.showDetails()