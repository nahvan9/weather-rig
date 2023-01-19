from library.services.cmd_msg import CmdMsg
from library.services.logger import Logger
from library.services.discord_notifications import DiscordNotifs


class NotificationManager():
    def __init__(self, manager, options):
        self.manager = manager
        self.dscNotif = options.get('discord')
        self.logging = options.get('logging')
        self.cmdMsg = options.get('cmd_output')

        self._discord = None
        self._logger = None
        self._printCli = None
        self._services = []

        self.startServices()


    # Start selected services
    def startServices(self):
        if self.dscNotif == True:
            url = self.manager.config['webhookurl']
            self._discord = DiscordNotifs(webhookurl=url)
            self._services.append(self._discord)
        if self.logging == True:
            self._logger = Logger()
            self._services.append(self._logger)
        if self.cmdMsg == True:
            self._printCli = CmdMsg()
            self._services.append(self._printCli)

    # Each service must have a "post" method
    def postServices(self):
        for service in self._services:
            service.post()

