import threading
import subprocess


class Process(threading.Thread):
    def __init__(self, batch_path):
        threading.Thread.__init__(self)
        self.batch_path = batch_path
        
        
    def run(self):
        #calls batch script in new terminal window
        self.process = subprocess.Popen(
            [self.batch_path], 
            creationflags=subprocess.CREATE_NEW_CONSOLE
        ) 

        return self.process.pid

    def kill(self):
        self.process.kill()
    