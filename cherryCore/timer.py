# Timer core

from rich.console import Console
from time import sleep
from cherryCore.cherry import CherrySession

from datetime import datetime, timedelta

class Timer():
    def __init__(self, console):
        self.cherrySession = CherrySession()
        self.bufTime = {
            key: None for key in [  
                'startTime', 
                'totalTime', 
                'endTime', 
                'currentTime', 
                'formattedTime',
                ]
            }
        self.console = console

    def run(self):
        self.activateMode()
        # required for storing data later
        startTime = datetime.now()
        totalTime = timedelta(minutes=self.cherrySession.focusTime)
        endTime = startTime + totalTime
        self.bufTime['startTime'] = startTime
        self.bufTime['totalTime'] = totalTime
        self.bufTime['endTime'] = endTime
        while datetime.now() < endTime:
            currentTime = endTime - datetime.now()
            dummyTime = datetime(1, 1, 1) + currentTime
            formattedTime = dummyTime.strftime('%M:%S')


            self.display(formattedTime)
            sleep(1)

    def display(self, formattedTime):
        self.console.print(f'   {formattedTime}', end='\r')


    def activateMode(self):
        self.console.print()



def main():
    a = Timer(Console())
    a.cherrySession.printConfig()
    a.run()


if __name__ == '__main__':
    main()


