from EncrypterStrategy import *

class EncryptionManager:
    def __init__(self):
        self._encryptionStrategy = None

    def setEncryptionStrategy(self,arg):
    # plays the role of a factory methode defining the Strategy of encryption
        if (arg == 'AES'):
            self._encryptionStrategy = AESStrategy()
        elif (arg == 'RSA'):
            self._encryptionStrategy = RSAStrategy()

    def encryptString(self, arg):
        return(self._encryptionStrategy.encrypt(arg))

    def decryptString(self, arg):
        return(self._encryptionStrategy.decrypt(arg))    