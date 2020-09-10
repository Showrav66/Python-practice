from array import *

arr1 = array('i',[3,4,5,6,6,7])
arr2 = array('i',[2,4,5,6,7,6])
arr3 = array('i',[])
for i in range(6):
    sum = arr1[i] + arr2[i]
    arr3.append(sum)
print(arr3)