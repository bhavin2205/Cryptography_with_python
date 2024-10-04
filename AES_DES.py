UID = 120278907
Lat_Name = 'Panchal'
First_Name = 'Bhavin'
from Crypto.Cipher import AES, DES

def des_input_av_test(plaintext, key, bit_positions):
    def count_different_bits(str1, str2):
        return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(str1, str2))

    def flip_bit(data, position):
        byte_pos = position // 8
        bit_pos = 7 - (position % 8)
        data_list = bytearray(data)
        data_list[byte_pos] ^= (1 << bit_pos)
        return bytes(data_list)

    cipher = DES.new(key, DES.MODE_ECB)
    return [
        count_different_bits(cipher.encrypt(flip_bit(plaintext, pos)),
                             cipher.encrypt(plaintext))
        for pos in bit_positions
    ]

def des_key_av_test(plaintext, key, bit_positions):
    def count_different_bits(str1, str2):
        return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(str1, str2))

    def flip_bit(data, position):
        byte_pos = position // 8
        bit_pos = 7 - (position % 8)
        data_list = bytearray(data)
        data_list[byte_pos] ^= (1 << bit_pos)
        return bytes(data_list)

    ciphertexts = []
    for pos in bit_positions:
        modified_key = flip_bit(key, pos)
        cipher = DES.new(modified_key, DES.MODE_ECB)
        ciphertexts.append(count_different_bits(cipher.encrypt(plaintext),
                                                DES.new(key, DES.MODE_ECB).encrypt(plaintext)))
    return ciphertexts

def aes_input_av_test(plaintext, key, bit_positions):
    def count_different_bits(str1, str2):
        return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(str1, str2))

    def flip_bit(data, position):
        byte_pos = position // 8
        bit_pos = 7 - (position % 8)
        data_list = bytearray(data)
        data_list[byte_pos] ^= (1 << bit_pos)
        return bytes(data_list)

    cipher = AES.new(key, AES.MODE_ECB)
    return [
        count_different_bits(cipher.encrypt(flip_bit(plaintext, pos)),
                             cipher.encrypt(plaintext))
        for pos in bit_positions
    ]

def aes_key_av_test(plaintext, key, bit_positions):
    def count_different_bits(str1, str2):
        return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(str1, str2))

    def flip_bit(data, position):
        byte_pos = position // 8
        bit_pos = 7 - (position % 8)
        data_list = bytearray(data)
        data_list[byte_pos] ^= (1 << bit_pos)
        return bytes(data_list)

    ciphertexts = []
    for pos in bit_positions:
        modified_key = flip_bit(key, pos)
        cipher = AES.new(modified_key, AES.MODE_ECB)
        ciphertexts.append(count_different_bits(cipher.encrypt(plaintext),
                                                AES.new(key, AES.MODE_ECB).encrypt(plaintext)))
    return ciphertexts

if __name__ == "__main__":
    # Test des_input_av_test
    plaintext_des = b'thisoneis16bytes'
    key_des = b'deskey!!'
    bit_positions_des = [3, 25, 36]
    print("DES Input AV Test:", des_input_av_test(plaintext_des, key_des, bit_positions_des))  # Output should be [27, 35, 28]

    # Test des_key_av_test
    plaintext_des = b'thisoneis16bytes'
    key_des = b'deskey!!'
    bit_positions_des = [3, 25, 36]
    print("DES Key AV Test:", des_key_av_test(plaintext_des, key_des, bit_positions_des))  # Output should be [56, 68, 64]

    # Test aes_input_av_test
    plaintext_aes = b'thisoneis16bytes'
    key_aes = b'veryverylongkey!'
    bit_positions_aes = [5, 29, 38]
    print("AES Input AV Test:", aes_input_av_test(plaintext_aes, key_aes, bit_positions_aes))  # Output should be [65, 67, 68]

    # Test aes_key_av_test
    plaintext_aes = b'thisoneis16bytes'
    key_aes = b'veryverylongkey!'
    bit_positions_aes = [5, 29, 38]
    print("AES Key AV Test:", aes_key_av_test(plaintext_aes, key_aes, bit_positions_aes))  # Output should be [61, 65, 65]
