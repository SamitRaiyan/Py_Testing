
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    div= a / b
    print("The result is:", div)
except Exception as e:
    print("Error occurred:", e)