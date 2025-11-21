name = "Abu Bakr"
age = 61
salary = 45000

def details():
    return print(f"Name: {name}\nAge: {age}\nSalary: {salary}")

def add(a,b):
    return print("The sum is",a+b)

if __name__ == "__main__":
    add(5,6)
    details()