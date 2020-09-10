def fact(n):
    if n==0:
        return 1
    fct = n * fact(n - 1)
    return fct


x = int(input('Enter a number:'))
print(x,'! =',fact(x))
