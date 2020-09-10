from math import *
import matplotlib.pyplot as plt

xGiven = [0, 30, 45, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]
yGiven = []
xline = []
yline = []

for i in xGiven:
    yGiven.append(sin(radians(i)))


def linearinterpolation(xGiven, yGiven):
    stop = xGiven[-1]
    x = xGiven[0]

    fi = yGiven[0]
    f1 = yGiven[1]
    xi = xGiven[0]
    x1 = xGiven[1]

    while (x <= stop):
        f = fi + (f1 - fi) * (x - xi) / (x1 - xi)
        xline.append(x)
        yline.append(f)
        x += 0.001

    return xline, yline


for i in range(len(xGiven) - 1):
    xlist = [xGiven[i], xGiven[i + 1]]
    ylist = [yGiven[i], yGiven[i + 1]]
    xline, yline = linearinterpolation(xlist, ylist)

plt.plot(xGiven, yGiven, 'ro',label='Given data')
plt.plot(xline, yline, 'g--',label='linear fit')
plt.legend()
plt.show()
