# Service class for discord notifications

from discordwebhook import Discord

from library import utils

class DiscordNotifs():
    def __init__(self, manager, webhookurl):
        self.manager = manager
        self.discord = Discord(url=webhookurl)

    def post(self, content, *args, **kwargs):
        output = self.formatContent(content)
        
        self.discord.post(content=str(output))
        self.discord.post(content=str(*args))
        self.discord.post(content=str(**kwargs))

    def formatContent(self, data):
        formatData = utils.strDictValues(data)
        content = ""
        for key in formatData:
            content += key+": "
            content += data[key]
            content += "\n"

        return content
        
