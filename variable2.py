x = 5

def num():
    x =10
    print(x)
    

num()
print(x)

def update_x():
    global x
    x = 20


print(x)
update_x()
print(x)