my_set = {1, 2, 3, 4, 6, 2, "apple", "banana"}
print("Original set:", my_set) 

# Empty set
empty_set = set()
print("Empty set:", empty_set)
print("Type of empty set:", type(empty_set))

# my_set.remove(2)   # Removes 2 from the set
my_set.discard(2)    # Removes 2 from the set if it exists
print("Set after removing 2:", my_set)
