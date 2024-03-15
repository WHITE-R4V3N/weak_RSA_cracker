# Description
This is a program that is capable of cracking weak RSA encryption. Now of days RSA encryptions are getting longer and longer and using bigger and bigger values for N. This in turn makes it harder to crack the RSA algorithm.

NOTE: This may get things wrong and is not 100%. It has trouble when the text includes numbers.

# What is RSA?
RSA is an algorithm used to encrypt and decrypt data using a public key and private key.

These public and private keys come in a pair. A public key can encrypt data that can be sent to a user with the coresponding private key. The user with the private key is the only one that can decrypt the data and view it.

This algorithm has some steps to create these private and public keys. They are as follows:
```
1. Select two prime numbers, p and q (The bigger the more secure)
2. Calculate n. n = p * q
3. Calculate phi(n). phi(n) = (p - 1) * (q - 1)
4. Choose a value for e such that 1 < e < phi(n) and gcd(phi(n), e) = 1 (gcd means gratest common denominator)
5. Calculate d. d = (e^-1) mod phi(n)
```

Now we have the algorithm in plain text. We can use this to get the public key {e, n} and the private key {d, n}.

# Public key to Private key
There are a few steps we need to follow to turn the public key into the private key so that we can decrypt messages sent to the user using this public and private key pair.

```
1. Get the public key (e, n)
2. Find the prime factors that multiply to n.
3. Calculate phi(n). phi(n) = (p - 1) * (q - 1)
4. Calculate d. d = (e^-1) mod phi(n)
5. Decrypt the data.
```

This script will do exactly that. It uses the private key and turns it into the users private key and allows us to decrypt the encrypted messages.