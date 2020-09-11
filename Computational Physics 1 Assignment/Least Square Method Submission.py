# 1. import necessary package, library or module here
import matplotlib.pyplot as plt


# Define required function(s)
def least_square(x, y):
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0

    for i in range(len(x)):
        c1 = c1 + x[i]
        c2 = c2 + x[i] ** 2
        c3 = c3 + x[i] ** 3
        c4 = c4 + x[i] ** 4
        c5 = c5 + y[i]
        c6 = c6 + x[i] * y[i]
        c7 = c7 + (x[i] ** 2) * y[i]

    n = len(x)
    a0 = float((c5 * (c2 * c4 - c3 * c3) - c1 * (c4 * c6 - c3 * c7) + c2 * (c3 * c6 - c2 * c7)) / (
            n * (c2 * c4 - c3 * c3) - c1 * (c1 * c4 - c2 * c3) + c2 * (c1 * c3 - c2 * c2)))

    a1 = float((n * (c4 * c6 - c3 * c7) - c5 * (c1 * c4 - c2 * c3) + c2 * (c1 * c7 - c2 * c6)) / (
            n * (c2 * c4 - c3 * c3) - c1 * (c1 * c4 - c2 * c3) + c2 * (c1 * c3 - c2 * c2)))

    a2 = float((n * (c2 * c7 - c3 * c6) - c1 * (c1 * c7 - c2 * c6) + c5 * (c1 * c3 - c2 * c2)) / (
            n * (c2 * c4 - c3 * c3) - c1 * (c1 * c4 - c2 * c3) + c2 * (c1 * c3 - c2 * c2)))

    initial = x[0]
    dx = float(x[1] - x[0]) / 10
    n_x = []
    n_y = []

    while initial <= x[len(x) - 1]:
        p = a0 + a1 * initial + a2 * initial * initial
        n_x.append(initial)
        n_y.append(p)
        initial += dx

    return n_x, n_y



# 2. define data set (list of x and y) and iteration number
xGiven = [1, 4, 7, 11, 15, 20, 30, 50, 77, 92, 100]
yGiven = [5, 20, 52, 121, 228, 403, 903, 2504, 5929, 8464, 10005]

# 3. user defined function call

xline, yline = least_square(xGiven, yGiven)

# 4. plot data point in red and least square fit in blue
plt.plot(xGiven, yGiven, 'ro', label='Given data points')
plt.plot(xline, yline, 'b--', label='Least Square fit(2nd order polynomial)')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()

plt.show()
