i = int(input('First number: '))
n = int(input('Last number: '))
d = int(input('Difference: '))


series = range(i,n+1,d)

sum = 0

for y in series:
    sum = sum + y*y
print(sum)