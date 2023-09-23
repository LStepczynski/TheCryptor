
# class TheCryptor:
#     def cipher(text, cipher_list):
#         binary_string = ''.join(format(ord(char), '08b') for char in text)
#         cipher, key = cipher_list
#         key = ''.join(format(ord(char), '08b') for char in key)
#         binary_string = cipher(binary_string, key)
#         ascii_characters = [chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)]
#         text_string = ''.join(ascii_characters)
#         return text_string

#     def get_key(binary_string, key):
#         if len(binary_string) == len(key):
#             return key
#         if len(binary_string) < len(key):
#             return key[:len(binary_string)]
#         if len(binary_string) > len(key):
#             length = len(binary_string) // len(key)
#             for _ in range(length):
#                 key += key
#             return key[:len(binary_string)]

#     def xor(binary_string, key):
#         binary_string = ''.join([number for number in binary_string if number != ' '])
#         key = TheCryptor.get_key(binary_string, key)
#         ciphered_sting = ''
#         for bin_num, key_num in zip(binary_string, key):
#             ciphered_sting += str(int(bin_num) ^ int(key_num))
#         return ciphered_sting
    
# print(TheCryptor.cipher('siemano', [TheCryptor.xor, 'test']))

class TheCryptor:
    @staticmethod
    def cipher(text, cipher_list):
        binary_string = ''.join(format(ord(char), '08b') for char in text)
        cipher, key = cipher_list
        key = ''.join(format(ord(char), '08b') for char in key)
        binary_string = cipher(binary_string, key)
        ascii_characters = [chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8)]
        text_string = ''.join(ascii_characters)
        return text_string
    
    @staticmethod
    def get_key(text, key):
        binary_string = ''.join(format(ord(char), '08b') for char in text)
        key_length = len(key)
        binary_length = len(binary_string)
        # Repeat the key enough times to match or exceed the binary_string length
        return (key * (binary_length // key_length + 1))[:binary_length]
    
    @staticmethod
    def xor(binary_string, key):
        key = TheCryptor.get_key(binary_string, key)
        ciphered_string = ''.join(str(int(bin_num) ^ int(key_num)) for bin_num, key_num in zip(binary_string, key))
        return ciphered_string


text = TheCryptor.cipher('siemano', [TheCryptor.xor, 'abc'])
print(text)
print(text == '♫♂♠♀♥')
print(TheCryptor.cipher(text, [TheCryptor.xor, 'abc']))