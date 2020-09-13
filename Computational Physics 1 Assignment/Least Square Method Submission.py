"""This is a bare bone code for Least Square Method written by
Showrav Acharjee
Reg no: 2017132066

formulae:

approximated 2nd order polynomial(Quadratic function):
p(x) = a0 + a1 * x + a2 * x ** 2
minimization produces:
n * a0 + c1 * a1 + c2 * a2 = c5
c1* a0 +c2 * a1 + c3 * a2 = c6
c2 * a0 + c3 * a1 + c4 * a2 = c7
"""

# Necessary package, library or module are imported here
import matplotlib.pyplot as plt


# Required function is defined here
def least_square(x, y):
    # This function returns new data set for the approximated polynomial
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0

    # Loop over i for generating coefficients and constants of the equations obtained from minimization
    for i in range(len(x)):
        c1 = c1 + x[i]
        c2 = c2 + x[i] ** 2
        c3 = c3 + x[i] ** 3
        c4 = c4 + x[i] ** 4
        c5 = c5 + y[i]
        c6 = c6 + x[i] * y[i]
        c7 = c7 + (x[i] ** 2) * y[i]

    # The coefficients of the working formula( p = a0 + a1 * x + a2 * x^2) is obtained here using Cramer's rule
    n = len(x)
    a0 = float((c5 * (c2 * c4 - c3 * c3) - c1 * (c4 * c6 - c3 * c7) + c2 * (c3 * c6 - c2 * c7)) / (
            n * (c2 * c4 - c3 * c3) - c1 * (c1 * c4 - c2 * c3) + c2 * (c1 * c3 - c2 * c2)))

    a1 = float((n * (c4 * c6 - c3 * c7) - c5 * (c1 * c4 - c2 * c3) + c2 * (c1 * c7 - c2 * c6)) / (
            n * (c2 * c4 - c3 * c3) - c1 * (c1 * c4 - c2 * c3) + c2 * (c1 * c3 - c2 * c2)))

    a2 = float((n * (c2 * c7 - c3 * c6) - c1 * (c1 * c7 - c2 * c6) + c5 * (c1 * c3 - c2 * c2)) / (
            n * (c2 * c4 - c3 * c3) - c1 * (c1 * c4 - c2 * c3) + c2 * (c1 * c3 - c2 * c2)))

    # New data set for approximated polynomial is generated here
    initial = x[0]
    n_x = []
    n_y = []

    while initial <= x[len(x) - 1]:
        p = a0 + a1 * initial + a2 * initial * initial
        n_x.append(initial)
        n_y.append(p)
        initial += 0.01

    return n_x, n_y


# Given data set and iteration number is defined here
xGiven = [1, 4, 7, 11, 15, 20, 30, 50, 77, 92, 100]
yGiven = [5, 20, 52, 121, 228, 403, 903, 2504, 5929, 8464, 10005]

# User defined function is called here
xline, yline = least_square(xGiven, yGiven)

# Given data points are plotted in red and the appropriate fit using Least Square Method is plotted in blue
plt.plot(xGiven, yGiven,'ro', label='Given data points')
plt.plot(xline, yline, 'b--', label='Polynomial fit(Quadratic)')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()

plt.show()
