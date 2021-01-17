from EncoderStrategy import *

class EncodingManager:
    def __init__(self):
        self._encodingStrategy = None

    def setEncodingStrategy(self,arg):
    # plays the role of a factory methode defining the Strategy of Encoding
        if (arg == 'BASE64'):
            self._encodingStrategy = Base64Strategy()
        elif (arg == 'ASCCI'):
            self._encodingStrategy = ASCCIStrategy()

    def encodeString(self, arg):
        return(self._encodingStrategy.encode(arg))

    def decodeString(self, arg):
        return(self._encodingStrategy.decode(arg))    