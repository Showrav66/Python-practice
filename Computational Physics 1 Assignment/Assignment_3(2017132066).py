'''Computational Physics 1 Assignment 3
Matrix(nxn) summation, subtraction and multiplication
Name: Showrab Acharjee
Reg no: 2017132066
Session: 2017-18
'''
import sys

n = int(input("Enter no of matrices(nxn):"))

matrices = []

# Taking input from user
for i in range(n):
    matrix = []
    r = int(input("Enter no of rows:"))
    c = int(input("Enter no of columns:"))
    # Exception handling
    if r != c:
        sys.exit("Order of the matrix are invalid for the operations")
    while i == 1:
        if r != len(matrices[0]):
            sys.exit("Order of the matrix are invalid for the operations")
    # Taking matrix elements input from user
    else:
        print("Enter elements(rowwise):")
        for i in range(r):
            x = []
            for j in range(c):
                x.append(float(input()))
            matrix.append(x)
        matrices.append(matrix)

# Addition calculation
sum = [[matrices[0][i][j] + matrices[1][i][j] for j in range(len(matrices[0][0]))] for i in range(len(matrices[0]))]

# Subtraction calculation
sub = [[matrices[0][i][j] - matrices[1][i][j] for j in range(len(matrices[0][0]))] for i in range(len(matrices[0]))]

# Multiplication calculation
product = [[0 for i in range(len(matrices[1][0]))] for j in range(len(matrices[0]))]

for i in range(len(matrices[0])):
    for j in range(len(matrices[1][0])):
        for k in range(len(matrices[1])):
            product[i][j] = product[i][j] + matrices[0][i][k] * matrices[1][k][j]

# Results printing
for k in range(3):
    if k == 0:
        print("Addition:")
        for i in range(len(sum)):
            for j in range(len(sum[0])):
                print(sum[i][j], end="  ")
            print()
    elif k == 1:
        print("Subtrction:")
        for i in range(len(sub)):
            for j in range(len(sub[0])):
                print(sub[i][j], end="  ")
            print()
    elif k == 2:
        print("Multiplication:")
        for i in range(len(product)):
            for j in range(len(product[0])):
                print(product[i][j], end="  ")
            print()
    print()
