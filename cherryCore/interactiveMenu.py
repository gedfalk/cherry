from rich.console import Console, Group
from rich.live import Live
from rich.text import Text
from readchar import readkey, key


def runInteractiveMenu():
    # console = Console()

    x_f = [30, (1, 99)]
    x_b = [5, (1, 99)]
    x_r = [4, (0, 12)]
    x_lb = [20, (0, 99)]
    xList = [x_f, x_b, x_r, x_lb]

    focusTime = Text(f'focusTime:\t{xList[0][0]}', style='bold blue')
    breakTime = Text(f'breakTime:\t{xList[1][0]}')
    rounds = Text(f'rounds:     \t{xList[2][0]}')
    lbreakTime = Text(f'lbreakTime:\t{xList[3][0]}')

    menu = Group(focusTime, breakTime, rounds, lbreakTime)
    menuList = [focusTime, breakTime, rounds, lbreakTime]

    currentOption = 0

    with Live(menu, refresh_per_second=10) as live:
        while True:
            for i in range(len(menuList)):
                if i == currentOption:
                    menuList[i].style = 'bold blue'
                else:
                    menuList[i].style = 'white'

            k = readkey()
            if k == 'q':
                return None
            elif k == key.ENTER:
                xList = [xList[i][0] for i in range(len(xList))]
                live.update('')
                return xList
            elif k == key.DOWN or k == 'k':
                currentOption = (currentOption + 1) % len(menuList)
            elif k == key.UP or k == 'i':
                currentOption = (currentOption - 1) % len(menuList)
            elif k == key.LEFT or k == 'j':
                _min, _max = xList[currentOption][1]
                if xList[currentOption][0] > _min:
                    xList[currentOption][0] -= 1
                    menuList[currentOption]._text[0] = \
                        menuList[currentOption]._text[0].split('\t')[0] + \
                        f'\t{xList[currentOption][0]}'
            elif k == key.RIGHT or k == 'l':
                _min, _max = xList[currentOption][1]
                if xList[currentOption][0] < _max:
                    xList[currentOption][0] += 1
                    menuList[currentOption]._text[0] = \
                        menuList[currentOption]._text[0].split('\t')[0] + \
                        f'\t{xList[currentOption][0]}'
    
     

if __name__ == '__main__':
    res = runInteractiveMenu()
    print(res)
