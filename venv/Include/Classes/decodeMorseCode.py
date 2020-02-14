def decodeMorse(morse_code):

    decodedMessage = []
    morseLetters = []
    decodedMessageStr = ""
    decoder = {".-": "A",
               "-...": "B",
               "-.-.": "C",
               "-..": "D",
               ".": "E",
               "..-.": "F",
               "--.": "G",
               "....": "H",
               "..": "I",
               ".---": "J",
               "-.-": "K",
               ".-..": "L",
               "--": "M",
               "-.": "N",
               "---": "O",
               ".--.": "P",
               "--.-": "Q",
               ".-.": "R",
               "...": "S",
               "-": "T",
               "..-": "U",
               "...-": "V",
               ".--": "W",
               "-..-": "X",
               "-.--": "Y",
               "--..": "Z",
               ".----": "1",
               "..---": "2",
               "...--": "3",
               "....-": "4",
               ".....": "5",
               "-....": "6",
               "--...": "7",
               "---..": "8",
               "----.": "9",
               "-----": "0",
               "........": "Error",
               "...-.-": "End",
               "...-.": "Roger",
               "-.-.-": "Start",
               ".-.-.-": ".",
               "...---...": "SOS",
               "--..--": ",",
               "..--..": "?",
               ".----.": "\'",
               "-.-.--": "!",
               "-..-.": "/",
               "-.--.": "(",
               "-.--.-": ")",
               ".-...": "&",
               "---...": ":",
               "-.-.-.": ";",
               "-...-": "=",
               ".-.-.": "+",
               "-....-": "-",
               "..--.-": "_",
               ".-..-.": "\"",
               "...-..-": "$",
               ".--.-.": "@",}

    morseWords = morse_code.split("   ")
    for i in range (0, len(morseWords)):
        morseLetters.append(morseWords[i].split())

    for i in range (0, len(morseLetters)):
        for k in range (0, len(morseLetters.__getitem__(i))):
            if decoder.get(morseLetters.__getitem__(i)[k]) != None:
                decodedMessage.append(decoder.get(morseLetters.__getitem__(i)[k]))
                decodedMessageStr += decodedMessage.pop()
        decodedMessageStr += " "

    return decodedMessageStr.strip()