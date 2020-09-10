a = 0
b = 1
for i in range(6):
    c = a + b
    a = b
    b = c
    print(c)