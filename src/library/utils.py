import yaml
import requests
import psutil
import time

from geopy.geocoders import Nominatim


def getConfig(file):
    with open(file, 'r') as y:
        obj = yaml.safe_load(y)
    return obj

def getOptions(file):
    options = getConfig(file)['notifications']
    return options

def getOptionsAsArrys(dictArr):
    keysArr = []
    valArr = []

    for i in dictArr:
        [(key, value)] = i.items()
        keysArr.append(key)
        valArr.append(value)

    return [keysArr, valArr]

def getLocation(addr):
    geolocator = Nominatim(user_agent="App")
    location = geolocator.geocode(addr)

    return location.latitude, location.longitude

def getTemperature(key, lat, log):
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={key}&q={lat} {log}&aqi=no").json()
    tempC = response['current']['temp_c']
    tempF = response['current']['temp_f']

    return tempC, tempF    

def checkProcess(pid):
    if psutil.pid_exists(pid):
        return True
    else:
        return False    
    
def currentTime():
    return time.strftime("%H:%M:%S", time.localtime())

def currentTimeFile():
    return time.strftime("%H_%M_%S", time.localtime())

def HrMinSec(seconds):
    return time.strftime("%H hr, %M min, %S s", time.gmtime(seconds))

def unpackDict(dict):
    k = []
    v = []
    for key in dict:
        v.append(dict[key])
        k.append(key)

    return [k, v]

def strDictValues(dict):
    copyDict = dict
    for key in copyDict:
        copyDict[key] = str(copyDict[key])

    return copyDict
