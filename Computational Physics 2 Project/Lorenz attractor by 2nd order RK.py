from cProfile import label
from matplotlib import pyplot as plt
import numpy as np

h=0.001
xn=1
yn=1
zn=1
t_sol=[]
x_sol=[]
y_sol=[]
z_sol=[]

for i in np.arange(0,100,0.01):
    k1 = 10*h*(yn-xn)
    l1 = h*(28*xn-xn*zn-yn)
    m1 = h*(xn*yn-(8/3)*zn)

    k2 = 10*h*(yn-(xn+k1))
    l2 = h*(28*xn-xn*zn-(yn+l1))
    m2 = h*(xn*yn-(8/3)*(zn+m1))

    xn_1 = xn + 1/2 * (k1 + k2)
    yn_1 = yn + 1/2 * (l1 + l2)
    zn_1 = zn + 1/2 * (m1 + m2)

    if i==0:
        xn_1 = xn
        yn_1 = yn
        zn_1 = xn

    t_sol.append(i)
    x_sol.append(xn_1)
    y_sol.append(yn_1)
    z_sol.append(zn_1)

    xn = xn_1
    yn = yn_1
    zn = zn_1

# plt.style.use('seaborn')
# plt.plot(t_sol,y_sol,label='position')
# plt.plot(t_sol,z_sol,label='velocity')
# plt.title('Solution of an 1D SHO by 2nd order Runge-kutta method')
# plt.xlabel('time')
# plt.ylabel('x(t),v(t)')
# plt.xlim(0)
# plt.legend()
# print(t_sol,x_sol)

fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.plot(x_sol,y_sol,z_sol)
plt.figure(2)
plt.subplot(3,1,1)
plt.title('x vs t')
plt.plot(t_sol,x_sol,label='x')
plt.subplot(3,1,2)
plt.title('y vs t')
plt.plot(t_sol,y_sol,label='y')
plt.subplot(3,1,3)
plt.title('z vs t')
plt.plot(t_sol,z_sol,label='z')
plt.legend()
plt.show()
