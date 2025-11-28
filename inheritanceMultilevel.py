class Grandfather:
 
    def __init__(self, grandFatherName):
        self.grandFatherName = grandFatherName
 
 
class Father(Grandfather):
    def __init__(self, fatherName, grandFatherName):
        self.fatherName = fatherName
        Grandfather.__init__(self, grandFatherName)
class Son(Father):
    def __init__(self, sonName, fatherName, grandFatherName):
        self.sonName = sonName
        Father.__init__(self, fatherName, grandFatherName)
 
    def print_name(self):
        print('Grandfather name :', self.grandFatherName)
        print("Father name :", self.fatherName)
        print("Son name :", self.sonName)
        
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandFatherName)
s1.print_name()