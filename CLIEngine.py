#!/usr/bin/env python3
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
import logging
import sys
from EncodingManager import *
from HashingManager import *
from EncryptionManager import *
from CrackManager import *
from Menus import *

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                    format='%(message)s')


style = style_from_dict({
    Token.Separator: '#f44336 bold',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def encode(strat, string):
    encodingManager = EncodingManager()
    encodingManager.setEncodingStrategy(strat)
    return encodingManager.encodeString(string)


def decode(strat, string):
    encodingManager = EncodingManager()
    encodingManager.setEncodingStrategy(strat)
    return encodingManager.decodeString(string)


def hash(strat, string):
    hashingManager = HashingManager()
    hashingManager.setHashingStrategy(strat)
    return hashingManager.hashString(string)


def crack(strat, string):
    crackManager = CrackManager()
    crackManager.setCrackStrategy(strat)
    return crackManager.crack(string)


def encrypt(strat, string):
    encryptionManager = EncryptionManager()
    encryptionManager.setEncryptionStrategy(strat)
    return encryptionManager.encryptString(string)


def decrypt(strat, string):
    encryptionManager = EncryptionManager()
    encryptionManager.setEncryptionStrategy(strat)
    return encryptionManager.decryptString(string)

def sign(strat, string):
    encryptionManager = EncryptionManager()
    encryptionManager.setEncryptionStrategy(strat)
    return encryptionManager.Sign(string)


def verify(strat, string):
    encryptionManager = EncryptionManager()
    encryptionManager.setEncryptionStrategy(strat)
    return encryptionManager.Verify(string)


def main():
    keepLooping = 1
    while(keepLooping):
        print('************')
        answers = prompt(questions, style=style)
# codage ou decodage
        if(answers['option'][0] == '1'):
            answer = prompt(CodOrDec)
            if(answer['choice'] == 'codage'):
                algorithme = prompt(algorithmesCodage)
                encode(algorithme['choice'], answer['str'])
            else:
                algorithme = prompt(algorithmesCodage)
                decode(algorithme['choice'], answer['str'])
# Hashage
        if(answers['option'][0] == '2'):
            logging.debug('Hashing...')
            answer = prompt(algorithmesHashage)
            hash(answer['choice'], answer['str'])
# Craquage
        if(answers['option'][0] == '3'):

            logging.debug('Cracking...')
            answer = prompt(CrackAttack)
            crack(answer['choice'], answer['str'])

# Chiffrement et déchiffrement symétrique
        if(answers['option'][0] == '4'):
            answer = prompt(ChifOrDechif)
            algorithme = prompt(algorithmesSymetrique)
            if(answer['choice'] == 'chiffre'):
                encrypt(algorithme['choice'], answer['str'])
            else:
                decrypt(algorithme['choice'], answer['str'])
# Chiffrement et déchiffrement asymétrique
        if(answers['option'][0] == '5'):
            logging.debug('Chiffrement Asymetrique ...')
            answer = prompt(ChifOrDechif)
            algorithme = prompt(algorithmesAsymetrique)
            if(answer['choice'] == 'chiffre'):
                encrypt(algorithme['choice'], answer['str'])
            elif(answer['choice'] == 'dechiffre'):
                decrypt(algorithme['choice'], answer['str'])
            elif(answer['choice'] == 'sign'):
                sign(algorithme['choice'], answer['str'])
            elif(answer['choice'] == 'verif'):
                verify(algorithme['choice'], answer['str'])
# Exit
        if(answers['option'][0] == '6'):
            logger.info('\n Exiting ... \n')
            keepLooping = 0

        print('************\n')


if __name__ == "__main__":
    main()
