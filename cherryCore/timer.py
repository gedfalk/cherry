# Timer core

from rich.console import Console
from time import sleep
from cherry import CherrySession

class Timer():
    def __init__(self, console):
        self.cherrySession = CherrySession()
        self.console = console

    def run(self):
        totalSeconds = self.cherrySession.focusTime * 60
        for i in range(totalSeconds + 1):
            self.console.print(i)
            sleep(1)

def main():
    a = Timer(Console())
    a.cherrySession.printConfig()
    a.run()


if __name__ == '__main__':
    main()


