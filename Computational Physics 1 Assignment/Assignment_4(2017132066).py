'''
Computational Physics 1 Assignment 4
Name: Showrab Acharjee
Reg no: 2017132066
Session: 2017-18

Faddeev Leverrier method:
Sn = A * (S_n-1 - P_n-1*I) and P_n = (1/n) * Trace[S_n]
S_n = supplementary matrices
P_n = corresponding coefficients
'''


# Code starts here
# This function returns supplementary matrices and the coefficients of the polynomial using Faddeev Leverrier method.
def supplimentary_mat(ini_mat, mat, trace):
    I = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]

    mat2 = []
    for i in range(3):
        a = []
        for j in range(3):
            a.append(trace * I[i][j])
        mat2.append(a)

    sub = [[mat[i][j] - mat2[i][j] for j in range(3)] for i in range(3)]

    product = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                product[i][j] = product[i][j] + ini_mat[i][k] * sub[k][j]

    coeff = (product[0][0] + product[1][1] + product[2][2])

    return coeff, product, sub


matrix = []
print("Enter elements( rowwise) of the 3x3 matrix:")
for i in range(3):
    x = []
    for j in range(3):
        x.append(float(input()))
    matrix.append(x)

# Trace calculation
trace = matrix[0][0] + matrix[1][1] + matrix[2][2]

# Coefficients of the polynomial
c1 = trace
c2 = (1 / 2) * (supplimentary_mat(matrix, matrix, trace)[0])
c3 = (1 / 3) * (supplimentary_mat(matrix, (supplimentary_mat(matrix, matrix, trace)[1]), c2)[0])

x = (supplimentary_mat(matrix, matrix, trace))
y = supplimentary_mat(matrix, x[1], c2)[2]

# Printing characteristic polynomial
print("The characteristic polynomial is:")
p1 = "%+ d" % (c1)
p2 = "%+ d" % (c2)
p3 = "%+ d" % (c3)
p = "P(m) = -m^3" + " " + str(p1) + "m^2" + " " + str(p2) + "m" + " " + str(p3)
print(p)

# Inverse matrix
inv_mat = []
for i in range(3):
    a = []
    for j in range(3):
        entry = (1 / c3) * y[i][j]
        a.append("%0.4f" % entry)
    inv_mat.append(a)
print()

# Printing inverse matrix
print("The inverse matrix is:")
for i in range(3):
    for j in range(3):
        print(inv_mat[i][j], end="  ")
    print()
