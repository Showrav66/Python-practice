# import necessary packages
import matplotlib.pyplot as plt


# define functions
# 1.
def lagrange_polynomial(point, x, f):
    '''Here Lagrange interpolation method is implemented'''
    result = 0
    for j in range(len(x)):

        p = 1
        for k in range(len(x)):
            if k != j:
                p *= float(point - x[k]) / float(x[j] - x[k])
        result += p * f[j]

    return result


# 2.
def lagrange_interpolation(x, y):
    '''This function generates new dataset'''
    initial = x[0]
    dx = float(x[1] - x[0]) / 10
    n_x = []
    n_y = []

    while initial <= x[len(x) - 1]:
        n_x.append(initial)
        n_y.append(lagrange_polynomial(initial, x, y))
        initial += dx

    return n_x, n_y



xGiven = [2, 3, 6, 9, 13, 22]
yGiven = [4, 8, 12, 34, 55, 91]

xline, yline = lagrange_interpolation(xGiven, yGiven)

plt.plot(xGiven, yGiven, 'ro', label='Given points')
plt.plot(xline, yline, 'g--', label='Lagrange interpolation')

plt.legend()
plt.show()
