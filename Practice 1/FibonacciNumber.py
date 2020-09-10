#Fibonacci number generator:
def fibo(n):
    a = 0
    b = 1
    if n<0:
        print("Opps!!You can't enter negative number")
    elif n==0:
        print()
    elif n==1:
        print(a)
    else:
        print("0 1",end=" ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            if c==0 and c==1:
                continue
            print(c,end=" ")

print("Generate Fibonacci numbers")
x = int(input("Enter no of terms:"))
fibo(x)

