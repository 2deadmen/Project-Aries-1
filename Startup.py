
import time
import requests
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
        self.count=0
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
                
                if  self.count == 0:
                    self.speak("can you repeat that please")
                    print(self.count)
                    self.count+=1
                    self.take()
                    return query
                    query=None
                    
                else:
                   
                    try:
                        requests.get("https://www.youtube.com/")
                    except requests.exceptions.RequestException as e:
                        self.speak("please check your internet connection")
                        self.take()
        #return query