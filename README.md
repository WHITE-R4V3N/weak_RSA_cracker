# Description
This is a program that is capable of cracking weak RSA encryption. Now of days RSA encryptions are getting longer and longer and using bigger and bigger values for N. This in turn makes it harder to crack the RSA algorithm.

NOTE: This may ge things wrong and is not 100%. It has trouble when the text includes numbers.

# What is RSA?
RSA is an algorithm used to encrypt and decrypt data using a public key and private key.

The Public key is used to encrypt data and send it to the user with the private key. This means that if someone intercepts the traffic they will not be able to read it unless they have the users private key.

The Private key is used to decrypt the data being sent. It allows the user to read what data has been sent to them using their public key.

NOTE: A weak RSA means a small n value which means we can easily find the prime numbers used and crack the users private key using only their public key.
