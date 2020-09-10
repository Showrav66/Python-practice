string = "Emma is good developer. Emma is a writer".split()
counter = 0
for i in range(len(string)-1):
    if string[0] == string[i]:
        counter+=1
print(counter)
print(string)