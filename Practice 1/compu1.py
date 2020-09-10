import math

T = float(input('Enter time='))
G = 6.67e-11
M = 5.97e24
R = 6371000

H = (G * M * (T ** 2) / (4 * (math.pi) ** 2)) ** (1 / 3) - R
print(f"The height is = {H}")
