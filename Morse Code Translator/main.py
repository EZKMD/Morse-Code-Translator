from bidict import bidict

baseMorseKey = {
    '.-':'A',
    '-...':'B',
    '-.-.':'C', 
    '-..':'D', 
    '.':'E', 
    '..-.':'F', 
    '--.':'G', 
    '....':'H', 
    '..':'I', 
    '.---':'J', 
    '-.-':'K', 
    '.-..':'L', 
    '--':'M', 
    '-.':'N', 
    '---':'O', 
    '.--.':'P', 
    '--.-':'Q', 
    '.-.':'R', 
    '...':'S', 
    '-':'T', 
    '..-':'U', 
    '...-':'V', 
    '.--':'W', 
    '-..-':'X', 
    '-.--':'Y', 
    '--..':'Z', 
    '.----':'1', 
    '..---':'2', 
    '...--':'3', 
    '....-':'4', 
    '.....':'5', 
    '-....':'6', 
    '--...':'7', 
    '---..':'8', 
    '----.':'9', 
    '-----':'0', 
    '/':' '
    }

morseToValueKey = bidict(baseMorseKey)

valueToMorseKey = morseToValueKey.inverse



def morseTranslation():
    while True:
        try:


            phrase = input("Enter morse code: ")

            phraseArray = phrase.split()


            translatedArray = []

            for letter in phraseArray:
                translatedArray.append(morseToValueKey[letter])



            sentence = ''.join(translatedArray)
            print(f'Translation: {sentence}')
        except KeyError:
            print("Enter . or - ")
        
        except KeyboardInterrupt:
            print("\nPick another option: ")
            break


def valueTranslation():
    while True:
        try:


            phrase = input("Enter english to translate: ")

            phraseArray = list(phrase.upper())
            print(phraseArray)


            translatedArray = []

            for letter in phraseArray:
                translatedArray.append(valueToMorseKey[letter])
                translatedArray.append(' ')



            sentence = ''.join(translatedArray)
            print(f'Translation: {sentence}')
        except KeyError:
            print("Enter valid values")
        
        except KeyboardInterrupt:
            print("\nPick another option: ")
            break

def main():
    while True:
        try:
            print("""
                  
        [1] Translate Morse Code
        [2] Translate to Morse Code
                  """)
            
            choice = input("")
            if choice.strip() == '1':
                morseTranslation()
            elif choice.strip() =='2':
                valueTranslation()
            else:
                print("Enter 1 or 2")



        except KeyboardInterrupt:
            print('Program Terminated by User')
            break

main()