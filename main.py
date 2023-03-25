# TODO : Find out about morse code ✔
# done

# TODO: Map letters to morse code in a dictionary ✔
# Using english letters for now, taken from GitHub https://gist.github.com/mohayonao/094c71af14fe4791c5dd
LETTER_TO_MORSE = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}


# # checking map
# print(LETTER_TO_MORSE)
# # Taken into dictionary ✅

# Todo: Create a function that converts function to morse code ✔

def text_to_morse(text):
    """Converts text inputted into a morse code, and returns it with another str char_not_converted."""

    morse = ""
    char_not_converted = ""
    for character in text:
        if character == " ":
            morse += "       "
        elif character not in LETTER_TO_MORSE:
            char_not_converted += character + " "
        else:
            morse += f"{LETTER_TO_MORSE[character]}   "

    return morse, char_not_converted


# TODO: Call the function ✔
morse_code, unable_to_parse = text_to_morse(input("Enter your text to be converted to Morse code: \n").lower())
if len(unable_to_parse) > 0:
    # Since unable_to_parse also contains spaces, length of unable to parse characters will be half
    print(f"Unable to convert {len(unable_to_parse) // 2} characters: {unable_to_parse}")

print(f"Your text in morse code is (after removing unable to parse characters) :\n {morse_code}")

# TODO: Check the results, everything is working as you wished ✔
