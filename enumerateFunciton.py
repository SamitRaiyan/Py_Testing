marks = [45,54,73,82,91,48,85,67]
print(len(marks))

for index, value in enumerate(marks, start=0):
    print(f"The mark of the student no {index+1}: ",value,f"while the index is {index}")

for index, value in enumerate(marks, start=1):
    print(f"The mark of the student no {index}: ",value,f"while the index is {index-1}")

    # both gives the same output but the index starts from different numbers based on the start value given in enumerate function.