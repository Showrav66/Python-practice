'''Computational Physics 2 Assignment 2
Name: Showrav Acharjee
Reg no: 2017132066
Session: 2017-18

This program plots the solution curves of position and velocity for an simple harmonic oscillator by 2nd order Runge-Kutta method.
'''

from matplotlib import pyplot as plt
import numpy as np

h=0.1
Xn=1
Zn=0
t_sol=[]
y_sol=[]
z_sol=[]

for i in np.arange(0,10,0.1):
    k1 = h*Zn
    l1 = -h*Xn
    k2 = h*(Zn + l1)
    l2 = -h*(Xn + k1)

    Yn_1 = Xn + 1/2 * (k1 + k2)
    Zn_1 = Zn + 1/2 * (l1 + l2)

    if i==0:
        Yn_1 = Xn
        Zn_1 = Zn

    t_sol.append(i)
    y_sol.append(Yn_1)
    z_sol.append(Zn_1)

    Xn = Yn_1
    Zn = Zn_1

plt.style.use('seaborn')
plt.plot(t_sol,y_sol,label='position')
plt.plot(t_sol,z_sol,label='velocity')
plt.title('Solution of an 1D SHO by 2nd order Runge-kutta method')
plt.xlabel('time')
plt.ylabel('x(t),v(t)')
plt.xlim(0)
plt.legend()
plt.show()
