from array import *

arr = array('i',[])

n = int(input("Enter no of elements:"))
for i in range(n):
    x = int(input("Enter values:"))
    arr.append(x)
print(arr)

# seq[start:end:step]

print(arr[::-1])