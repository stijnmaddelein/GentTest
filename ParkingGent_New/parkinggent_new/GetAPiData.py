from dataclasses import dataclass, fields
import requests
import json

""" 
Get the data from the API
 """
def getData():
    response = requests.get("https://data.stad.gent/api/v2/catalog/datasets/bezetting-parkeergarages-real-time/records")
    ReturnValue = FormatData(response)
    return ReturnValue


#want to change formating to simple serialized class
#easier to work with

""" 
change the raw json format
into a usable format for importing it into the database
 """
def FormatData(Data: requests.Response):

    ResponseData = ResponseFormat(Data)
    ReturnValue = {}
    i = 0
    Dict1Value = ResponseData.get("records")

    for value in Dict1Value:
        i=i+1
        ReturnValue[i] = ListFormat(value)

            
    return ReturnValue

# change the format of the response from json string to dictionary
def ResponseFormat(Data: requests.Response):
    TempData = json.loads(Data.content)
    ReturnValue = dict(TempData.items())
    return ReturnValue

# recursive format call to get dictionary with useful data
# every call gives one dictionary with all data inside
def ListFormat(Data):
    if "record" in Data.keys():
        TempDict=Data.get("record")
        tempjson=json.dumps(TempDict)
        ReturnValue=json.loads(tempjson)
        ReturnValue = ListFormat(dict(ReturnValue.items()))
    if "fields" in Data.keys():
        TempDict=Data.get("fields")
        tempjson=json.dumps(TempDict)
        ReturnValue=json.loads(tempjson)
        return dict(ReturnValue.items())
    return ReturnValue.items()