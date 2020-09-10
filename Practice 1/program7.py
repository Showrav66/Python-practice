i = int(input('First number: '))
n = int(input('Last number: '))
d = int(input('Difference: '))


series = range(i,n+1,d)

for x in series:
    new= 1/x
    print(new)

