import requests


request=requests.get(" https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,political,sexist")
request.raise_for_status()
data=request.json()
print(data['joke'])
