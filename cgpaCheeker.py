gpa = float(input("Input your GPA: "))

if gpa <= 4 and gpa > 3.75:
    print("GPA: A+")
elif gpa <= 3.75 and gpa > 3.5:
    print("GPA: A")
elif gpa <= 3.5 and gpa > 3.25:
    print("GPA: A-")
elif gpa <= 3.25 and gpa > 3:
    print("GPA: B+")
elif gpa <= 3 and gpa > 2.75:
    print("GPA: B")
elif gpa <= 2.75 and gpa > 2.5:
    print("GPA: B-")
elif gpa <= 2.5 and gpa > 2.25:
    print("GPA: C+")
elif gpa <= 2.25 and gpa > 2:
    print("GPA: C")
elif gpa == 2:
    print("GPA: D")
elif gpa < 2 and gpa >= 0:
    print("GPA: F")
else:
    print("Invalid Input")
 