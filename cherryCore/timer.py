# Timer core

from rich.console import Console
from time import sleep
from cherryCore.cherry import CherrySession

from datetime import datetime, timedelta

import sys
import tty, termios
import select


_DEV_ = 1
_DEV_ = 100


def aread_key():
    inp, _, _ = select.select([sys.stdin], [], [], 0)
    if inp:
        key = sys.stdin.read(1)
        return key
    else:
        return None


class Timer():
    def __init__(self, timer_settings=None, currentMode=None):
        self.old_terminal_settings = termios.tcgetattr(sys.stdin)
        self.cherrySession = CherrySession(timer_settings)
        self.finished = False
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
    def raw_mode_on_and_off(func):
        def wrapper(self, *args, **kwargs):
            tty.setraw(sys.stdin.fileno())
            result = func(self, *args, **kwargs)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_terminal_settings)
            return result
        return wrapper
    # @staticmethod
    def raw_mode_off_and_on(func):
        def wrapper(self, *args, **kwargs):
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_terminal_settings)
            result = func(self, *args, **kwargs)
            tty.setraw(sys.stdin.fileno())
            return result
        return wrapper


    @raw_mode_on_and_off
    def run(self):
        self.running = True
        self.activateMode()
        # required for storing data later
        self.bufTime['startTime'] = datetime.now()

        
        for r in range(self.cherrySession.rounds):
            currentTime = timedelta(minutes=self.cherrySession.focusTime)
            self.displayAnything(f'Round {r+1}')
            while currentTime.total_seconds() > 0:
                    
                # region Reading Keystrokes
                key = aread_key()
                if key == 'q':
                    self.displayAnything('Timer has been stopped.\nSee you later)\n')
                    # self.finished = True
                    return
                    break
                elif key == ' ':
                    self.running = not self.running
                elif key == '\x03':
                    try:
                        raise KeyboardInterrupt
                    except KeyboardInterrupt:
                        self.displayAnything(f'Oh, you are leaving...\nWell, bye-bye then\n')
                        # self.finished = True
                        return
                else:
                # endregion
                    if self.running:
                        self.displayTime(currentTime)
                        currentTime -= timedelta(milliseconds=100*_DEV_)

                    
                sleep(0.1)
        else:
            self.displayAnything(f'Our work here is over... Well Done!)')

    @raw_mode_off_and_on
    def displayTime(self, currentTime):
        dummyTime = datetime(1, 1, 1) + currentTime
        formattedTime = dummyTime.strftime('%M:%S')
        self.console.print(f'_  {formattedTime}', end='\r')

    @raw_mode_off_and_on
    def displayAnything(self, anything):
        self.console.print(f'{anything}   ')

    def activateMode(self):
        self.console.print()


def main():
    a = Timer(Console())
    a.run()


if __name__ == '__main__':
    main()


