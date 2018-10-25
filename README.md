## BIP39_mnemonic_creation_light_python
A simple python program for generating valid BIP39 mnemonics



#Description: 
A simplified python program for generating
valid bip39 mnemonics, using an initial random entropy via the
secrets module in Python for cryptographically secure entropy,
then revealing the entropy in its various formats including hex,
and as a bytearray before hashing to obtain the leading required
number of bits from the hash digest in order to compute the
checksum and complete the final groups of words shows as 11 bit strings
that correspond to an index value for a word as per the bip39 spec.

#Formula: 
Initial Entropy in bits /32 = checksum length in bits
initial entropy mod 11 = remaining bits + checksum = last word
Initial entropy + checksum = total bits /11 = total words. 
Example usage: 128 bits entropy, will require a 4 bit checksum,
for a total of 132 bits.

#Notes: 
While this code could be re-written to further condense/clean it,
my goal was initially just to get it to work. For example, starting with the
secret.randbits() function, I noticed often the value returned was less
than the range specified even using rangebelow(), so I went a few bits higher in length
to help assure that I got at least 129 bits (or 130) and then from there
slice at least 128 bits to obtain the desired starting amount of entorpy neeeded.
In addition,there is a bytearray error that sometimes throws if their is an odd number
of bytes in the array, which was related to scenarios where 129 bits was used instead of 128
for example. That error should now be resolved  - and namely - after formatting
the initial entropy decimal number as a string then appending 0b to ensure it is treated
as a binary value prior to conversion in subsequent steps.
