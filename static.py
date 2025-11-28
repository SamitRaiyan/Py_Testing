class Math:
    @staticmethod # as it does not depend on instance variables and it call be called without creating an instance and also can be called using class name
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result) # Output: 3