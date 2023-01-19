from discordwebhook import Discord

class DiscordNotifs():
    def __init__(self, webhookurl):
        self.discord = Discord(url=webhookurl)

    def postMessage(self, content):
        self.discord.post(content=content)