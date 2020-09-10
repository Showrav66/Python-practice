def printEveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = input("Enter String ")
print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEveIndexChar(inputStr)