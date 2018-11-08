## BIP39_mnemonic_creation_light_python
A simple python program for generating valid BIP39 mnemonics


Description: 
A simplified python program for generating
valid bip39 mnemonics, using an initial random entropy via the
secrets module in Python for cryptographically secure entropy,
then revealing the entropy in its various formats including hex,
and as a bytearray before hashing to obtain the leading required
number of bits from the hash digest in order to compute the
checksum and complete the final groups of words shown as 11 bit strings
that correspond to an index value for a word as per the bip39 spec. 
The resulting words can be used as valid BIP39 mnemonic recovery phrases for related compatible
crypto wallets. 

Formula: 
Initial Entropy in bits /32 = checksum length in bits  (this is equal to wordcount/3 == checksum lenght)
initial entropy mod 11 = remaining bits + checksum = last word
Initial entropy + checksum = total bits /11 = total words. (total words can be either 12 or 24, depending on initial entropy length)


Example usage: 128 bits entropy, will require a 4 bit checksum,
for a total of 132 bits, that will result in 12 final words. A user can choose for the tool to create the 128 bits randomly - by selecting 12 - then hitting enter on the following screen, or enter the 128 bits manually in the form of a hexidecimal string (i.e. a 32 character hex string, left-padded with 0x making it 34 characters total). In all cases the tool always computes the required checksum which is determinisitc and derived from the initial entropy, therefore, for user-supplied entropy the checksum should not be included as it will be automatically computed by the tool and appended to the end of the string before the final word group is derived.







