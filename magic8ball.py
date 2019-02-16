import random

print("Ask me a question, mortal.")
input('>> ')

def result(random):
    if random == 1:
        return 'No!!'
    elif random == 2:
        return 'Maybe..'
    elif random == 3:
        return 'Yes!'
    elif random == 4:
        return 'Try again later.'
    elif random == 5:
        return 'Eehhh.. try again'
    elif random == 6:
        return 'Do not ask me such a stupid thing.'
    elif random == 7:
        return 'Wrong neighborhood, bucko.'
    elif random == 8:
        return 'Are you serious?'
    elif random == 9:
        return 'I love you.'
r = random.randint(1,9)
fortune = result(r)
print(fortune)