def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    return print(l[i])
  except:
    return print("Some error occurred")

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)