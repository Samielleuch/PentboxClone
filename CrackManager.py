from CrackStrategy import *


class CrackManager:

    def setCrackStrategy(self, arg):
        # plays the role of a factory methode defining the Strategy of Cracking
        if (arg == 'BRUTE_FORCE'):
            self._crackStrategy = BruteForceStrategy()
        elif (arg == 'DICTIONARY_ATTACK'):
            self._crackStrategy = DictAttackStrategy()

    def crack(self, arg):
        return(self._crackStrategy.crack(arg))
