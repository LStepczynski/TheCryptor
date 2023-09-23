
class TheCryptor:
    def text_to_binary(text):
        binary_string = ''.join(format(ord(char), '08b') for char in text)
        return binary_string

    def binary_to_text(binary_string):
        binary_string = ''.join([number for number in binary_string if number != ' '])
        if len(binary_string) % 8 != 0:
            return "Error: The binary string must be a multiple of 8 bits."
        
        ascii_characters = [chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)]
        text_string = ''.join(ascii_characters)
        return text_string
