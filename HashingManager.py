from HasherStrategy import *

class HashingManager:
    def __init__(self):
        self._hashingStrategy = None

    def setHashingStrategy(self,arg):
    # plays the role of a factory methode defining the Strategy of Encoding
        if (arg == 'md5'):
            self._hashingStrategy = Md5Strategy()
        elif (arg == 'SHA-512'):
            self._hashingStrategy = Sha512Strategy()

    def hashString(self, arg):
        return(self._hashingStrategy.hash(arg))
