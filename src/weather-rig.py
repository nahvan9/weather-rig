import time

import utils
import process


class WeatherRig():
    def __init__(self, config):
        self.config = utils.getConfig(config)
        self.apikey = self.config["weatherAPIKey"]
        self.checkInterval = self.config['checkInterval'] 
        self.scriptPath = self.config["scriptPath"]
        
        self.location = self.config["cityAndState"]
        self.tempUnits = self.config['tempUnits']
        self.startTemp = self.config["startTemp"]
        self.stopTemp = self.config["stopTemp"]
        self.runAtStart = self.config["runAtStart"]
        
        self.lat, self.log = utils.getLocation(self.location)
        self.process = process.Process(self.scriptPath)
        self.pid = None
        
        
    def getCurTemperature(self):
        tempC, tempF = utils.getTemperature(self.apikey, self.lat, self.log)
        if self.tempUnits == "F":
            return tempF
        elif self.tempUnits == "C":
            return tempC

    def checkTcond(self):
        t = self.getCurTemperature()
        if t <= self.startTemp:
            return 1
        elif t> self.startTemp and t< self.stopTemp:
            return 2
        else:
            return 0

    def startScript(self):
        self.pid = self.process.run()
        
    def stopScript(self):
        self.process.kill()
        self.pid = None

    def checkProc(self):
        if self.pid != None:
            if utils.checkProcess(self.pid) == False:
                self.pid = None
                return True
    
    
if __name__ == "__main__":
    app = WeatherRig("./src/config.yaml")
    
    # Start loop
    while True:
        curTtme = utils.currentTime()
        temperature = app.getCurTemperature()
        print(f"Time: {curTtme} | Temperature in {app.location}:", temperature, f"{app.tempUnits}")
        i = app.checkTcond()
        if app.checkProc():
            print("Script not running! You may have accidentally closed it. ") 
        
        if app.pid == None:
            if i != 0:
                print("<runAtStart> parameter is set to True, and temperature is within range. Starting script...")
                app.startScript()
                print("Process ID:", app.pid)
        elif app.pid != None:
            if i == 0:
                print("Temperature above stopTemp, stop script.")
                app.stopScript()
            else:
                print(f"Temperature within acceptable range, doing nothing. Process ID: {app.pid}")
        
        print(f"Sleeping {utils.HrMinSec(app.checkInterval)}...\n")    
        time.sleep(app.checkInterval)
        