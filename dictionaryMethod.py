form1 = {1: 11, 2: 22, 3: 33, 4: 44}
form2 = {5: 55, 6: 66,3: 333}
print("Before Update:", form1)
form1.update(form2)
print("After Update:", form1)
# del form2
# print("form2 after deletion:", form2)

del form1[2]
print("form1 after deleting key 2:", form1)