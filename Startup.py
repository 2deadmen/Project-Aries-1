
import time

import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import wikipedia
import smtplib
import datetime



class Setup:
    def __init__(self):
        self.engine=pyttsx3.init('sapi5')
        self.voices=self.engine.getProperty('voices')
        self.engine.getProperty('voice')
        self.detector=sr.Recognizer()

    def speak(self,text):
        """it will take the text and speak it out loud"""
        self.engine.setProperty('voice',  self.voices[1].id)
        self.engine.say(text)
        self.engine.runAndWait()

    def take(self):
   

        with sr.Microphone() as source:
            print("listening")
            audio=self.detector.listen(source)

            try:
                print("recognizing")
                query=self.detector.recognize_google(audio,language='en-in').lower()
                print(f'user said {query}')
                return query

            except Exception as e:
                self.speak("can you repeat that please")
                self.take()
                return query
                query=None
            return query

        

    

   

    

  





