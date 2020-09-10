from array import *

arr = array('i',[])
n = int(input("Enter the length of the array:"))

for i in range(n):
    x = int(input("Enter values:"))
    arr.append(x)

print(arr)

for i in arr:
    print(i)

ind = int(input("Enter a value you want to search:"))

for j in range(n):
    if ind == arr[j]:
        print([j])

k=0
for e in arr:
    if ind == e:
        print(k)
        break

    k+=1

print(arr.index(ind))
