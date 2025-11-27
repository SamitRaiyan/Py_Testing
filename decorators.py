def decorator_function(fx):  # fx = function to be decorated (main function as input)
    def mfx(): # mfx = modified fx
        print("--------------------------------------------------")
        print("-------Going to execute the main function-------")
        output =fx()  # Call the main function
        print("-------Finished executing the main function-------")
        print("--------------------------------------------------")
        return output  # Return the result of the main function
    return mfx  # Return the modified function inside the decorator function

@decorator_function # Decorating the add function. Now add = decorator_function(add)
def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a + b

# calling the add function
result = add()
print("Result:", result)

def improved_add(x,y):
    pass  # Placeholder for future implementation