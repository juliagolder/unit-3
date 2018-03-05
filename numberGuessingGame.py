#julia golder
#3/1/18
#numberGuessingGame.py



from random import randint

num = randint(1,100)

total = 0

while True:
    guess = int(input('Guess a number between 1 and 100: '))
    total = total + 1
    if guess == num:
        print('You go it in', total, 'tries')
        break
    elif guess > num:
        print('This is too high!')
    else:
        print('This is too low!')
