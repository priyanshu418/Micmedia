import webbrowser
from datetime import date

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("speak anyting:")
    r.adjust_for_ambient_noise(source, duration=0.7)

    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        today = date.today();
        print("current date is")
        print(today)

        print("you said :{}".format(text))

        if (text == 'YouTube'):
            webbrowser.open('https:\\youtube.com')
        if text == 'Google':
            webbrowser.open('www.google.com')
        if text == 'gana':
            webbrowser.open('www.ganna.com')




    except sr.UnknownValueError:
        print("unknown value error occured")


    except sr.RequestError as e:
        print("could not request results ;{0}".format(e))