from crypt.Fernet import Fernet

class Crypt:
    
    @staticmethod
    def cryptMessage(password,message):
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(message)
        print(cipher_text)


    @staticmethod
    def decryptMessage(password,message):
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        plain_text = cipher_suite.decrypt(message)
        print(plain_text)