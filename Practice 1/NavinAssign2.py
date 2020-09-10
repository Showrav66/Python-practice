
def update(x):
    print(id(x))
    x = 8
    print(x)
    print(id(x))
a = 5
update(a)
print(id(a))
