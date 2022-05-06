'''Computational Physics 2 Homework 9
Name: Showrav Acharjee
Reg no: 2017132066
Session: 2017-18
Variational Monte Carlo method for the Simple Harmonic Oscillator to estimate the ground state energy
'''

import numpy as np

L = 9.046*10**10
alpha = 0.5*L
sigma = 1/(2*alpha**0.5)
mu = 0

E = []
N = 100000
x = np.random.normal(mu, sigma, N)
for i in x:
    E_0 = -(-2*alpha + 4*alpha**2*i**2)/(2*L) + (L*i**2)/2
    E.append(E_0)

sum = 0
for i in range(0, len(E)):
    sum = sum + E[i]

expectation_value = sum / N

print("The ground state energy of SHO is:")
print(expectation_value, "ħω")