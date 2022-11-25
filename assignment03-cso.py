# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
# and stores it into a file called "cso.json".

import requests
import json

def getAll(dataset):
    url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
    response = requests.get(url)
    return response.json()

def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

if __name__ == "__main__":
    getAllAsFile("FIQ02")

