'''Computational Physics 2 Homework 8
Name: Showrav Acharjee
Reg no: 2017132066
Session: 2017-18
Monte Carlo Simulation (Probability of finding a dot inside a circle surrounded by a square of side length 2)
'''
import random

n_fun = 0
n_tot = 0

for i in range(1000000):
    x = random.uniform(0,1)
    y = random.uniform(0, 1)
    f = (1-x*x)**0.5
    if y < f:
        n_fun = n_fun + 1
    n_tot = n_tot + 1

probability = n_fun/n_tot

print("Probability of finding a dot inside the circle:")
print(probability)
