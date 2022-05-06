'''Computational Physics 2 Homework 5
Name: Showrav Acharjee
Reg no: 2017132066
Session: 2017-18
This program plots the solution curves of 1D Heat Equation against position and time using Bender-Schmidt method.
'''
import math
import matplotlib.pyplot as plt

x = [0, 0.2, 0.4, 0.6, 0.8, 1]
t = [0, 0.02, 0.04, 0.06, 0.08, 0.1]
u0 = []

for i in range(6):
    p = math.sin(math.radians(180*x[i]))
    u0.append(p)

def calc(f):
    data = []
    a = 0
    b = 2
    uim1_j = f[a]
    uip1_j = f[b]

    for i in range(4):
        ui_jp1 = 0.5*(uim1_j + uip1_j)
        data.append(ui_jp1)
        if i == 3:
            break
        a = a+1
        b = b+1
        uim1_j = f[a]
        uip1_j = f[b]

    return data

u1 = calc(u0)
u1.insert(0, 0)
u1.insert(5, 0)
u2 = (calc(u1))
u2.insert(0, 0)
u2.insert(5, 0)
u3 = (calc(u2))
u3.insert(0, 0)
u3.insert(5, 0)
u4 = (calc(u3))
u4.insert(0, 0)
u4.insert(5, 0)
u5 = (calc(u4))
u5.insert(0, 0)
u5.insert(5, 0)

v = []
for i in range(6):
    vi = [u0[i], u1[i], u2[i], u3[i], u4[i], u5[i]]
    v.append(vi)
v0 = v[0]
v1 = v[1]
v2 = v[2]
v3 = v[3]
v4 = v[4]
v5 = v[5]

plt.style.use('seaborn')
plt.title("u(x) vs x")
plt.plot(x, u0)
plt.plot(x, u1)
plt.plot(x, u2)
plt.plot(x, u3)
plt.plot(x, u4)
plt.plot(x, u5)
plt.xlabel("x")
plt.ylabel("u(x)")
plt.show()

plt.style.use('seaborn')
plt.title("u(t) vs t")
plt.plot(t, v0)
plt.plot(t, v1)
plt.plot(t, v2)
plt.plot(t, v3)
plt.plot(t, v4)
plt.plot(t, v5)
plt.xlabel("t")
plt.ylabel("u(t)")
plt.show()