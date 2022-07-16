import os
import webbrowser
import datetime
from matplotlib.pyplot import ginput
import requests
class Tech:

    def __init__(self):
        pass

    def openyt(self,results):
        path='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(path).open('youtube.com')

    def timenow(self):
        a = int(datetime.datetime.now().hour)

        if a > 0 and a < 12:
            return f"its {a}am "
            
        elif a >= 12 and a < 18:
            return f"its {a}am "

        else:
            return f"its {a}am "
        

    def dad_joke(self):
            request=requests.get(" https://icanhazdadjoke.com/slack")
            request.raise_for_status()
            data=request.json()
            return (data['attachments'][0]['fallback'])

    def joke(self):
            request=requests.get(" https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,political,sexist")
            request.raise_for_status()
            data=request.json()
            return (data['joke'])
        
# //checking for ginput