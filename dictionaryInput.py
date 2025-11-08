course = {}
size = int(input("Enter the total number of the courses:"))

for i in range(size):
    course_code = input("Enter the course code:")
    course_credits = int(input("Enter the course credits:"))
    course[course_code] = course_credits

print("The course details are as follows:")
print("course_code : course_credits")
for key, value in course.items():
    print(f"{key}: {value}")