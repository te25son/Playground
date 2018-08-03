def morsecode_creator(word):
    """
        Converts a string into morse code.
        
        NOTE :
        This function does not recognize special characters (!,?>", etc...)
        Any special characters in the text will be displayed in parantheses.
    """
    code_list = []
    
    code_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
    }
    
    for char in string:
        char = char.lower()
        if char in code_dict:
            code_list.append(code_dict[char])
        elif char.lower() == ' ':
            code_list.append(' ')
        elif char == '\n' or char == '\r':
            continue
        else:
            code_list.append('( %s )' % char)
            
    return ' '.join(code_list)
    
print(morsecode_creator('hello, my name is joe smith and i am 100 years old'))

for char in 'abcdefghijklmnopqrstuvwxyz1234567890':
    print('{:<2} {:<5}'.format(char, morsecode_creator(char)))
