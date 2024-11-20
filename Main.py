### Author: Stone Provo, 000854122 ###
### Created 11-19-1024 ###
### Main.py ###

#### This script is meant to handle the command line interface, and the error checking itself, otherwise it calls on two others, CreateHash and CompareHash to create and compare the hash values respectively. ####

### Imports ###
from CreateHash import createHash
import argparse
import hashlib
import os
### Imports ###

# CMD line interface
def cmdLineIn():

    #type=lambda is really cool. I could call a function by just specifying it as the type without values, but with lambda, I can full on call a function inside the cmd line argument to check it
    parser = argparse.ArgumentParser(description="Enter the file path you wish to generate a hash value of.")
    parser.add_argument("-Path", "--path", type=lambda value: errorCheck("path",value), help="The path to the file you wish to generate a hash value of.")
    parser.add_argument("-Algorithm", "--algorithm", type=lambda value: errorCheck("algorithm",value), default="sha256", help="The algorithm you wish to use to generate a hash value. Defaults to SHA-256.")
    parser.add_argument("-Compare", "--compare", type=lambda value: errorCheck("compare",value), default=False, help="True if you wish to compare this hash to the content of hash.txt. False if not.")
    args=parser.parse_args()


    # If the user doesn't want to compare hash, run createHash and add to hash.txt.
    # If they do want to compare hash, don't add the hash value to hash.txt, ask if they'd like to add it later.
    if args.compare == False:
        addHash=("Y")
    if args.compare == True:
        addHash=("N")
    
    hashVal, inHTxt =createHash(args.path,args.algorithm,addHash)


    #Printing output to screen
    print()
    print(f"File Path:              {args.path}")
    print(f"Hashing Algorithm:      {args.algorithm}")
    print(f"Compare with Hash.txt:  {args.compare}")
    print(f"Hashed value:           {hashVal}")
    print()
    
    #If the user wanted to compare, check if it's in hash.txt, if it's not, ask if they'd like to add it. 
    if args.compare == True:
        if inHTxt == False:
            print(f"Entry {hashVal} ({args.path}) using {args.algorithm} does not exist in hash.txt.")

            # Ask the user if they'd like to add the entry after comparison. Loop it to make sure they enter the right input, if they don't, give them 3 tries before exiting.
            for i in range(3):
                addHash=input("Would you like to add this entry? (Y or N):")
                print()
                if addHash.upper() in ("Y","N"):
                    break
                print('Invalid input. Please enter "Y" or "N".')
                print()
            else:
                print("Too many invalid attempts. Exiting.")
                print()
                return



            
            createHash(args.path,args.algorithm,addHash)
            if addHash.upper()=="Y":
                print(f"Adding entry {hashVal} ({args.path}) using {args.algorithm} to hash.txt")
            else:
                print("Entry ignored.")
        else:
            print(f"Entry {hashVal} ({args.path}) using {args.algorithm} already exists in hash.txt.")

    #If the user didn't want to compare, the value will be added to hash.txt automatically.
    if args.compare == False:
        print(f"Adding entry {hashVal} ({args.path}) using {args.algorithm} to hash.txt")
  
    print()


# Checking for Errors in cmd line input
def errorCheck(name, value):

    # Error check for the -Path value. I opt to use raise, since it's basically an error formatted version of return. That, plus it lets me be a lot more surgical with wwhat exactly went wrong with the command line.
    if name == "path":
        if not os.path.exists(value):
            raise argparse.ArgumentTypeError(f'Path: "{value}" does not exist.')
        return value

    # Error check for the -Algorithm value
    elif name == "algorithm":

        # Normalizes the algorithm value, since hashlib wants it to be something like sha256 instead of SHA-256 or SHA 256.
        normValue = value.lower().replace("-","").replace(" ","")
        if normValue not in hashlib.algorithms_available:
            raise argparse.ArgumentTypeError(f'Invalid algorithm: "{value}"')
        return normValue

    elif name == "compare":
        
        # Just in case the user enters a string instead of a boolean, check for common strings they'd enter. Chatgpt helped a little here, I asked it some common ways to specify true and false that weren't "True" and "False".
        if type(value) == str:
            if value.lower() in ("true","1","yes","y"):
                return True
            if value.lower() in ("false","0","no","n"):
                return False

        # Quick check if it's a bool value, and thus True or False.
        elif type(value) == bool:
            return value
        raise argparse.ArgumentTypeError(f'-Compare value "{value}" not recognized.')

    else:
        raise argparse.ArgumentTypeError(f'Unknown argument: "{name}"')
            
        

if __name__ == "__main__":
    cmdLineIn()
