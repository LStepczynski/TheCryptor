from unidecode import unidecode

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
    def text_to_binary(text, key=None):
        binary_string = ''.join(format(ord(char), '08b') for char in text)
        return binary_string
    
    @staticmethod
    def binary_to_text(binary_string, key=None):
        binary_string = ''.join([number for number in binary_string if number != ' '])
        ascii_characters = [chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8)]
        text_string = ''.join(ascii_characters)
        return text_string

    @staticmethod
    def get_key(binary_string, key):
        key = ''.join(format(ord(char), '08b') for char in key)
        key_length = len(key)
        binary_length = len(binary_string)
        # Repeat the key enough times to match or exceed the binary_string length
        return (key * (binary_length // key_length + 1))[:binary_length]

    @staticmethod
    def xor(binary_string, key):
        """Cipher that accepts binary code and performs the xor operation. Example: text=1001, key=0111, output=1110"""
        def find_spaces(binary_string):
            """Finds the indexes of spaces in the binary code and returns them"""
            space_binary = '00100000'  # Binary representation for space
            space_indexes = []
            index = binary_string.find(space_binary)  # Find the first occurrence of space
            
            while index != -1:  # -1 means no more spaces are found
                space_indexes.append(index)
                index = binary_string.find(space_binary, index + 1)  # Find the next occurrence of space, if any, starting from the index after the last found space
            
            return space_indexes
        
        space_indexes = find_spaces(binary_string) #Indexes of spaces in a list

        #Removes all the spaces from the binary string before ciphering
        binary_string = binary_string.replace('00100000', '')

        #Ciphers the binary code
        key = TheCryptor.get_key(binary_string, key)
        ciphered_string = ''.join(str(int(bin_num) ^ int(key_num)) for bin_num, key_num in zip(binary_string, key))

        #Puts the spaces back to their original place 
        for space in space_indexes:
            print(space)
            ciphered_string = list(ciphered_string)
            ciphered_string = ''.join(ciphered_string[:space] + list('00100000') + ciphered_string[space:])
        return ciphered_string

    @staticmethod
    def xand(binary_string, key):
        key = TheCryptor.get_key(binary_string, key)
        ciphered_string = ''.join(str(int(not(int(bin_num) ^ int(key_num)))) for bin_num, key_num in zip(binary_string, key))
        return ciphered_string

