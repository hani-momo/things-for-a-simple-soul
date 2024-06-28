
def latin_to_morse(line):
    morse_line = []
    morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 
        'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 
        'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 
        'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
        'y': '-.--', 'z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.'
    }

    morse_line = ['/'.join(morse_dict[char] for char in line.lower() if char in morse_dict)]
    # latin_ls = list(line.lower())
    # for char in latin_ls:
    #    if char in morse_dict:
    #        morse_line.append(morse_dict[char])
    #        morse_line.append('/')
    #    elif char == ' ':
    #        morse_line.append('/')
    #    else:
    #        morse_line.append(' ')
    return ' '.join(morse_line)


print('\nReady to translate! \np.s. To exit enter \'EXIT PROGRAMM\'')
while True:
    latin_line = input('\n\t')

    if latin_line.upper() == 'EXIT PROGRAMM':
        print('\tSee you next time!')
        break

    morse_line = latin_to_morse(latin_line)
    print('\t' + morse_line, '\n')
    print('\n' + '/'*9, '\n')
