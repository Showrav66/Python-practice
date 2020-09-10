from math import *

print("ax2 + bx + c = 0")

a = int(input('Enter the co-efficient of X2:'))
b = int(input('Enter the co-efficient of X:'))
c = int(input('Enter the constant:'))

d = (sqrt(b*b - 4*a*c))/2*a
x1 = -(b/2*a) + d
x2 = -(b/2*a) - d

print("x1=",x1)
print("x2=",x2)
