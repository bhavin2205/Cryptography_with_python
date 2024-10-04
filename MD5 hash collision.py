from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import io
import itertools

UID = 120278907
First_Name = "Bhavin"
Last_Name = "Panchal"


# Location of the #'s in the below block. Remember the last location is ignored in lists so this will include 54,55 : print(key_with_error[54:56])
key_with_error = '''-----BEGIN DSA PRIVATE KEY-----
MIIBuQIBAAKBgQC973oUk7##7lilY1gwPAtXvTNDWbPbQhlstbax0b6LMyPCE1xf
gwLoercCPm1OWl65pRExUR5g0CJxFZNekWQKh7fNqzMQt5fUKMMwtU4Im05M+sTb
FeVYTiUrEdWjAbF5XvN6RgcEp7rL1ZX4VucElbxoAIvek+Aqfr0Zg/ltBQIVAKoK
+9q7j+T3esxgCTQMI2BQKSQnAn8dphjfU5jwzf+Nst9rkn1tZO0afBuzvNMRS8BF
9LCJ2q2Nly9Orifz8IJqkhIGnEy802QyjUgLJAgYlBWarK1vJTQApgwN3t66mE9J
Oc3gBgi9skZ/AQimaMb8YiHskbhn85ISpgJcvkjnL2KiTA/FtwTbzAj/Z5Sqv0xK
ax2GAoGBAJpAieRPdSlKrM7x5gVlPZiI5vXEdw83IBIsK0W5XTtD5LeDfemLQDO9
Qz49svcBuH6pdINnvQ3CrxaiJyJTMnfNNK9NuBeW2Q4KZJxQflXhcNuXcG0i2m0l
QizOAkzQKKHeIMk5+7KoD3tgm4xzJvPewhaSca6upI3xVUobnjs/AhR7SchExgXv
cJMj8CVGbPRdKkKBUg==
-----END DSA PRIVATE KEY-----
'''

# NOTE: No modifications required for this function. This will verify if your key is correct.
# This will return True if the key is correct and False if it is incorrect. Use it as it is in your bruteforce function.
def verify(key):
    try:
        possible_key = DSA.import_key(io.StringIO(key).getvalue())
        print("The key is correct:")
        print(key)
        return True
    except ValueError:
        return False

def bruteforce(key_with_error):
    # Convert the key_with_error string to a list
    key_list = list(key_with_error)

    # Generate all possible combinations of characters for positions 54 and 55
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    combinations = itertools.product(characters, repeat=2)

    # Try each combination and verify the modified key
    for combination in combinations:
        key_list[54:56] = combination
        modified_key = ''.join(key_list)
        if verify(modified_key):
            return modified_key

    return None

# Calling the bruteforce function
new_key = bruteforce(key_with_error)
if new_key:
    print("two character of valid key are:", new_key[54],new_key[56])
    print("The correct key is:\n", new_key)
    
else:
    print("No valid key found.")





#PART-2 

import hashlib
import os

plain1 = b'\xd1\x31\xdd\x02\xc5\xe6\xee\xc4\x69\x3d\x9a\x06\x98\xaf\xf9\x5c\x2f\xca\xb5\x87\x12\x46\x7e\xab\x40\x04\x58\x3e\xb8\xfb\x7f\x89\x55\xad\x34\x06\x09\xf4\xb3\x02\x83\xe4\x88\x83\x25\x71\x41\x5a\x08\x51\x25\xe8\xf7\xcd\xc9\x9f\xd9\x1d\xbd\xf2\x80\x37\x3c\x5b\xd8\x82\x3e\x31\x56\x34\x8f\x5b\xae\x6d\xac\xd4\x36\xc9\x19\xc6\xdd\x53\xe2\xb4\x87\xda\x03\xfd\x02\x39\x63\x06\xd2\x48\xcd\xa0\xe9\x9f\x33\x42\x0f\x57\x7e\xe8\xce\x54\xb6\x70\x80\xa8\x0d\x1e\xc6\x98\x21\xbc\xb6\xa8\x83\x93\x96\xf9\x65\x2b\x6f\xf7\x2a\x70'

# Incorrect inputblock
plain2 = b'\xd1\x31\xdd\x02\xc5\xe6\xee\xc4\x69\x3d\x9a\x06\x98\xaf\xf9\x5c\x2f\xca\xb5\x00\x12\x46\x7e\xab\x40\x04\x58\x3e\xb8\xfb\x7f\x89\x55\xad\x34\x06\x09\xf4\xb3\x02\x83\xe4\x88\x83\x25\x00\x41\x5a\x08\x51\x25\xe8\xf7\xcd\xc9\x9f\xd9\x1d\xbd\x72\x80\x37\x3c\x5b\xd8\x82\x3e\x31\x56\x34\x8f\x5b\xae\x6d\xac\xd4\x36\xc9\x19\xc6\xdd\x53\xe2\x34\x87\xda\x03\xfd\x02\x39\x63\x06\xd2\x48\xcd\xa0\xe9\x9f\x33\x42\x0f\x57\x7e\xe8\xce\x54\xb6\x70\x80\x28\x0d\x1e\xc6\x98\x21\xbc\xb6\xa8\x83\x93\x96\xf9\x65\xab\x6f\xf7\x2a\x70'

# Returns true if hashes match
def verify_hash(temp):
    return (hashlib.md5(plain1).digest() == hashlib.md5(temp).digest() and plain1 != temp)

def hash_collision(plain2):
    # Convert the plain2 bytestring to a list
    plain2_list = list(plain2)

    # Generate all possible combinations of bytes for indices 19, 45, and 59
    characters = bytes(range(256))

    # Try each combination and verify the modified hash
    for byte1 in characters:
        for byte2 in characters:
            for byte3 in characters:
                plain2_list[19], plain2_list[45], plain2_list[59] = byte1, byte2, byte3
                modified_plain2 = bytes(plain2_list)
                if verify_hash(modified_plain2):
                    return modified_plain2

    return None

result = hash_collision(plain2)
if result:
    print("Hash collision found:")
    print(result)
else:
    print("No hash collision found.")