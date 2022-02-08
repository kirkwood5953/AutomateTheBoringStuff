import random

number = random.randint(1,21)
guessnum = 0


print('I am thinking of a number between 1 and 20.')
print('Take a guess.')

guess = int(input())
while guess != number:
    if guess > number:
        print('thats a little too high')
        guess = int(input())
    elif guess < number:
        print('thats a little too low')
        guess = int(input())
    guessnum = guessnum + 1
if guess == number:
    print('Congrats thats correct!')
    print('It took you ' + str(guessnum+1) + ' attempts')
