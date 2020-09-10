
def ctf():

    x = float(input("Enter 1(celcius to farenheit) or 2(farenheit to celcius:"))
    z = float(input("Enter the value:"))

    if x==1:
        f = (9*z + 160)/5
        print(z,"degree celcius =",f,"degree farenheit")
    else:
        c = (5*z - 160)/9
        print(z,"degree farenheit =",c,"degree celcius")

ctf()