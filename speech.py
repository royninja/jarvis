import speech_recognition as sr
import pyttsx3
import time
import os
from time import ctime
import pyaudio
#engine = pyttsx3.init()
def jarvis():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        data = r.recognize_google(audio)
        print('you said: '+data)
        if "hello Jarvis" in data:
            engine = pyttsx3.init()
            engine.say('Hello Sayan')
            engine.runAndWait()
        if "hi" in data:
            engine = pyttsx3.init()
            engine.say('Hi Boss')
            engine.runAndWait()
        if "rate" in data:
            engine = pyttsx3.init()
            engine.say('My Current Speaking Rate is : '+str(engine.getProperty('rate')))
            engine.runAndWait()
        if "how are you" in data:
            engine = pyttsx3.init()
            engine.say('Am Fine Sir! Sir wht can i do for you?')
            engine.runAndWait()
        if "what time is it" in data:
            engine = pyttsx3.init()
            engine.say('Current time is ' + str(ctime()))
            engine.runAndWait()
        if "sleep Jarvis" in data:
            engine = pyttsx3.init()
            engine.say('Ok Sir am taking leave Sir!')
            engine.runAndWait()
            exit(0)
        if "check my mail" in data:
            engine = pyttsx3.init()
            engine.say('Certainly Sir! Its in background please check the Taskbar')
            os.system("start chrome https://gmail.com")


while True:
    jarvis()
    #hello jarvis
    #hi
    #rate
    #how are you
    #what time is
    #sleep jarvis
    #check my mail