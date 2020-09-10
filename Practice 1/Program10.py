from random import randint

n=int(input('How many times do you want to try? '))

for i in range(1,n+1):
    guessNumber = int(input('Enter your guess between 1 to 5: '))
    randomNumber =randint(1,5)
    if guessNumber == randomNumber:
        print('You Have Won')
    else:
        print('You Have Lost')
