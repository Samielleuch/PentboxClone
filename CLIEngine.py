#!/usr/bin/env python3
import logging
import sys
from EncodingManager import *

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG ,format='%(message)s')

def encode(strat,string):
    encodingManager= EncodingManager()
    encodingManager.setEncodingStrategy(strat)
    return encodingManager.encodeString(string)

def decode(strat,string):
    encodingManager= EncodingManager()
    encodingManager.setEncodingStrategy(strat)
    return encodingManager.decodeString(string)

def main():
    encode('BASE64',"sami")
    decode('ASCCI',"test")

if __name__ == "__main__":
    main()