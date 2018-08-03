def morsecode_creator(word):
    """
        Converts a string into morse code.
        
        NOTE :
        This function does not recognize special characters (!,?>", etc...)
        Any special characters in the text will be displayed in parantheses.
    """
    code_list = []
    for char in word:
        if char.lower() == 'a':
            code_list.append('.-')
        elif char.lower() == 'b':
            code_list.append('-...')
        elif char.lower() == 'c':
            code_list.append('-.-.')
        elif char.lower() == 'd':
            code_list.append('-..')
        elif char.lower() == 'e':
            code_list.append('.')
        elif char.lower() == 'f':
            code_list.append('..-.')
        elif char.lower() == 'g':
            code_list.append('--.')
        elif char.lower() == 'h':
            code_list.append('....')
        elif char.lower() == 'i':
            code_list.append('..')
        elif char.lower() == 'j':
            code_list.append('.---')
        elif char.lower() == 'k':
            code_list.append('-.-')
        elif char.lower() == 'l':
            code_list.append('.-..')
        elif char.lower() == 'm':
            code_list.append('--')
        elif char.lower() == 'n':
            code_list.append('-.')
        elif char.lower() == 'o':
            code_list.append('---')
        elif char.lower() == 'p':
            code_list.append('.--.')
        elif char.lower() == 'q':
            code_list.append('--.-')
        elif char.lower() == 'r':
            code_list.append('.-.')
        elif char.lower() == 's':
            code_list.append('...')
        elif char.lower() == 't':
            code_list.append('-')
        elif char.lower() == 'u':
            code_list.append('..-')
        elif char.lower() == 'v':
            code_list.append('...-')
        elif char.lower() == 'w':
            code_list.append('.--')
        elif char.lower() == 'x':
            code_list.append('-..-')
        elif char.lower() == 'y':
            code_list.append('-.--')
        elif char.lower() == 'z':
            code_list.append('--..')
        elif char.lower() == ' ':
            code_list.append(' ')
        elif char == '0':
            code_list.append('-----')
        elif char == '1':
            code_list.append('.----')
        elif char == '2':
            code_list.append('..---')
        elif char == '3':
            code_list.append('...--')
        elif char == '4':
            code_list.append('....-')
        elif char == '5':
            code_list.append('.....')
        elif char == '6':
            code_list.append('-....')
        elif char == '7':
            code_list.append('--...')
        elif char == '8':
            code_list.append('---..')
        elif char == '9':
            code_list.append('----.')
        elif char == '\n' or '\r':
            continue
        else:
            code_list.append('( %s )' % char)
            
    return ' '.join(code_list)
    
print(morsecode_creator('hello, my name is joe smith and i am 100 years old'))
