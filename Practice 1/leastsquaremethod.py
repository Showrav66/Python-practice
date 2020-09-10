import matplotlib.pyplot as plt


def least_square(x):
    initial = x[0]
    dx = float(x[1] - x[0]) / 10
    xline = []
    yline = []
    while initial <= x[len(x) - 1]:
        y = 3.5 + 1.4 * initial
        xline.append(initial)
        yline.append(y)

        initial += dx

    return xline, yline

xGiven = [1, 2, 3, 4]
yGiven = [6, 5, 7, 10]

xline, yline = least_square(xGiven)

plt.plot(xGiven, yGiven, 'ro',label = 'Given data points')
plt.plot(xline, yline, 'b--',label = 'Fitted curve')
plt.legend()
plt.show()
