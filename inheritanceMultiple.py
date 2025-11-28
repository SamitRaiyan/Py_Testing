class Mother:
    motherName = ""
 
    def mother(self):
        print(self.motherName)
 
class Father:
    fatherName = ""
 
    def father(self):
        print(self.fatherName)
 
class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fatherName)
        print("Mother :", self.motherName)

s1 = Son()
s1.fatherName = "Daddy"
s1.motherName = "Mommy"
s1.parents()