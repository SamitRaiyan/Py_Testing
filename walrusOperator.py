foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

'''
same code without walrus operator:
foods = list()
while True:
  food = input("What food do you like?: ")
  if food == "quit":
      break
  foods.append(food)

'''