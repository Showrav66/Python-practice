file = open("new.txt","r")

text = file.readlines()[1]
print(text)
size = len(text)
print(size)
