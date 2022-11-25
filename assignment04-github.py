# Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name
# I do not need to see your key. The program should then commit those changes and push the file back to the repository.

from github import Github
import requests
from config import config as cf

# To hide the key, it is stored in a config file as a key-value pair in a dictionary and imported:
apikey = cf["githubkey"]
g = Github(apikey)

# Getting a github repository, it's contents and it's url:
repository = g.get_repo("Ruairi8/CThink")
file = repository.get_contents("textfile1.txt")
file_url = file.download_url
# Sending a GET request using the '.get()' method:
response = requests.get(file_url)
# Retrieving the text in unicode:
text = response.text
new_file = text.replace("Andrew", "Ruairi")
filePath = file.path
# The first string is the message, '.sha' are secure hash algorithms for security, branch is the github branch:
repository.update_file(filePath, "commit", new_file, file.sha, branch="main")

