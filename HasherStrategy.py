import logging
import hashlib   
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class HasherStrategy(ABC):
    """
    interface that defines the way the Hashing is done
    """
    @abstractmethod
    def hash(self, string):
        pass

class Md5Strategy(HasherStrategy):
    def hash(self, str):
        logger.info(f"md5 Hash: {str}")
        #codage md5 
        hashed=hashlib.md5(str.encode()).hexdigest() 
        logger.info(f"Hashed Value is: {hashed} ")
        return(hashed)

class Sha512Strategy(HasherStrategy):
    def hash(self, str):
        logger.info(f"Sha512 Hash: {str}")
        hashed=hashlib.sha512(str.encode()).hexdigest() 
        logger.info(f"Hashed Value is: {hashed} ")
        return(hashed)
    