from array import *
vals = array('i',[2,3,4,56,7,8,9])

for i in range(len(vals)):
    print(vals[i])

NewArray = array(vals.typecode,[a*a for a in vals])
for i in range(len(NewArray)):
    print(NewArray[i])
