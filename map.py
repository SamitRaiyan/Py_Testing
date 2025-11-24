# Example of map()
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))
print(squared_numbers)
# Output: [1, 4, 9, 16]