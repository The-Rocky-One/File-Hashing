# File-Hashing and Comparison
Author: Stone Provo, 000854122.
This project provides a Command Line Interface (CLI) tool to generate and compare the hash values of files using various hashing algorithms. It includes the functionality to store these hash values in a file and reference that file for comparison.

## Features
<b>- Generate File Hash Values:</b> The program generates a hash value for a specified file using one of various hashing algorithms. (Default: SHA-256)
<b>- Storing File Hash Values:</b> Using a text file (hash.txt), the program is capable of storing and referencing old hash values.
<b>- Compare File Hash Values:</b> The program can compare a fresh file hash to those inside hash.txt, searching through the entire contents of the file for a match.
<b>- Supports Multiple Algorithms</b> It supports all hashing algorithms in the hashlib library.

## Installation
### Pre-Requisites
- Python 3.x
  - Ensure your Python installation is up to date by running the "python --version" command on your command line interface.
- The following imports, all of which are part of Python's standard library:
  - argparse
  - os
  - hashlib

### Steps for Installation
1. Clone this repository by using "git clone https://github.com/The-Rocky-One/File-Hashing.git".
2. Navigate to the File-Hashing directory by using "cd File-Hashing".
3. Run the program, as shown below.

## Useage
### Syntax
python .\Main.py -Path <path> -Algorithm <algorithm> -Compare <True/False>

### Arguments
-Path (--path)
  - The path to the file you want to hash the contents of.
  - For example, "-Path C:\Documents\example.txt"

-Algorithm (--algorithm)
  - The algorithm you wish to use for hashing. This will default to SHA-256 if not specified.
  - For example:
      - -Algorithm "SHA-256"
      - -Algorithm "MD5"
      - -Algorithm "SHA1"

-Compare (--compare)
  - Set this to True, Y, y, 1, or Yes to compare the generated hash value against the contents of hash.txt. Set it to False, N, n, 0, or No, or omit it to not compare with hash.txt.
  - For example, "-Compare True"

### Examples
Generate a hash value for the file example.txt, located on the C: drive, using the MD5 algorithm.
- python .\Main.py -Path C:\example.txt -Algorithm md5

Generate a hash value for the file example.txt, located in the working directory, using the SHA256 algorithm, and compare it to hash.txt.
- python .\Main.py -Path example.txt -Algorithm SHA256 -Compare True

Generate a hash value for the file example.txt, located in the working directory, using the SHA1 algorithm, and do not compare it to hash.txt.
- python .\Main.py -Path example.txt -Algorithm sha1 -Compare False

## Error Handling
If a specified path does not exist, the program will raise an error indicating the path does not exist.
If a specified algorithm is not in the hashlib library, the program will raise an error indicating it cannot find the algorithm in the hashlib library.
If an invalid input is given for the -Compare field, the program will raise an error indicating it does not recognize the input.
If the program cannot find hash.txt, it will raise a non-critical error indicating as such before creating a new hash.txt to use.

## File Storage
The program stores file hashes in hash.txt, with one exception. If the -Compare field is set to True, it will not, by default, store the file hash. It will, however, after comparison, ask if the user would like the file stored anyway.
The contents of hash.txt are expected to look something like the following; of course, your hash values will be different.
![image](https://github.com/user-attachments/assets/6cdd7100-0537-470e-90a4-ca8df0ac9dee)

## Acknowledgements/References
- https://docs.python.org/3/library/hashlib.html
- https://www.w3schools.com/python/python_lambda.asp
- https://docs.python.org/3/howto/argparse.html
- Chatgpt - Assisted with spell-checking and grammar-checking this README, as well as identifying bugs and potential errors. While the solution to said errors was developed without the assistance of generative AI, it proved very useful for testing outcomes in my code that I would not have thought to test.
