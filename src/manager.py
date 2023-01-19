


from library import utils
from weather_rig import WeatherRig

class Manager():
    def __init__(self, config):
        self.app = WeatherRig(config)
        self.options = utils.getOptions(config)


    def run(self):
        while True:
            output = self.app.run()
            print(output)
            self.app.waitNext()





if __name__ == "__main__":
    app = Manager(config="./src/config.yaml")

    print(app.options)
    app.run()

