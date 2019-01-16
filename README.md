## BIP39_mnemonic_creation_light_python
Simple python and javascript programs for generating valid BIP39 mnemonics, including reversible 'palindromic' mnemonics (i.e. recovery phrases) that are BIP-39 compliant in terms of security, wordlist, and checksum, and that can be used offline as standalone applications (internet-less) without the need of an internet connection or third-party libraries, as all code is contained inline within the singular file (either python file or html file).


Description: 
Simplified Python and Javascript programs for generating
valid bip39 mnemonics, using an initial random entropy via the
secrets module in Python for cryptographically secure entropy (for the Python-related .py files), and the Web3 Cryptography API 
(for the Javascript-based .html files) then revealing the entropy in its various formats including hex, as a binary string, and as a bytearray before hashing with the SHA256 algorithm to obtain the leading required
number of bits from the hash digest in order to compute the
checksum and complete the final groups of words shown as 11 bit strings
that correspond to an index value for a word as per the BIP39 specification. 

The resulting words can be used as valid BIP39 mnemonic recovery phrases for related compatible
crypto wallets, and because these apps are early stage and under experimental development, they should be checked against more established tools, in order to confirm that a given entropy maps correctly to its resulting mnemonic words. 

The general formula followed in the creation of BIP39-compliant mnemonics is as follows: 
Initial Entropy in bits /32 = checksum length in bits  (this is equal to wordcount/3 == checksum length)
initial entropy mod 11 = remaining bits + checksum = last word
Initial entropy + checksum = total bits /11 = total words. (total words can be either 12 or 24, depending on initial entropy length)


Example usage: 128 bits entropy, will require a 4 bit checksum,
for a total of 132 bits, that will result in 12 final words. A user can choose for the tool to create the 128 bits randomly - by selecting 12 - then hitting enter on the following screen, or enter the 128 bits manually in the form of a hexidecimal string (i.e. a 32 character hex string, left-padded with 0x making it 34 characters total). In all cases the tool always computes the required checksum which is determinisitc and derived from the initial entropy, therefore, for user-supplied entropy the checksum should not be included as it will be automatically computed by the tool and appended to the end of the string before the final word group is derived.

Note: The palindromic 'reversible' mnemonics are simply regular BIP39-compliant ones that happen to also have the ability to reverse the order of their words and still be BIP39-compliant, this is only possible for certain mnemonics that meet specific criteria, and the author does not believe that there is any security loss for these reversible ones, as one would still need to brute-force the range of valid mnemonics in order to find ones that are also reversible.  







