import requests
import json
url = "https://www.google.com"
response = requests.get(url)
x = response.text
# x must be file for this to work:
#with open(x, "wt") as f:
#    writeData = f.write()

url2 = "http://andrewbeatty1.pythonanywhere.com/books"
#response = requests.get(url2)
#print(response.json())


def readBooks():
    response = requests.get(url2)
    #print(response.headers)
    #print(response.content, "\n")
    #print(response.status_code)
    return response.json()

def getAllBooks():
    response = requests.get(url)
    return response.json()


def readBook(id):
    geturl = url + "/" + str(id)
    response = requests.get(url2)
    if response.status_code != 200:
        print("API not working")
    else:
        print("API working")
        txt = json.loads(response.text)
        #print(int(txt['id']))
        #print(response.text('id'))

    return response.json()

def createbook(book):
    response = requests.post(url2, json=book)
    if response.status_code == 200:
        print("Good")
    else:
        print("Bad!")
    #headers ={ "Content-type": "application/json"}
    #response = requests.post(url, data=json.dumps(book), headers=headers)
    return response.json()

def update(id, book):
    puturl = url2 + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(id):
    delUrl = url2 + "/" + str(id)
    response = requests.delete(delUrl)
    return response.json()

if __name__ == "__main__":
    #print(readBooks())
    readBook(id)
    #createbook(book)
    #update(id, book)
    #deletebook(id)