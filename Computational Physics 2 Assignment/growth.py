'''Computational Physics 2 Assignment 1
Name: Showrav Acharjee
Reg no: 2017132066
Session: 2017-18

This program plots the solution curves of nuclear growth equation by Taylor's and Euler's method along with the exact solution curve.
'''

from matplotlib import pyplot as plt
import numpy as np
import math
time=[]
taylor=[]
exact=[]
euler=[]
N0=1
for i in np.arange(0,5,0.1):
    N1= 1 + i + 0.5*i*i + (1/6)*i*i*i
    N2 = 1*(math.exp(i))
    N3 = N0 + 0.1*(N0)
    if i==0:
        N3=N0
    taylor.append(N1)
    time.append(i)
    exact.append(N2)
    euler.append(N3)
    N0=N3

plt.plot(time,taylor,label='Taylor')
plt.plot(time,euler,label='Euler')
plt.plot(time,exact,label='Exact')
plt.ylim(0,110)
plt.title('Growth curve')
plt.xlabel('time(s)')
plt.ylabel('Number of nuclei')
plt.legend()
plt.show()