while True:
    print('Who are you?')
    name = input('> ')

    if name != 'joe':
        continue
    print('Hello joe, what is the password? (It is a fish)')
    password = input('> ')
    if password == 'swordfish':
        break
    elif password != 'swordfish':
        print('Incorrect password, try again')
print('Access Granted')