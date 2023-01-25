# Service class for discord notifications

from discordwebhook import Discord

from library.services import disc_msg 


class DiscordNotifs():
    def __init__(self, manager, webhookurl):
        self.manager = manager
        self.discord = Discord(url=webhookurl)

    # Receives content as a dictionary
    def post(self, content, *args, **kwargs):
        tempUnits = self.getTUnits(content)
        customNotifs = []
        
        # Get available custom stats
        for key in content.keys():
            if key in disc_msg.labelConversions:
                customNotifs.append(key)
        
        # Format custom stats
        customMsg = ''        
        for k in customNotifs:
            customMsg += (self.getMsg(k, content[k], unit=tempUnits)+'\n')
                
        print(customMsg)
        self.discord.post(content=customMsg)

    # Returns custom discord notifications    
    def getMsg(self, key, *args, **kwargs):
        label = disc_msg.labelConversions[key]
        func = getattr(disc_msg, label)
        return func(*args, **kwargs)
    
    def getTUnits(self, content):
        return content['Temp Units'] or 'C'
    