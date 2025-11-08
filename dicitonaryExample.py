info = {
    'name': 'S R',
    'age': 23,
    'city': 'stk',
    'occupation': 'Python Developer',
    'best_language': 'Python',
    'married': False,
    'salary': 75000.50
}

# # Print the whole dictionary
# print(info)

# # Print specific values
# print("Name:", info['name'])
# print("Age:", info['age'])

# # print specific values without an error
# print("Country:", info.get('country'))

# # print all keys
# print("Keys:", info.keys())


# print all pairs
for key,value in info.items():
    print(f"{key}: {value}")

# for x in info.items():
#     print(x)

# print(info.items())
 