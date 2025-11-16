# example of custom error handling in Python with raise keyword.
a= int(input("Enter between 2 - 8: "))
if a < 2 or a > 8:
    raise ValueError("Value must be between 2 and 8")
    # print("Value is within the range") # This line will not be executed if the exception is raised

print("Value is within the range")