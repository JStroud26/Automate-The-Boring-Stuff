name = ''
tries = 0
while name != 'your name':
    print('Please type your name')
    name = input('> ')
    tries = tries + 1
    if tries == 10:
        print('You should really just type your name.')
        print('')
    elif tries == 15:
        print('You might be retarted! Keep trying though.')
        print('')
print('Thanks idiot, it only took you ' + str(tries) + ' tries')
