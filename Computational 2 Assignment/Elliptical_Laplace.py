'''Computational Physics 2 Homework 4
Name: Showrav Acharjee
Reg no: 2017132066
Session: 2017-18
This program solves the Laplace equation for a certain boundary condition by both Jacobi's and Gauss-Seidal method.
'''

import matplotlib.pyplot as plt

# Jacobi's method:
u11_n = 875
u12_n = 1000
u21_n = 375
u22_n = 625
ls1 = []
print("\nSolution of Laplace equation by Jacobi's method:")
print("The values are in the order of: [u11, u12, u21, u22]")
for i in range(30):
    u11_np1 = round((2000 + 500 + u12_n + u21_n) / 4, 2)
    u12_np1 = round((2000 + 1000 + u11_n + u22_n) / 4, 2)
    u21_np1 = round((u11_n + u22_n) / 4, 2)
    u22_np1 = round((500 + 1000 + u12_n + u21_n) / 4, 2)
    ls1.append(u11_np1)
    ls1.append(u12_np1)
    ls1.append(u21_np1)
    ls1.append(u22_np1)
    if u11_n == u11_np1 and u12_n == u12_np1 and u21_n == u21_np1 and u22_n == u22_np1:
        print(ls1)
        print("**{}th and {}th iteration values matched**".format(i-1,i))
        break
    ls1.clear()
    u11_n = u11_np1
    u12_n = u12_np1
    u21_n = u21_np1
    u22_n = u22_np1


# Gauss-Seidal method
ls2=[]
print("\nSolution of Laplace equation by Gauss-Seidal method:")
print("The values are in the order of: [u11, u12, u21, u22]")
for i in range(10):
    u11_np1 = round((2000 + 500 + u12_n + u21_n) / 4, 2)
    u22_np1 = round((500 + 1000 + 1000 + u11_np1) / 4, 2)
    u12_np1 = round((2000 + 1000 + u11_np1 + u22_np1) / 4, 2)
    u21_np1 = round((u11_np1 + u22_np1) / 4, 2)
    ls2.append(u11_np1)
    ls2.append(u12_np1)
    ls2.append(u21_np1)
    ls2.append(u22_np1)
    if u11_n == u11_np1 and u12_n == u12_np1 and u21_n == u21_np1 and u22_n == u22_np1:
        print(ls1)
        print("**{}th and {}th iteration values matched**".format(i-1,i))
        break
    ls2.clear()
    u11_n = u11_np1
    u12_n = u12_np1
    u21_n = u21_np1
    u22_n = u22_np1