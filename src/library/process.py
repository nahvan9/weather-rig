import threading
import subprocess


class Process(threading.Thread):
    def __init__(self, batch_path):
        threading.Thread.__init__(self)
        self.batch_path = batch_path
        
    def run(self):
        self.process = subprocess.Popen([self.batch_path], creationflags=subprocess.CREATE_NEW_CONSOLE) #calls batch script in new terminal window
        return self.process.pid

    def kill(self):
        self.process.kill()
    