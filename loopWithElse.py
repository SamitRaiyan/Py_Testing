# for x in range(5):
#     print ("iteration no {} in for loop".format(x+1))
# else:
#     print ("else block in loop")
# print ("Out of loop")

for x in range(5):
    print("iteration no: ",x)
    if x==3:
        continue
    # print("iteration no: ",x)
else:
    print("in the else block")

print("out of loop")
