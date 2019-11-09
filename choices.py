from options import *

def choice():
    showOptions()
    choice = -1

    while not(choice < len(options()) and choice >= 0):
        try:
            choice = int(input('Option: '))
        except:
            print('Input number')
            choice = -1
    return choice