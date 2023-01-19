import time

from library import utils
from library import process


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

        # Private atributes
        self._timeToWaitString = utils.HrMinSec(self.checkInterval)
        self._temperature = None
        self._curTime = None
        self._TCond = None
        self._procStat = None

        
        
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
        else:
            return False

    
    def run(self):
        self._curTtme = utils.currentTime()
        self._temperature = self.getCurTemperature()
        self._TCond = self.checkTcond()
        self._procStat = self.checkProc()

        returnValue = None
        if self.pid == None:
            if self._TCond != 0:
                # Temperature in range and script not started. Start script. 
                if self._procStat: 
                # Not the first instance started 
                    returnValue = 2
                else:
                    returnValue = 1
                
                self.startScript()
        elif self.pid != None:
            if self._TCond == 0:
                # temperature exceed limits. stop script
                self.stopScript()
                returnValue = 0
            else:
                # temp in range, script already running. do nothing
                returnValue = -1

        # API
        data = {
            'Time': self._curTtme,
            'Temperature': self._temperature,
            'Temp Units': self.tempUnits,
            'Return': returnValue,
            'Process ID': self.pid,
        }

        return data

    def waitNext(self):
        time.sleep(self.checkInterval)
        return        


# Test stand-alone, no notifications

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
        