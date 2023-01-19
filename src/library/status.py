class Status():
    def __init__(self, manager):
        self.manager = manager
        self._status = None

    def statusMessage(self, returnCode):
        if returnCode == -1:
            self.status = 'Temperature in range, process already running. '
        elif returnCode == 0:
            self.status = 'Temperature exceeded range, stopping process. '
        elif returnCode == 1:
            self.status = 'Temperature in range, process not yet started. Starting process. '
        elif returnCode == 2:
            self.status = 'Temperature in range, process was interupted. Restarting process. '

        return self.status

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        self._status = value

    @status.deleter
    def status(self):
        del self._status
