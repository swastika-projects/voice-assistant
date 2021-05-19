import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import faceRecognition
import random
import operator
import requests
from urllib.request import urlopen

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def getUsername():
    try:
        with sr.Microphone() as source:
            talk('Hello! I am Bob What do i call you?')
            uname = listener.listen(source)
            user_name = listener.recognize_google(uname)
            user_name = user_name.lower()
    except:
        pass
    return user_name

def take_command():
    try:
        with sr.Microphone() as source:
            username = getUsername()
            talk('Hello' + username)
            print('hello ' + username)
            #talk(username)
            talk('Call my name before speaking to let me know you are talking to me')
            talk('How may i assist you?')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            while command == 'who am i':
                talk('Your name is ' + username)
                talk('How may i assist you?')
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
            if 'bob' in command:
                command = command.replace('bob', '')
                print(command)
    except:
        pass
    return command


def run_bob():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'order' in command:
        order = command.replace('order','')
        talk('Redirecting you to Amazon website.')
        webbrowser.open_new_tab(order)
    elif 'detect' or 'recognise' in command:
        faceRecognition.face_rec()
    elif 'what' or 'who' or 'where' or 'how' or 'when' in command:
        person = command.replace('what' or 'who' or 'where' or 'how' or 'when', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'stop' in command:
        exit()
    else:
        talk('Please say the command again.')


while True:
    run_bob()
