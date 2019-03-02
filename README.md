## BIP39 Mnemonic Tools

Simple Python and Javascript-based programs for generating valid BIP39 mnemonics, including reversible 'palindromic' mnemonics (i.e. recovery phrases) that are BIP-39 compliant in terms of security, wordlist, and checksum, and that can be used offline as standalone applications (internet-less) without the need of an internet connection or third-party libraries, as all code is contained inline within the singular file (either python file or html file). 

This repository currently contains three separate tools, which consist of two Python (.py) files and one Javascript-based app that is wrapped in an .html file, each of which works on a standalone basis independently either from the command-line or within an application (browser or compiler): 

 <blockquote>
<pre><code>[bip39appv1_8.py] <a href="https://github.com/hatgit/BIP39-Mnemonic-Tools/blob/master/bip39appv1_8.py">https://github.com/hatgit/BIP39-Mnemonic-Tools/blob/master/bip39appv1_8.py</a>
</code></pre>
</blockquote>

<blockquote>
<pre><code>[Palindromic_Mnemonic_Tool.py] <a href="https://github.com/hatgit/BIP39-Mnemonic-Tools/blob/master/Palindromic_Mnemonic_Tool.py">https://github.com/hatgit/BIP39-Mnemonic-Tools/blob/master/Palindromic_Mnemonic_Tool.py</a>
</code></pre>
</blockquote>

<blockquote>
<pre><code> [Palindromic-Mnemonic-Tool.html] <a href="https://github.com/hatgit/BIP39-Mnemonic-Tools/blob/master/Palindromic-Mnemonic-Tool.html">https://github.com/hatgit/BIP39-Mnemonic-Tools/blob/master/Palindromic-Mnemonic-Tool.html</a>
</code></pre>
</blockquote>


**Description**: 
Simplified Python and Javascript programs for generating
valid bip39 mnemonics, using an initial random entropy via the
secrets module in Python for cryptographically secure entropy (for the Python-related .py files), and the Web3 Cryptography API (for the Javascript-based .html files) then revealing the entropy in its various formats including hex, as a binary string, and as a bytearray before hashing with the SHA256 algorithm to obtain the leading required
number of bits from the hash digest in order to compute the
checksum and complete the final groups of words shown as 11 bit strings
that correspond to an index value for a word as per the BIP39 specification. 

The resulting words can be used as valid BIP39 mnemonic recovery phrases for related compatible
crypto wallets, and because these apps are early stage and under experimental development, they should be checked against more established tools, in order to confirm that a given entropy maps correctly to its resulting mnemonic words. 

The general formula followed in the creation of BIP39-compliant mnemonics is as follows: 
Initial Entropy in bits /32 = checksum length in bits  (this is equal to wordcount/3 == checksum length)
initial entropy mod 11 = remaining bits + checksum = last word
Initial entropy + checksum = total bits /11 = total words. (total words can be either 12 or 24, depending on initial entropy length)

|                |12-word mnemonic               |24-word mnemonic             |
|----------------|-------------------------------|-----------------------------|
|Initial Entropy |`128 bits`                     |`256 bits`                   |
|Checksum        |`4 bits`                       |`8 bits`                     |
|Total Bits      |`132 bits`                     |`264 bits`                   |
|Total Words     |`132/11 = 12 words`            |`264/11 = 24 words`          |
|----------------|-------------------------------|-----------------------------|



**Example usage**: 
128 bits entropy, will require a 4 bit checksum,for a total of 132 bits, that will result in 12 final words. A user can choose for the tool to create the 128 bits randomly - by selecting 12 - then hitting enter on the following screen, or enter the 128 bits manually in the form of a hexidecimal string (i.e. a 32 character hex string, left-padded with 0x making it 34 characters total). In all cases the tool always computes the required checksum which is determinisitc and derived from the initial entropy, therefore, for user-supplied entropy the checksum should not be included as it will be automatically computed by the tool and appended to the end of the string before the final word group is derived.

<img width="847" alt="BIP39 HTML Tool" src="https://user-images.githubusercontent.com/5213035/53685230-e34a8580-3ce5-11e9-8715-ae7c21f63c1e.png">

Note: The palindromic 'reversible' mnemonics are simply regular BIP39-compliant ones that happen to also have the ability to reverse the order of their words and still be BIP39-compliant, this is only possible for certain mnemonics that meet specific criteria, and the author does not believe that there is any security loss for these reversible ones, as one would still need to brute-force the range of valid mnemonics in order to find ones that are also reversible.  

<img width="1027" alt="BIP39 HTML Tool Palindromic Mnemonic Phase" src="https://user-images.githubusercontent.com/5213035/53685387-cdd65b00-3ce7-11e9-8e78-4225c89d72c5.png">

**IMPORTANT**: The above entropy values shown in the above example should never be used with any real funds even when testing.





