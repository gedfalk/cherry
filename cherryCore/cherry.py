# ...

import time
import configparser

def readConfig(configFile):
    conf = configparser.ConfigParser()
    conf.read(configFile)

    activeTimer = conf['activeTimer']['name']
    focusTime = conf[activeTimer]['focusTime']
    breakTime = conf[activeTimer]['breakTime']
    lbreakTime = conf[activeTimer]['lbreakTime']
    rounds = conf[activeTimer]['rounds']

    return focusTime, breakTime, lbreakTime, rounds


class Session():
    def __init__(self):
        ft, bt, lbt, r = readConfig('cherry.conf')
        self.focusTime = ft
        self.breakTime = bt
        self.lbreakTime = lbt
        self.rounds = r

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
    
