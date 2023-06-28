# Timer core

from rich.console import Console
from time import sleep
from cherryCore.cherry import CherrySession

from datetime import datetime, timedelta


class Timer():
    def __init__(self, console):
        self.cherrySession = CherrySession()
        self.console = console

    def run(self):
        # required for storing data later
        startTime = datetime.now()
        totalTime = timedelta(minutes=self.cherrySession.focusTime)
        endTime = startTime + totalTime 
        while datetime.now() < endTime:
            currentTime = endTime - datetime.now()
            dummyTime = datetime(1, 1, 1) + currentTime
            formattedTime = dummyTime.strftime('%M:%S')
            self.console.print(formattedTime, end='\r')
            sleep(1)


def main():
    a = Timer(Console())
    a.cherrySession.printConfig()
    a.run()


if __name__ == '__main__':
    main()


