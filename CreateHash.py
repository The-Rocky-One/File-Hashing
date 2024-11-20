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

    # Actual hash statement, though if for whatever reason hash.txt is unavailable, return an error.
    try:
        with open(path, "rb") as filePath:
            hashVal.update(filePath.read())
    except (IOError, OSError) as err:
        print(f"Error accessing hash.txt: {err}")

    inHTxt=False


    # Check to make sure Hash.txt exists.
    try:
        # Checking if the path is already in hash.txt, in which case skip adding it to hash.txt a second time.
        with open("hash.txt", "r") as hTxt:
            if hashVal.hexdigest() in hTxt.read().splitlines():
                inHTxt = True
    except FileNotFoundError:
        print("Hash.txt not found, creating new file.")

    if addHash.upper() == "Y":
        if inHTxt == False:
            with open("hash.txt", "a") as hTxt:
                hTxt.write(hashVal.hexdigest() + "\n")
        

    return hashVal.hexdigest(), inHTxt
