from math import *
u =10
theta = 30
x = 1
y = (tan(theta) * x) - (9.81 * x**2) / (2 * u**2 * (cos(theta))**2)
print(y)