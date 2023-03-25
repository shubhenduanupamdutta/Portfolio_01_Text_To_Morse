# Find out about morse code ✔
# Letters of word are separated by 3 dits, I will use 3 space
# Words are separated by 7 dits, I will use 7 spaces

# Map letters to morse code in a dictionary ✔
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
    ")": "-.--.-",
    " ": "    "  # one more space will be added during conversion
}


# Create a function that converts function to morse code ✔

def text_to_morse(text: str) -> tuple[str, list[str]]:
    """Converts text inputted into a morse code, and returns it with another str of char_not_converted."""
    char_not_converted = []
    morse = ""
    for char in text:
        if char in LETTER_TO_MORSE:
            morse += LETTER_TO_MORSE[char] + "   "
        else:
            char_not_converted.append(char)

    return morse, char_not_converted


# Call the function ✔
morse_code, unable_to_convert = text_to_morse(input("Enter your text to be converted to Morse code: \n").lower())
if len(unable_to_convert) > 0:
    print(f"Unable to convert {len(unable_to_convert)} characters: {' '.join(unable_to_convert)}")

print(f"Your text in morse code is (after removing non convertable characters) :\n {morse_code}")

# Check the results, everything is working as you wished ✔
