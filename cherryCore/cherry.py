# ...

import time
import configparser


class Session():
    def __init__(self, focusTime=30, breakTime=5, lbreakTime=15, rounds=4):
        self.focusTime = focusTime
        self.breakTime = breakTime
        self.lbreakTime = lbreakTime
        self.rounds = rounds

    def printConfig(self):
        print(f'\tCurrent config of the session looks like:')
        print(f'\t - focus time = {self.focusTime}')
        print(f'\t - break time = {self.breakTime}')
        print(f'\t - long break time = {self.lbreakTime}')
        print(f'\t - rounds = {self.rounds}')

def greetings(currentSession):
    print('Hello, User!')
    print('Initializing session', end='', flush=True)
    for _ in range(3):
        time.sleep(1)
        print(' .', end='', flush=True)
    else:
        time.sleep(1)
        print()
    currentSession.printConfig()

def main():
    currentSession = Session()
    greetings(currentSession)
    

if __name__ == '__main__':
    main()
    
