# Service class to log output to log files

import logging
import os
import time

from library import utils

class Logger():
    def __init__(self, manager, logDir):
        self.manager = manager
        self.curTime = utils.currentTimeFile()
        self.logPath = os.path.join(logDir, self.curTime+".log")
        self.level = logging.getLevelName(self.manager.manager.config['logLevel'])

        if not os.path.exists(logDir):
            os.makedirs(logDir)
        
        logging.basicConfig(
            filename=self.logPath, 
            encoding='utf-8', 
            level=self.level,
            format='%(asctime)s %(message)s'
        )

        self.manager.addOutputs('Log Path', self.logPath)

        
    def post(self, content, *args, **kwargs):
        logging.info(content)
        if args != ():
            logging.info(args)
        if kwargs != {}:
            logging.info(kwargs)
    