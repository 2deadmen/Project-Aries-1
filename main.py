import time

import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import wikipedia
import smtplib
import datetime
from Startup import Setup
import requests
###n Terminal type

# pip install pipwin
# Then
#
# pipwin install pyaudio


print("Started up boss")




setup=Setup()
setup.speak("Hello ")







  
def bootup():
    # self.engine.setProperty("rate", 200)
    a = int(datetime.datetime.now().hour)

    if a>0 and a<12:
        setup.speak(f"good morning Sir welcome back its {a}am ")
    elif a >=12 and a<18:
        setup.speak(f"good afternoon Sir welcome back its {a}pm")

    else:
        setup.speak(f"good evening Sir welcome back its {a}pm")

    setup.speak("How may i be of help today")
bootup()



results=setup.take()
print(results)



if 'wikipedia' in results:
    setup.speak("searching on wikipedia")
    query=results.replace('wikipedia',"")
    resulta=wikipedia.summary(query,sentences=2)
    setup.speak(resulta)

elif 'time now' in results:
    a = int(datetime.datetime.now().hour)

    if a > 0 and a < 12:
        setup.speak(f" its {a}am ")
    elif a >= 12 and a < 18:
        setup.speak(f"its {a}pm")

    else:
        setup.speak(f" its {a}pm")

elif 'open youtube' in results:
    path='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(path).open('youtube.com')


elif 'dad joke' or 'add joke' in results:
    request=requests.get(" https://icanhazdadjoke.com/slack")
    request.raise_for_status()
    data=request.json()
    setup.speak(data['attachments'][0]['fallback'])


elif "joke" or "jokes" in results:
    request=requests.get(" https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,political,sexist")
    request.raise_for_status()
    data=request.json()
    setup.speak(data['joke'])
