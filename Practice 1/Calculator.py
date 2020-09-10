# CALCULATOR

print("What operation do you like to do?(+,-,*,/):")
sign = input()
try:
    a, b = int(input()), int(input())
    if sign == "+":
        print("Sum is:", a + b)
    elif sign == "-":
        print("Subtraction is:", a - b)
    elif sign == "*":
        print("Multiplication is:", a * b)
    elif sign == "/":
        print("Quotient is:", a / b)
except ZeroDivisionError:
    print("Oops! you can't divide by 0..Try again...")

# END
