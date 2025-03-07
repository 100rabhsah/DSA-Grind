#Program for Morse Code Translator (Conversion of Morse Code to English Text)

def morse_to_text(morse_code):
    morse_code_dict = {".-": 'A', "-...": 'B', "-.-.": 'C', "-..": 'D', ".": 'E', "..-.": 'F',
                       "--.": 'G', "....": 'H', "..": 'I', ".---": 'J', "-.-": 'K', ".-..": 'L',
                       "--": 'M', "-.": 'N', "---": 'O', ".--.": 'P', "--.-": 'Q', ".-.": 'R',
                       "...": 'S', "-": 'T', "..-": 'U', "...-": 'V', ".--": 'W', "-..-": 'X',
                       "-.--": 'Y', "--..": 'Z',
                       "-----": '0', ".----": '1', "..---": '2', "...--": '3', "....-": '4',
                       ".....": '5', "-....": '6', "--...": '7', "---..": '8', "----.": '9',
                       "/": ' '}

    words = morse_code.split('/')  # Words are separated by three spaces
    translated_text = ''

    for word in words:
        letters = word.split(' ')
        for letter in letters:
            # Default to empty string if not found
            translated_text += morse_code_dict.get(letter, '')
        translated_text += ' '  # Add space between words

    return translated_text.strip()  # Remove trailing space


# Example usage:
morse_code_input = "-- --- .-. ... . / -.-. --- -.. . / .. ... / ..-. --- .-. --. . - - .- -... .-.. ."
english_text_output = morse_to_text(morse_code_input)
print("Morse Code:", morse_code_input)
print("English Text:", english_text_output)
