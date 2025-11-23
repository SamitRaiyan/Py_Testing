# using iterations to read the marks of students from marks.txt file
# also using readlines() method to read all lines at once
# The readline() method includes the newline character \n at the end of each line, and print() adds another newline by default.

f = open("marks.txt", "r")

while True:
    line = f.readline()
    if not line:
        break
    print("Line:", line, end='')  # end='' to avoid double newlines