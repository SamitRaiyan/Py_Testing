# using with statement to handle files
with open("myfile.txt", "a") as f:
    f.write("Appending using with statement.\n")
    print("File appended successfully using with statement.")