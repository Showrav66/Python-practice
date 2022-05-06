'''Computational Physics 2 Homework 7
Name: Showrav Acharjee
Reg no: 2017132066
Session: 2017-18
Monte Carlo Simulation (Integration of Sin(x) in the limit x=0 to x=pi)
'''
import math
import random

n_fun = 0
n_tot = 0
area_box = (math.pi)**2

for i in range(1000000):
    x = random.uniform(0, math.pi)
    y = random.uniform(0, math.pi)
    f = math.sin(x)
    if y < f:
        n_fun = n_fun + 1
    n_tot = n_tot + 1

value = (n_fun*area_box)/n_tot
print("Integration of y(x)=sin(x):")
print(value)