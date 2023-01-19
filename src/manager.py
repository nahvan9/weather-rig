from weather_rig import WeatherRig

from library import utils
from library.notifications import NotificationManager


class Manager():
    def __init__(self, config):
        self.config = utils.getConfig(config)
        self.app = WeatherRig(config)
        self.options = utils.getOptions(config)
        self.notifications = NotificationManager(self, self.options)

    def run(self):
        while True:
            output = self.app.run()
            self.notifications.postServices(output)
            self.app.waitNext()


if __name__ == "__main__":
    app = Manager(config="./src/config.yaml")