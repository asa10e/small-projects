from pysine import sine
import time
import random

letters_to_codes = {'A': '.-', 'B': '-...','C': '-.-.','D': '-..','E': '.',
              'F': '..-.','G': '--.','H': '....','I': '..','J': '.---',
              'K': '-.-','L': '.-..','M': '--','N': '-.','O': '---',
              'P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-',
              'U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--',
              'Z': '--..' #,
              # '0': '-----','1': '.----','2': '..---','3': '...--',
              # '4': '....-',  '5': '.....','6': '-....','7': '--...',
              # '8': '---..','9': '----.',
              # '.': '.-.-.-', ',': '--..--','?': '..--..',"'": '.----.',
              # '!': '-.-.--', '(': '-.--.', ')': '-.--.-'
        }

class Morse(object):

    def __init__(self, text=None):

        if text != None:
            self.text = text.upper()
            self.code = ' '.join(letters_to_codes[l] for l in self.text)
        elif text == None:
            self.text, self.code = random.choice(list(letters_to_codes.items()))

    def play(self):
        for char in self.code:
            if char == '.':
                sine(frequency=700, duration=0.15)
            elif char == '-':
                sine(frequency=700, duration=0.45)
            elif char == ' ':
                pass

            time.sleep(.1)



def letter_trainer(mode='sound'):
    """
    Quizzes the user on random letters in morse code.
    mode is either 'sound' or 'text'
    """
    user_guess = ''
    while user_guess.lower() != 'exit':

        morse = Morse()
        if mode == 'sound':
            morse.play()
            user_guess = input('')

        elif mode == 'text':
            user_guess = input(morse.code + '\n').upper()

        if user_guess == morse.text:
            print('Correct!')
        elif user_guess != morse.text:
            print('Incorrect, answer was {}'.format(morse.text))
