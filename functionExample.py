def avg(a,b):
    c = (a + b) / 2
    return c

print(avg(4,6))  # Output: 5.0

def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum(1,2,3,4,5))  # Output: 15