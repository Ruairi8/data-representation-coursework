#Program to work out the average book price from all the books on the server
import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()

def avBookPrice():
    pass