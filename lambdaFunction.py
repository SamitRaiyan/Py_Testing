double = lambda x: x * 2
cube = lambda x: x ** 3
avg = lambda x, y: (x + y) / 2
multiAvg = lambda a,b,c,d: (a + b + c + d) / 4

print(multiAvg(10, 20, 30, 40))  # Output: 25.0
print(double(5))                # Output: 10
print(cube(3))                  # Output: 27
print(avg(10, 20))              # Output: 15.0