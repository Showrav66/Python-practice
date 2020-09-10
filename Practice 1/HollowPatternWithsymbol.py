n = 10
for i in range(n):
    print(" " * (n - i), end="")
    for j in range(i):
        if i > 2 and i < (n - 1):
            if j > 0 and j < (i - 1):
                print("  ", end="")
            else:
                print("*", "", end="")
        else:
            print("*", "", end="")
    print()