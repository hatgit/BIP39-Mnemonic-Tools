bip39 Valid Mnemonic Generator Python App
'''
Author: Steven Hatzakis © 2018

Version 1.6 beta
Description: A simplified python program for generating
valid bip39 mnemonics, using an initial random entropy via the
secrets module in Python for cryptographically secure entropy,
then revealing the entropy in its various formats including hex,
and as a bytearray before hashing to obtain the leading required
number of bits from the hash digest in order to compute the
checksum and complete the final word group.

Formula: Initial Entropy in bits /32 = checksum length in bits
initial entropy mod 11 = remaining bits + checksum = last word
Initial entropy + checksum = total bits /11 = total words. 

Example usage: 128 bits entropy, will require a 4 bit checksum,
for a total of 132 bits.

Notes: while this code could be re-written to further condense/clean it,
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

'''


import hashlib
import secrets
import binascii


ent_dec=format(secrets.randbits(130),'0129b') #*get a minimum of x bits
ent_dec=ent_dec[:128] #*use only bits required from the initial random number
print('Initial Ent:',ent_dec) #print the entire string of bits to be used 
print('Length of Initial Ent:',len(ent_dec)) #print the length of the string
ent_decpad=str('0b')+str(ent_dec) #*append  0b pad so the number is treated as binary and not base 10
print('Initial Ent as hex:',hex(int(ent_dec,2))) #print initial string as hexidecimal base 16
print('Length of Ent as hex:',len((hex(int(ent_dec,2))))) #print length of hex string

ent_hex=(hex(int(ent_dec,2))) #assign hex string to ent_hex variable

ent_hex_nopad=ent_hex[2:]#removing leading 0x hex pad

print('Ent length as hex w/ no 0x pad:',len(ent_hex_nopad)) #prints length without 0x pad
print('Initial Ent as hex w/ no pad:',hex(int(ent_dec,2))[2:])# print string without 0x pad

array=bytearray.fromhex(ent_hex_nopad) #*convert no padded hex string to bytearray
print(array,'<--- Entropy as Bytes') #print array as bytes in bytearray()
print('Length of Initial Ent as bytearray:',len(array)) #print length of bytearray

bits=hashlib.sha256(array).hexdigest() #*compute the sha256 hash of the bytearray as a hex digest

print(bits,'<--- SHA256 Hash digest of entropy bytes') #print the hash digest of the bytearray
bit=bits[0:1] #*take first x bit of bits (x is not defined but be added to slice manually) 

print(bit,'<--- partial fragment of initial "byte"of hash') #print first part of hash used for bits
print((bit[0:1]),'<--- First n bits of hash to convert to hex') #print needed bits from 

