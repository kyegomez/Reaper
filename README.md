[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

# Reaper
This is a Python script that implements a simple encryption and decryption algorithm. The script uses four different encryption methods: base64 encoding with 16, 32, 64, and 85 bits. The encryption method used is selected randomly. The script also includes a simple anti-debugging technique and a self-modifying code feature.

Architecture
-----------

The script consists of several functions:

* `random_char`: generates a random character from the ASCII letters.
* `encrypt`: takes a list of lines as input, encrypts each line using one of the four encryption methods, and returns the encrypted lines and the encryption method used.
* `write_lines`: writes the encrypted lines to a file.
* `decrypt`: takes the encrypted lines and the encryption method used, decrypts the lines, and executes the decrypted code.
* `main`: the main function that reads the script, encrypts the lines, writes the encrypted lines to a file, and decrypts the lines.

How it works
------------

1. The script starts by importing the necessary libraries: `os`, `base64`, `random`, `string`, `hashlib`, `struct`, `socket`.
2. The `random_char` function generates a random character from the ASCII letters.
3. The `encrypt` function takes a list of lines as input, encrypts each line using one of the four encryption methods, and returns the encrypted lines and the encryption method used.
4. The `write_lines` function writes the encrypted lines to a file.
5. The `decrypt` function takes the encrypted lines and the encryption method used, decrypts the lines, and executes the decrypted code.
6. The `main` function reads the script, encrypts the lines, writes the encrypted lines to a file, and decrypts the lines.

Usage
-----

To use the script, simply run it using the Python interpreter. The script will encrypt the lines and write them to a file. To decrypt the lines, run the script again with the encryption method used as an argument.

Encryption methods
-------------------

The script uses four different encryption methods: base64 encoding with 16, 32, 64, and 85 bits. The encryption method used is selected randomly.

License
-------

This script is licensed under the MIT License.