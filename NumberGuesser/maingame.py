import random


def maingame(a, b, tries, diff):
    randnum = random.randint(a, b)
    print('\nI\'m thinking of a number between ' + str(a)+ ' and ' + str(b) + '.')
    print('Guess the number. You have ' + str(tries) + ' tries.')
    print('Difficulty - ' + diff)
    while tries != 0:
        print('Number of tries left = ' + str(tries))
        num = int(input('Take a Guess. \n'))
        if num < a or num > b:
            print('Out of Range.')
        else:
            tries = tries - 1
            if num < randnum:
                print('Too low. Try again.')
            elif num > randnum:
                print('Too high. Try again.')
            elif num == randnum:
                print('Correct!!!. The number I thought of was ' + str(randnum))
                break
        if tries == 0:
            print('Oops! You\'ve exhausted all your tries. \nThe number I thought of was ' + str(randnum))
            print('Replay to try again.')

