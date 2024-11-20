### Author: Stone Provo, 000854122 ###
### Created 11-19-1024 ###
### CreateHash.py ###

#### This script will create, compare, and store a hash value into hash.txt ####

### Imports ###
#Unsure if I'll need all of these imports, but since they're imported to main.py, it couldn't hurt.
import argparse
import hashlib
import os
### Imports ###

def createHash(path,algorithm,addHash):
    hashVal = hashlib.new(algorithm)

    # Actual hash statement, though if for whatever reason hash.txt is unavailable, an error will print.
    try:
        with open(path, "rb") as filePath:
            hashVal.update(filePath.read())
    except (IOError, OSError) as err:
        print(f"Error accessing hash.txt: {e}")

    inHTxt=False


    # Checking if the path is already in hash.txt, in which case skip adding it to hash.txt a second time. Basically a repeat of hashCompare, but it's fine.
    try:
        with open("hash.txt", "r") as hTxt:
            if hashVal.hexdigest() in hTxt.read().splitlines():
                inHTxt = True
    except FileNotFoundError:
        pass

    if addHash.upper() == ("Y"):
        if inHTxt == False:
            with open("hash.txt", "a") as hTxt:
                hTxt.write(hashVal.hexdigest() + "\n")
    
    return hashVal.hexdigest(), inHTxt
