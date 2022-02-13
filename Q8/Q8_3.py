# Morse code dictionary for your convenience
MORSE_CODE_DICTIONARY = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/"
}

"""
This function takes in a string representing a sentence or word,
and converts the string into morse code.

Arguments:
    sentence (str): A string representing a sentence or word
Returns:
    the morse code representation of the sentence
Examples:
    "SOS" => "... --- ..."
    "Hello World" => ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
"""


def morse_code_translator(sentence):
    s = ""
    for c in sentence:
        c = c.upper()
        s += MORSE_CODE_DICTIONARY[c]
        s += ' '
    s = s[:len(s)-1]
    return s
