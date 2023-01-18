from geopy.geocoders import Nominatim
import yaml
import requests
import psutil


def getConfig(file):
    with open(file, 'r') as y:
        obj = yaml.safe_load(y)
    return obj

def getLocation(addr):
    geolocator = Nominatim(user_agent="App")
    location = geolocator.geocode(addr)
    return location.latitude, location.longitude

def getHrTemperature(key, lat, log):
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={key}&q={lat} {log}&aqi=no").json()
    tempC = response['current']['temp_c']
    tempF = response['current']['temp_f']

    return tempC, tempF    

def checkProcess(pid):
    if psutil.pid_exists(pid):
        return True
    else:
        return False