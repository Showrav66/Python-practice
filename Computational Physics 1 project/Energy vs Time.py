import numpy as np
import math
import matplotlib.pyplot as plt

# input
k1 = float(input("k1:"))
k2 = float(input("k2:"))
m = float(input("mass:"))
x_01 = float(input("initial position of the 1st mass:"))
x_02 = float(input("initial position of the 2nd mass:"))

p = -(k1 + k2) / m
q = k2 / m
A = np.array([[p, q], [q, p]])
x_0 = np.array([[x_01], [x_02]])

# eigenvalues & eigenvectors
eval, evect = np.linalg.eig(A)
v_inv = np.linalg.inv(evect)

# unknown coefficients b1,b2
mul = np.matmul(v_inv, x_0)
b1 = float(mul[0])
b2 = float(mul[1])

omega_1 = math.sqrt(-eval[0])
omega_2 = eval[1]
v_11 = evect[0][0]
v_21 = evect[0][1]
v_12 = evect[1][0]
v_22 = evect[1][1]

T = []
V = []
E = []
time = []
for t in np.arange(0, 1000, 0.5):
    x_1 = b1 * v_11 * math.cos(math.radians(omega_1) * t) + b2 * v_21 * math.cos(math.radians(omega_2) * t)
    x_2 = b1 * v_12 * math.cos(math.radians(omega_1) * t) + b2 * v_22 * math.cos(math.radians(omega_2) * t)
    x_1_dot = -omega_1 * b1 * v_11 * math.sin(math.radians(omega_1) * t) - omega_2 * b2 * v_21 * math.sin(
        math.radians(omega_2) * t)
    x_2_dot = -omega_1 * b1 * v_12 * math.sin(math.radians(omega_1) * t) - omega_2 * b2 * v_22 * math.sin(
        math.radians(omega_2) * t)

    KE = (m / 2) * (pow(x_1_dot, 2) + pow(x_2_dot, 2))
    PE = (m / 4) * ((pow(x_1, 2) + pow(x_2, 2)) * (pow(omega_1, 2) + pow(omega_2, 2)) + 2 * x_1 * x_2 * (
            pow(omega_1, 2) - pow(omega_2, 2)))

    T.append(KE)
    V.append(PE)
    E.append(KE + PE)
    time.append(t)

plt.plot(time, T, label="total kinetic energy")
plt.plot(time, V, label="total potential energy")
plt.plot(time, E, 'r--', label="total energy")
plt.xlabel('time')
plt.ylabel('energy')
plt.xlim(0, 500)
plt.legend()
plt.show()
