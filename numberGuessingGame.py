#julia golder
#3/1/18
#numberGuessingGame.py



import from randint(1,100)

num = randint(1,100)


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
    
