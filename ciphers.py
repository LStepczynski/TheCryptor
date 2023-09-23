
class Cipher:
    def xor(binary_string, key):
        binary_string = ''.join([number for number in binary_string if number != ' '])
        key = Cipher.get_key(binary_string, key)
        ciphered_sting = ''
        for bin_num, key_num in zip(binary_string, key):
            ciphered_sting += str(int(bin_num) ^ int(key_num))
        return ciphered_sting
        

    def get_key(binary_string, key):
        if len(binary_string) == len(key):
            return key
        if len(binary_string) < len(key):
            return key[:len(binary_string)]
        if len(binary_string) > len(key):
            length = len(binary_string) // len(key)
            for _ in range(length):
                key += key
            return key[:len(binary_string)]
        
