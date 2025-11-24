# Example of filter()
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
even_numbers = list(filter(lambda y: y % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4, 6]