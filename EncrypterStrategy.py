import hashlib
import ast
from Crypto.Cipher import AES
import base64
import os
import math
import logging
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
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
        IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
        KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
        SALT_SIZE = 16  # This size is arbitrary
        password = b'this is my highly secure encryption password'
        salt = os.urandom(SALT_SIZE)
        derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000,
                                      dklen=IV_SIZE + KEY_SIZE)
        iv = derived[0:IV_SIZE]
        key = derived[IV_SIZE:]
        encrypted = salt + \
            AES.new(key, AES.MODE_CFB, iv).encrypt(str.encode('ascii'))
        #we now encode it to base64
        base64_encrypted = base64.b64encode(encrypted).decode('ascii')

        logger.info(f"\nEncrypted value: {base64_encrypted}")

    def decrypt(self, str):
        IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
        KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
        SALT_SIZE = 16  # This size is arbitrary
        password = b'this is my highly secure encryption password'
        logger.info(f"Decryption AES: {str}")
        message_bytes =  base64.b64decode(str)
        salt = message_bytes[0:SALT_SIZE]
        derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000,
                                      dklen=IV_SIZE + KEY_SIZE)
        iv = derived[0:IV_SIZE]
        key = derived[IV_SIZE:]
        cleartext = AES.new(key, AES.MODE_CFB, iv).decrypt(
            message_bytes[SALT_SIZE:])
        logger.info(f"\n original value: {cleartext}")







class RSAStrategy(EncrypterStrategy):
    def __init__(self):
        #creation d´un couple de clés
        self.key=RSA.generate(1024)

    def encrypt(self, str):
        logger.info(f"Encryption RSA: {str}")
        #afficher ses clés:
        k = self.key.exportKey('PEM')
        p = self.key.publickey().exportKey('PEM')
        logger.info(f"\n private key : \n {k}")
        logger.info(f"\n public key : \n {p}")
        #sauvegarder ses clés dans des fichiers:
        with open('private.pem','w') as kf:
            kf.write(k.decode())
            kf.close()
            
        with open('public.pem','w') as pf:
            pf.write(p.decode())
            pf.close()
        #chiffrage
        public_key = self.key.publickey()
        encryptor = PKCS1_OAEP.new(public_key)
        encrypted = encryptor.encrypt(bytes(str,"utf8"))
        #we now encode it to base64
        base64_encrypted = base64.b64encode(encrypted).decode('ascii')
        logger.info(f"\nEncrypted value: {base64_encrypted}")
        with open('encrypted.txt','w') as kf:
	        kf.write(base64_encrypted)
	        kf.close()
        logger.info("\nencrypted value saved at encrypted.txt")
        logger.info("\nkeys saved as private.pem and public.pem")




    def decrypt(self, str):
        logger.info(f"Decryption RSA: {str}")
        str =  base64.b64decode(str)
                #dechiffrage
                #importer des clés utilisé pendant le chiffrage
        with open('private.pem','r') as fk:
            priv = fk.read()
            fk.close()
        
        private = RSA.importKey(priv)

        decryptor = PKCS1_OAEP.new(private)
        decrypted = decryptor.decrypt(str)
        x =decrypted.decode('utf-8')
        logger.info(f"Decrypted value: {x}")
