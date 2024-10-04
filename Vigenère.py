UID = 120278907
Lat_name = 'Panchal'
First_name = 'Bhavin' 


def caesar_str_enc(text1, shift):
   
    text1 = text1.upper()
    encrypted_text = ""
    for char in text1:
        if char == " ":
          continue
        elif char.isalpha():
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_str_dec(encrypted_text, shift):
   
    encrypted_text = encrypted_text.upper()
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text

def vigenere_enc(key, text2):
   
    key = key.upper()
    text2 = text2.upper()
    
    encrypted_text = ""
    key_index = 0
    for char in text2:
        if char == " ":
          continue
        elif char.isalpha():
            encrypted_text += chr((ord(char) - 65 + (ord(key[key_index % len(key)]) - 65)) % 26 + 65)
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_dec(key, encrypted_text):
    
    key = key.upper()
    encrypted_text = encrypted_text.upper()
    decrypted_text = ""
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            decrypted_text += chr((ord(char) - 65 - (ord(key[key_index % len(key)]) - 65)) % 26 + 65)
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

# Test cases
def test_func():
    print(caesar_str_enc('A TEST SENTENCE', 2))  # return 'CVGUVUGPVGPEG'
    print(caesar_str_dec('CVGUVUGPVGPEG', 2))    # return 'ATESTSENTENCE'
    print(vigenere_enc('KEY', 'Test String'))    # return 'DIQDWRBMLQ'
    print(vigenere_dec('KEY', 'DIQDWRBMLQ'))     # return 'TESTSTRING'

    return None
  
"""
  
  text1 = input("Enter the text for ceaser cipher: ")
  k = int(input("Enter the shift:"))
  text2 = input("Enter the text for vigenere cipher: ")
  key = input("Enter the key:")
  

  #ceaser cipher:
  ceaser_encrypted_text = caesar_str_enc(text1, k)
  print(ceaser_encrypted_text)
  ceaser_decrypted_text = caesar_str_dec(ceaser_encrypted_text,k)
  print(ceaser_decrypted_text)

  #vigenere cipher:
  vigenere_encrypted_text = vigenere_enc(key, text2)
  print(vigenere_encrypted_text)
  vigenere_decrypted_text = vigenere_dec(key,vigenere_encrypted_text)
  print(vigenere_decrypted_text)
  
"""


if __name__ == "__main__":
  
 test_func()
 
 
 
 

 

