# Timer core

from rich.console import Console
from time import sleep
from cherryCore.cherry import CherrySession

from datetime import datetime, timedelta

import sys
import tty, termios
import select



def aread_key():
    inp, _, _ = select.select([sys.stdin], [], [], 0)
    if inp:
        key = sys.stdin.read(1)
        return key
    else:
        return None


class Timer():
    def __init__(self, currentMode):
        self.old_terminal_settings = termios.tcgetattr(sys.stdin)
        self.cherrySession = CherrySession()
        self.running = False
        self.bufTime = {
            key: None for key in [  
                'startTime', 
                'totalTime', 
                'endTime', 
                'currentTime', 
                'formattedTime',
                ]
            }
        self.currentMode = currentMode

        # temp
        self.console = Console()

    # @staticmethod
    def raw_mode_on(func):
        def wrapper(self, *args, **kwargs):
            tty.setraw(sys.stdin.fileno())
            result = func(self, *args, **kwargs)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_terminal_settings)
            return result
        return wrapper

    # @staticmethod
    def raw_mode_off(func):
        def wrapper(self, *args, **kwargs):
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_terminal_settings)
            result = func(self, *args, **kwargs)
            tty.setraw(sys.stdin.fileno())
            return result
        return wrapper


    @raw_mode_on
    def run(self):
        self.running = True
        self.activateMode()
        # required for storing data later
        startTime = datetime.now()
        totalTime = timedelta(minutes=self.cherrySession.focusTime)
        endTime = startTime + totalTime
        self.bufTime['startTime'] = startTime
        self.bufTime['totalTime'] = totalTime
        self.bufTime['endTime'] = endTime

        while datetime.now() < endTime:
            if self.running:
                currentTime = endTime - datetime.now()
                dummyTime = datetime(1, 1, 1) + currentTime
                formattedTime = dummyTime.strftime('%M:%S')
                self.display(formattedTime)

            key = aread_key()
            if key == 'q':
                self.displayAnything('Timer has been stopped.\nSee you later)\n')
                break
            elif key == ' ':
                self.running = not self.running
            elif key == '\x03':
                try:
                    raise KeyboardInterrupt
                except KeyboardInterrupt:
                    self.displayAnything(f'Oh, you are leaving...\nWell, bye-bye then\n')
                    break

            sleep(0.1)

    def display(self, formattedTime):
        self.console.print(f'   {formattedTime}', end='\r')

    @raw_mode_off
    def displayAnything(self, anything):
        self.console.print(f'{anything}       ')

    def activateMode(self):
        self.console.print()



def main():
    a = Timer(Console())
    a.cherrySession.printConfig()
    a.run()


if __name__ == '__main__':
    main()


