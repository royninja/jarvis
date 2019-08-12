import pyttsx3
import speech_recognition as sr


def ThinkNow(data):
    if "Hello" in data:
        sayJarvis('Hello Sayan')


def listenhim():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print('You said : ' + data)
    except sr.UnknownValueError:
        sayJarvis('Sorry Sir Didnot get You!')

    return data


def sayJarvis(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # two voice are here just chenage the array reference
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    listenhim()
    ThinkNow()
