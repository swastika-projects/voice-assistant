import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import wolframalpha
import sys
import faceRecognition

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_username():
    try:
        with sr.Microphone() as source:
            talk('Hello! I am bob. What do i call you?')
            print('Say your name...')
            uname = listener.listen(source)
            user_name = listener.recognize_google(uname)
            user_name = user_name.lower()
            talk('Hello' + user_name)
            print('hello ' + user_name)
            talk('Call my name before speaking to let me know you are talking to me')
    except:
        pass
    #return user_name


def take_command():
    try:
        with sr.Microphone() as source:
            talk('How may i assist you?')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bob' in command:
                command = command.replace('bob', '')
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

    elif "calculate" in command.lower():

        app_id = "AX233G-8UQVX7WEA4"
        client = wolframalpha.Client(app_id)
        indx = command.lower().split().index('calculate')
        query = command.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("Answer is : " + answer)
        talk("The answer is " + answer)

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
        order = command.replace('order', '')
        talk('Redirecting you to Amazon website.')
        webbrowser.open_new_tab(order)

    elif 'what' or 'who' or 'where' or 'how' or 'when' in command:
        person = command.replace('what' or 'who' or 'where' or 'how' or 'when', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'stop' in command:
        sys.exit()

    elif 'detect' or 'recognise' in command:
        faceRecognition.face_rec()

    else:
        talk('Please say the command again.')

cnt = 1

while True:
    if cnt == 1:
        get_username()
        cnt = cnt - 1
    run_bob()
