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
from fun import Fun
from tech import Tech
###n Terminal type

# pip install pipwin
# Then
#
# pipwin install pyaudio


print("Started up boss")

setup=Setup()
fun=Fun()
tech=Tech()



setup.speak("Hello ")



  
def bootup():
    # self.engine.setProperty("rate", 200)
    a = int(datetime.datetime.now().strftime("%H"))
    b = int(datetime.datetime.now().strftime("%M"))

    if a>0 and a<12:
        setup.speak(f"good morning Sir welcome back its {f'{a} {b}'}am ")
    elif a >=12 and a<18:
        setup.speak(f"good afternoon Sir welcome back its {f'{a} {b}'}pm")

    else:
        setup.speak(f"good evening Sir welcome back its {f'{a} {b}'}pm")

    setup.speak("How may i be of help today")
bootup()



results=setup.take()
print(results)



if 'wikipedia' in results:
    setup.speak("searching on wikipedia")
    resultswiki=fun.wikipedia(results)
    setup.speak(resultswiki)
    setup.take()

elif 'time now' in results:
   results=tech.timenow()
   setup.speak(results)

elif 'open youtube' in results:
    tech.openyt(results=results)


elif 'dad joke' or 'add joke' in results:
    result_dad=tech.dad_joke()
    setup.speak(result_dad)


elif "joke" or "jokes" in results:
        result_joke=tech.joke()
        setup.speak(result_joke)

