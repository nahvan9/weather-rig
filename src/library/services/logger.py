import logging
import os
import time

from library import utils

class Logger():
    def __init__(self, manager, logDir):
        self.manager = manager
        self.curTime = utils.currentTimeFile()
        self.logPath = os.path.join(logDir, self.curTime+".log")
        self.level = logging.getLevelName(self.manager.config['logLevel'])

        if not os.path.exists(logDir):
            os.makedirs(logDir)
        
        logging.basicConfig(
            filename=self.logPath, 
            encoding='utf-8', 
            level=self.level,
            format='%(asctime)s %(message)s'
        )

        
    def post(self, content):
        logging.info(content)
    