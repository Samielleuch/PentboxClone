import logging
from abc import ABC, abstractmethod
from HashingManager import *

logger = logging.getLogger(__name__)


class CrackStrategy(ABC):
    """
    interface that defines the way the cracking is done
    """

    @abstractmethod
    def crack(self, string):
        """
        find the hidden value in the hash
        """
        pass



class BruteForceStrategy(CrackStrategy):
    def crack(self, str):
        logger.info(f"Cracking brute Force: {str}")
   
class DictAttackStrategy(CrackStrategy):
    def crack(self, str):
        logger.info(f"Cracking with Dictionnary Attack: {str}")
        logger.info('\n Checking...\n\n')
        file = open("dict.txt", 'r', encoding='utf-8')
        words = file.read()
        file.close()
        wordlist= words.split()
        #call the hasher
        hashingManager = HashingManager()
        hashingManager.setHashingStrategy('md5')
        found=0
        for word in wordlist:
            test = hashingManager.hashString(word)
            if test == str:
                logger.info(f"\n ***\n ur password is : {word} \n ***\n ")
                found=1
                break

        if(found == 0):
            logger.info("\n password not found \n")


