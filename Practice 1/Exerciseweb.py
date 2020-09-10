def func():
    string = input("Enter a string: ")
    for i in range(0,len(string)):
        if i%2==0:
            print("Index",[i],string[i])

func()