import random
myNumber = random.randint(1, 20)
tries = 0
print('I\'m thinking of a number between 1 and 20, Guess the number. You have 7 tries.')
# Ask the user to guess
while tries < 8:
    print('Number of tries left = ' + str(7-tries))
    num = int(input('Take a guess \n'))
    if num < 1 or num > 20:
        print('Please input a valid number!')
    else:
        tries = tries + 1
        if num < myNumber:
            print('Too low, try again')
        elif num > myNumber:
            print('Too high, try again')
        elif num == myNumber:
            print('Correct!! The number I thought of is ' + str(myNumber))
            break
if tries > 7:
    print('Sorry you exhausted your tries. The number is ' + str(myNumber))