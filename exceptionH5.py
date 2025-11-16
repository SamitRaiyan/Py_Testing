a = input("Enter between 2 - 8 or 'quit': ")
if a.lower() == 'quit':
    print("Program exited")
else:
    a = int(a)
    if a < 2 or a > 8:
        raise ValueError("Value must be between 2 and 8")
    print("Value is within the range")