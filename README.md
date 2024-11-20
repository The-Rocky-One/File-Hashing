# File-Hashing and Comparison
Author: Stone Provo, 000854122.
This project provides a Command Line Interface (CLI) tool to generate and compare the hash values of files using various hashing algorithms. It includes the functionality to store said hash values into a file, and reference that file for comparison.

## Features
<b>- Generate File Hash Values:</b> The program generates a hash value for a specified file using one of various hashing algorithms. (Default: SHA-256)
<b>- Storing File Hash Values:</b> Using a text file (hash.txt), the program is capable of storing and referencing old hash values.
<b>- Compare File Hash Values:</b> The program can compare a fresh file hash to those inside hash.txt, looking through the entire contents of the file for a match.
<b>- Supports Multiple Algorithms</b> It supports all hashing algorithms in the hashlib library.

## Installation
### Pre-Requisites
- Python 3.x
- The following imports, all of which are apart of Python's standard library
  - argparse
  - os
  - hashlib
