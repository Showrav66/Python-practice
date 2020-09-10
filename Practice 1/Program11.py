#taking list input from user

n=input('Enter your numbers with space: ')
list = n.split()
sum = 0
for num in list:
    sum = sum + int(num)
print(sum)