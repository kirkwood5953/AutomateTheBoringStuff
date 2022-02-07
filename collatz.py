def collatz(number):

    test = number % 2
    if test == 0:
        newNumber = number//2

    if test == 1:
        newNumber = 3*number+1

    print(newNumber)
    return newNumber

print('Enter number:')
try:
    num =int(input())

    while num != 1:
        num = collatz(num)

except ValueError:
    print('You didn\'t enter a number you silly goose')
