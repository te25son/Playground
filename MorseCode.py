"""
A program that converts English text to morse code 
and morse code back into English text.
"""

CODE_DICT = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': ' ', '\n': '\n', '\r': '\r'
}


def get_letter(string):
    """
    Returns a letter for the given string of morse code
    """
    for key, value in CODE_DICT.items():
        if string == value:
            return key
        

def morsecode_creator(word):
    """
        Converts a string into morse code.
        
        NOTE :
        This function does not recognize special characters (!,?>", etc...)
        Any special characters in the text will be displayed in parantheses.
    """
    code_list = []
    
    for char in string:
        char = char.lower()
        if char in CODE_DICT:
            code_list.append(CODE_DICT[char])
        else:
            code_list.append('#')
            
    return ' '.join(code_list)
    

def morse_to_english(string):
    """
    Takes a string of morse code and returns the code
    translated in English

    NOTE:
        - Spaces wished to be displayed in the final sentence must be forward slashes (/)
        - Normal spaces that do not want to be displayed must be between each letter
        - Any other special characters will be returned without change
    """
    string_list = string.split()
    sentence = []

    for letter in string_list:
        if letter in CODE_DICT.values():
            sentence.append(get_letter(letter))
        else:
            sentence.append(letter)

    return ''.join(sentence)
