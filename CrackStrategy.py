import logging
from abc import ABC, abstractmethod

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

