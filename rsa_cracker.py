# Author:       WHITE-R4V3N
# Date:         2024/03/08
# Description:  A program written in python 3 that demonstates how weak RSA can be cracked and decoded. This is to
#               show the limitations of RSA encryption.

#### IMPORTS ####

import re
import string

from collections import OrderedDict

#### CODE ####

def prime_numbers(n): # Gets all the prime factors that multiply up to n
    i = 2
    factors = [] # Where it will store the factors into

    while i * i <= n: # Loops until it reaches n
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i) # append the factor found

    if n > 1:
        factors.append(n)
    
    return factors # returns all prime factors found that could be used to break the RSA encryption

# The public key for the RSA looks as such: (e, n). Using the public key we can crack the private key.
# This would allow us to intercept traffic being sent to the user and decrypt it for ourselves.

# Example public key: (3, 3127)
#                     (e,  n  )

n = 3127
e = 3
cipher = str(113515182658265811321498451167914982025271645115181498635115314981016257612751742375399)

factors = prime_numbers(n) # Find the two prime factors of n

## Find d and phi n ##
phi_n = (factors[0] - 1) * (factors[1] - 1)

j = 0
while True:
    if (j * e) % phi_n == 1:
        d = j
        break # Exit once private key is found (d, n)
    j += 1

## Create the ASCII Cipher Table ##
cipher_alphabet = {}

for ch in list(string.printable):
    ct = (ord(ch) ** e) % n # Encrypt all printable characters

    cipher_alphabet[ct] = ch # Save as encrypted, ascii pair in dictionary

## Convert cipher to ASCII ##
found_letter = []
found_dict = {}
message = ''

for key in cipher_alphabet:
    found_letter += list(re.finditer(str(key), cipher)) # Find all instances of the letter

for letter in found_letter:
    pos = str(letter.span()).replace('(', '').replace(')', '').replace(',', '').split(' ') # Take out only the span
    text = letter.group() # Take the part of cipher found.
    #print(f'Letter: {cipher_alphabet[int(cipher[int(pos[0]):int(pos[1])])]} | Cipher: {text:4} | Position: {pos}')
    found_dict[int(pos[0])] = cipher_alphabet[int(cipher[int(pos[0]):int(pos[1])])] # Creates a dictionary of starting pos: 'cipher'

sorted_dict = dict(sorted(found_dict.items())) # Sort the dictionary

# Print the sorted dictionary as a string
for l in sorted_dict:
    message += sorted_dict[l]
print(f'Possible String:\n{message}')

# This will try its best to crack all of the cipher. It will make errors.