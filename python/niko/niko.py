import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
from Variables import ACTIVATION_WORD, COMMAND_TIME_OUT, SPEAK_SPEED
import time


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # << Change this to 0 to set the male voice


def speak(text, given_rate: int = 0) -> None:
    # rate: int = given_rate
    # if rate == 0:
    #     rate = SPEAK_SPEED
    engine.setProperty('rate', 20)
    engine.say(text)
    engine.runAndWait()
    time.sleep(2)


def parseCommand() -> str:
    listener = sr.Recognizer()
    print('Listening for a command')
    with sr.Microphone() as source:
        listener.pause_threshold = COMMAND_TIME_OUT
        input_speech = listener.listen(source)
    try:
        print('Rec...')
        Query: str = listener.recognize_google(input_speech, language='en_gb')
        print(f'U said: {query}')
    except Exception as exception:
        speak('Sorry, I did not understand')
        print(exception)
        return 'None'

    return Query


if __name__ == "__main__":
    query: list

    speak("Hello! Iam ready to assist you.")
    while 1:
        query = ['']
        # query = parseCommand().lower().split()

        if query[0] == ACTIVATION_WORD:
            query.pop(0)

            if query[0] == 'say':
                if 'hello' in query:
                    speak('Hi!')
                else:
                    speak(' '.join(query.pop()))
