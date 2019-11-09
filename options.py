from logo import *

def options():
    return [
        'Crypt message',
        'Crypt mail',
        'Crypt file',
        'String option'
    ]


def showOptions():
    _options = options()
    print(logo())
    for option in range(0,len(_options)):
        print('['+str(option)+']',_options[option])