from math import *
import matplotlib.pyplot as plt

# y = tan(theta)*x - (9.81*x**2) / 2*u**2*(cos(theta))**2
# R = u**2 * sin(2*theta) / 9.81

u = float(input('Enter initial velocity:'))
theta = radians(float(input('Enter projection angle:')))

R = ((u**2) * sin(2 * theta)) / 9.81

horizontal_dis = []
vertical_dis = []

for x in range(int(R)):

    y = tan(theta) * x - (9.81 * x ** 2) / (2 * u ** 2 * (cos(theta)) ** 2)

    if y<0:
        break

    horizontal_dis.append(x)
    vertical_dis.append(y)

a = horizontal_dis
b = vertical_dis

plt.plot(a, b)
plt.xlabel('horizontal displacement')
plt.ylabel('vertical displacement')
plt.show()
