import pyttsx3

engine = pyttsx3.init()
engine.say('Good Morning Sayan')
# engine.runAndWait()

# rate

rate = engine.getProperty('rate')
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('The Quick Brown fox jumped over the lazy dog.')
engine.runAndWait()

