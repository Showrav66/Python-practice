
def count(list):
    for i in range(len(names)):
        if len(names[i])>5:
            print("The names with more than 5 letters:",names[i])
        else:
            print("You did not enter any names with more than 5 leters!!")
            break


names = list([])

for i in range(5):
    x = input("Enter next name:")
    names.append(x)

count(names)