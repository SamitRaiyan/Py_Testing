class MathTeacher:
    def teach(self):
        print("Math teacher teaches algebra")

class ScienceTeacher:
    def teach(self):
        print("Science teacher teaches physics")

class Student(MathTeacher, ScienceTeacher):  # Math teacher is primary. Cause MathTeacher to be called first.
    def learn(self):
        print("Student asks:")
        super().teach()  # Asks the primary teacher first

student = Student()
student.learn()