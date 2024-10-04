from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Global variables
UID = 120278907
Last_Name = 'Panchal'
First_Name = 'Bhavin'

# Function for RSA key pair generation
def generate_rsa_keypair():
    key = RSA.generate(2048)
    return key

# Function for RSA encryption using public key
def rsa_enc_public(plaintext, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# Function for RSA decryption using private key
def rsa_dec_private(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Test cases
if __name__ == "__main__":
    keypair = generate_rsa_keypair()
    public_key = keypair.publickey()
    private_key = keypair

    # Encrypt a message using the public key
    message = b"This is testing message"
    encrypted_message = rsa_enc_public(message, public_key)
    encrypted_message_base64 = base64.b64encode(encrypted_message)
    print("Encrypted message:", encrypted_message_base64.decode())

    # Decrypt the message using the private key
    decrypted_message = rsa_dec_private(encrypted_message, private_key)
    print("Decrypted message:", decrypted_message.decode())
