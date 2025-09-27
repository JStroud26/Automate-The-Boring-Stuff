import random

def get_answer(answer_number): #will return fortune answer based on what int answer_number is assigned (1-9)
    if answer_number == 1:
        return 'It is certain.'
    elif answer_number == 2:
        return 'Maybe so.'
    elif answer_number == 3:
        return 'Perhaps not.'
    elif answer_number == 4:
        return 'Yes.'
    elif answer_number == 5:
        return 'Instructions unclear, try again.'
    elif answer_number == 6:
        return 'Ask again later. :)'
    elif answer_number == 7:
        return 'Concentrate and ask again.'
    elif answer_number == 8:
        return 'Outlook is not so good.'
    elif answer_number == 9:
        return 'Very doubtful'

print('Ask a yes or no question: ')
input('> ')
r = random.randint(1,9)
fortune = get_answer(r)
print(fortune)

