n = int(input("Enter a number of n: "))
for i in range(1,n):
    print(" "*(n-i),end="")
    for j in range(i):
        print(i,'',end="")
    print()