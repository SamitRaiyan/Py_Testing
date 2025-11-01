# -------------Calculator with options----------------
heading = """
Welcome to the calculation with options to have operations only on two numbers.
Choose your options:-
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modules
6. Difference
"""
print(heading)

# functions is used to create calculations
# defining the functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Division by 0"
    return a/b
def mod(a,b):
    return a%b
def diff(a,b):
    return(None)

#  for multiple calculations: 
while 1:
    choice = int(input("Option Please: "))
    
    if choice in [1,2,3,4]:
        number1 = float(input("First Number: "))
        number2 = float(input("Second Number: "))

        if choice == 1:
            print(f"{number1}+{number2} = {add(number1,number2)}")
        
        elif choice == 2:
            print(f"{number1}-{number2} = {sub(number1,number2)}")

        elif choice == 3:
            print(f"{number1}*{number2} = {mul(number1,number2)}")

        elif choice == 4:
            print(f"{number1}/{number2} = {div(number1,number2)}")

        elif choice == 5:
            print(f"{number1} mod {number2} = {mod(number1,number2)}")

        nextCalculation = input("More calculation (y/n): \n")
        if nextCalculation != 'y':
            break
    
    else:
        print("invalid\n")