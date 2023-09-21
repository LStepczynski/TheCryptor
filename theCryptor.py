
class TheCryptor:
    def text_to_hex(text):
        hex_string = ''.join(format(ord(char), '02x') for char in text)
        return hex_string

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

    def binary_to_hex(binary_string):
        binary_string = ''.join([number for number in binary_string if number != ' '])
        binary_string = binary_string.zfill(len(binary_string) + (4 - len(binary_string) % 4) % 4)  # Pad with zeroes to make length multiple of 4
        hex_string = hex(int(binary_string, 2))[2:]
        return hex_string.upper()
    
    def hex_to_text(hex_string):
        hex_string = ''.join([number for number in hex_string if number != ' '])
        text_string = ''.join(chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2))
        return text_string

    def hex_to_binary(hex_string):
        hex_string = ''.join([number for number in hex_string if number != ' '])
        binary_string = ''.join(format(int(char, 16), '04b') for char in hex_string)
        return binary_string
