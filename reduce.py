from functools import reduce

# Example of reduce()
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)
# Output: 10