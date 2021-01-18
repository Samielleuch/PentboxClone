import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class EncrypterStrategy(ABC):
    """
    interface that defines the way the encryption is done
    """

    @abstractmethod
    def encrypt(self, string):
        """
        encrypr
        """
        pass

    @abstractmethod
    def decrypt(self, string):
        """
        decrypt
        """
        pass


class AESStrategy(EncrypterStrategy):
    def encrypt(self, str):
        logger.info(f"Encryption AES: {str}")
    def decrypt(self, str):
        logger.info(f"Decryption AES: {str}")

class RSAStrategy(EncrypterStrategy):
    def encrypt(self, str):
        logger.info(f"Encryption RSA: {str}")
    def decrypt(self, str):
        logger.info(f"Decryption RSA: {str}")
