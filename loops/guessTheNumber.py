#This is a number guessing game.
import random

secret_number = random.randint(1,21)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess a certain amount of times
for guesses_taken in range(1,7):
    print('Take a guess.')
    guess = int(input('> '))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break
if guess == secret_number:
    print('Congrats! You got the number in ' + str(guesses_taken) + ' guesses.')
else:
    print('Sorry, you ran out of guesses. The secret number was ' + str(secret_number))

