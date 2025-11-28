class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
object = Student3()
object.func1()
object.func2()

# it is a hybrid inheritance because Student1 and Student2 are inheriting School class which is hierarchical inheritance and Student3 is inheriting Student1 class which is single inheritance