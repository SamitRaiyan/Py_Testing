# it is like the switch statement, but it does not need the break statement.
number = int(input("Enter a number (1-5): "))

match number:
    case 1:
        print("You entered One.")
    case 2:
        print("You entered Two.")
    case 3:
        print("You entered Three.")
    case 4:
        print("You entered Four.")
    case 5:
        print("You entered Five.")
    case _:
        print("Invalid input! Please enter a number between 1 and 5.")
