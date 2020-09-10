from array import *
arr = array("i", [])
for i in range(4):
    x = int(input("Enter the value: "))
    arr.append(x)
print(arr)
b = array('i', [])
for i in range(4):
    b.append(arr[-(i+1)])
print(b)


