import crypto
from CryptClass import Crypt

def start():
    password = setPassword()
    message = setMessage()
    Crypt.cryptMessage(password,message)
    Crypt.decryptMessage(password,message)



def setPassword():
    return input('Enter password: ')


def setMessage():
    return input('Enter message: ')