from matplotlib import pyplot as plt

H = float(input('Enter Total height in meter:'))
T = float(input('Enter time in seconds:'))

save_height = []
save_time = []

for t in range(1, int(T + 1)):
    S = 0.5 * 9.81 * t ** 2
    h = H - S
    if h < 0:
        break
    print('Height at time', t, 's', 'is', h, 'm')
    save_height.append(h)
    save_time.append(t)

print(save_height)
print(save_time)

x = save_time
y = save_height

plt.plot(x, y, 'ro')
plt.plot(x,y)
plt.xlabel('Time in seconds')
plt.ylabel('Height in m')
plt.show()
