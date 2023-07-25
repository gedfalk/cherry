# ...

import time
import configparser

def readConfig(configFile):
    conf = configparser.ConfigParser()
    conf.read(configFile)

    activeTimer = conf['activeTimer']['name']
    focusTime = int(conf[activeTimer]['focusTime'])
    breakTime = int(conf[activeTimer]['breakTime'])
    lbreakTime = int(conf[activeTimer]['lbreakTime'])
    rounds = int(conf[activeTimer]['rounds'])

    return focusTime, breakTime, lbreakTime, rounds

def writeConfig(configFile, timer_settings: tuple):
    conf = configparser.ConfigParser()
    conf.read(configFile)
    
    timerLabel = 'customTimer' + ''.join([f'{i:02}' for i in timer_settings])
    if timerLabel not in conf:
        frequency = 1
    else:
        frequency = int(conf[timerLabel]['frequency']) + 1
    conf[timerLabel] = {}
    
    ft, bt, *dummy = timer_settings
    r, lbt = None, None
    conf[timerLabel]['focustime'] = str(ft)
    conf[timerLabel]['breaktime'] = str(bt)
    if len(timer_settings) > 2:
        r = timer_settings[2]
        conf[timerLabel]['rounds'] = str(r)
    if len(timer_settings) == 4:
        lbt = timer_settings[3]
        conf[timerLabel]['lbreaktime'] = str(lbt)
    conf[timerLabel]['frequency'] = str(frequency)

    # TODO:
    # Need to change [activeTimer] to either last used timer or most frequent

    with open(configFile, 'w') as configWrite:
        conf.write(configWrite)

    return ft, bt, r, lbt




class CherrySession():
    def __init__(self, timer_settings = None):
        
        if not timer_settings:
            # Need to change path to absolute?
            ft, bt, lbt, r = readConfig('cherryCore/cherry.conf')
        else:
            ft, bt, r, lbt = writeConfig('cherryCore/cherry.conf', timer_settings)
            
        self.focusTime = ft
        self.breakTime = bt
        self.rounds = r or 1
        self.lbreakTime = lbt


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
    currentSession = CherrySession()
    greetings(currentSession)
    

if __name__ == '__main__':
    main()
    
