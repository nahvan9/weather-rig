# Service class to write output to console

class CmdMsg():
    def __init__(self, manager):
        self.app = manager

    def post(self, content, *args, **kwargs):
        print(content)
        if args != ():
            print(*args)
        if kwargs != {}:
            print(**kwargs)
        