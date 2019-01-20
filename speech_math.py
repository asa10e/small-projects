import math
from random import randint
from gtts import gTTS # Google text to speech
import subprocess # For playing an audiofile
import speech_recognition as sr

def get_user_answer():
    """
    Listens for sound and stores the sound as text
    """

    rec = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        audio = rec.listen(source)

    user_response = rec.recognize_google(audio)
    return user_response


def make_math_problem(r1 = [2,10], r2 = [2,10], game = 'multiplication'):
    '''
    Returns a tuple with the problem (in string format) and the answer (an integer).
    '''

    a = str(randint(r1[0],r1[1]))
    b = str(randint(r2[0],r2[1]))

    if game == 'multiplication':
        problem = '{0} times {1}'.format(a,b)
        answer = int(a)*int(b)
    elif game == 'addition':
        problem = '{0} plus {1}'.format(a,b)
        answer = int(a) + int(b)

    return (problem, answer)

def say(text):
    '''
    Computer says the inputted text
    '''
    tts = gTTS(text = text, lang = 'en-us') # American accent
    tts.save('tempaudio.mp3') # Make an audio file and save it
    speech = subprocess.call(['afplay','tempaudio.mp3']) # Play that audio file


def one_problem_one_answer(r1, r2, game):

    problem, answer = make_math_problem(r1, r2, game) # Make the math problem
    say(problem) # Tell the user what the problem is
    print('Ok go') # Visual cue; unnecesary
    user_response = get_user_answer() # Get the user's answer to the problem
    print(user_response)

    try:
        if int(user_response) == answer:
            say('Correct.')
        elif int(user_response) != answer:
            say('Incorrect. Answer was {}.'.format(answer))
        elif str(user_response) == 'exit game':
            return user_response
    except:
        say("Sorry, I couldn't understand that.")

    return user_response


def main(r1 = [2,10], r2 = [2,10], game = 'multiplication'):

    user_response = ''
    while user_response != 'exit game': # Keep doing math problems until the user says 'exit game'
        user_response = one_problem_one_answer(r1, r2, game)

    say('Thanks for playing!')


if __name__ == '__main__':
    main()
