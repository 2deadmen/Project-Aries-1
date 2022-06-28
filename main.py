import time

import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import wikipedia
import smtplib
import datetime


###n Terminal type

# pip install pipwin
# Then
#
# pipwin install pyaudio


print("Started up boss")








engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.getProperty('voice')

def speak(text):
    """it will take the text and speak it out loud"""
    engine.setProperty('voice',  voices[1].id)
    engine.say(text)
    engine.runAndWait()
  

def bootup():
    engine.setProperty("rate", 200)
    a = int(datetime.datetime.now().hour)

    if a>0 and a<12:
        speak(f"good morning Sir welcome back its {a}am ")
    elif a >=12 and a<18:
        speak(f"good afternoon Sir welcome back its {a}pm")

    else:
        speak(f"good evening Sir welcome back its {a}pm")

    speak("How may i be of help today")
bootup()

def take():
    detector=sr.Recognizer()

    with sr.Microphone() as source:
        print("listening")
        audio=detector.listen(source)

        try:
            print("recognizing")
            query=detector.recognize_google(audio,language='en-in').lower()
            print(f'user said {query}')

        except Exception as e:
            speak("can you repeat that please")
            take()
            query=None
        return query

query=take()


if 'wikipedia' in query:
    speak("searching on wikipedia")
    query=query.replace('wikipedia',"")
    resulta=wikipedia.summary(query,sentences=2)
    speak(resulta)

elif 'time now' in query:
    a = int(datetime.datetime.now().hour)

    if a > 0 and a < 12:
        speak(f" its {a}am ")
    elif a >= 12 and a < 18:
        speak(f"its {a}pm")

    else:
        speak(f" its {a}pm")

elif 'open youtube' in query:
    path='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(path).open('youtube.com')


