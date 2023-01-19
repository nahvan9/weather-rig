from discordwebhook import Discord

class DiscordNotifs():
    def __init__(self, manager, webhookurl):
        self.manager = manager
        self.discord = Discord(url=webhookurl)

    def postMessage(self, content):
        self.discord.post(content=content)