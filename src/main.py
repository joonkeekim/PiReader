import os
from detector import hotword


class Main():
    def __init__(self):
        self.detector = hotword()
        pass
    def run(self):
        pass



if __name__ == '__main__':
    print('PiReader is Running...')
    pi = Main()
    pi.run()
