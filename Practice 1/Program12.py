nol=0
nod=0
now=0
n = input('Enter a text string: ')

for i in n:
     i = i.lower()
     if i<='z' and i>='a':
         nol = nol + 1
     elif i>='0' and i<='9':
         nod = nod +1
     elif i == ' ':
         now = now + 1
print('Number of letters:',nol)
print('Number of digits:',nod)
print('Number of words:',now+1)


