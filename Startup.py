
import time
import requests
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import wikipedia
import smtplib
import datetime
from sqlalchemy import Table, Column, Integer, ForeignKey,Float
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trial-4.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Volume(db.Model):
    __tablename__="volume"
    id=db.Column(db.Integer,primary_key=True)
    volume=db.Column(db.Float)
db.create_all()



class Setup:
    def __init__(self):
        self.engine=pyttsx3.init('sapi5')
        self.voices=self.engine.getProperty('voices')
        self.rate=self.engine.getProperty('rate')
        self.volume= self.engine.getProperty('volume') 
        self.engine.getProperty('voice')
        self.detector=sr.Recognizer()
        self.count=0
    def speak(self,text):
        """it will take the text and speak it out loud"""
        posts = Volume.query.filter_by(id=1).first()
        # print(posts.volume)
        self.engine.setProperty('volume',posts.volume)
        self.engine.setProperty('voice',  self.voices[1].id)
        self.engine.setProperty('rate',250)
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
    def kai(self,results):
        b=results.split()
        for i in b:
            try:
                z=int(i)
            except:
                z=i
        
        if type(z)==int:
            hola=z/100
            print( hola)

            id=1
            post = Volume.query.get(id)
            print("workin1")
            post.volume=hola
            
            db.session.commit()
            print("entered")
       
        # b=results.split()
        # for i in b:
        #     try:
        #         z=int(i)
        #     except:
        #         z=i
        
        # if type(z)==int:
        #     hola=z/100
        #     print( hola)
        #     id=1
        #     post = Volume.query.get(id)
        #     post.volume=hola/100
        #     db.session.commit()
        #     print("done")
