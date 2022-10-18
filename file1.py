# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
# and stores it into a file called "cso.json".

import requests
import json
urlBegin = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAll(dataset):
    url = urlBegin + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

def formatted(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    valuecount = 0 
    for dim0 in range(0,sizes[0]):
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        label = dimensions[currentId]["category"]["label"][index]
        print(index)
        print("\t", label)
        print("\t\t", index)
        for dim1 in range(0,sizes[1]):
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label = dimensions[currentId]["category"]["label"][index]
            for dim2 in range(0,sizes[2]):
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label = dimensions[currentId]["category"]["label"][index]
                print("\t\t\t",label, " ", values[valuecount])
                valuecount += 1


if __name__ == "__main__":
    #getAllAsFile("FIQ02")
    formatted("FIQ02")
