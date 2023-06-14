# DELETE this
# just demo of Rich and readchar libraries together

from rich.console import Console
from readchar import readkey, key
from time import sleep

def main():
    console = Console(width=50)

    menu = ['Start', 'Pause', 'Refresh', 'Exit']
    currentOption = 0

    while True:
        console.clear()
       
        console.rule(f'[bold blue]:cherries: Cherry')
        for i, option in enumerate(menu):
            if currentOption == i:
                console.print(f'[bold green]  {option}[/bold green]')
            else:
                console.print(f' {option}')
        console.rule()

        k = readkey()
        if k == key.DOWN or k == 'k':
            currentOption = (currentOption + 1) % len(menu)
        elif k == key.UP or k == 'i':
            currentOption = (currentOption - 1) % len(menu)
        elif (k == key.ENTER or k == key.SPACE) and currentOption == 3:
            console.clear()
            break

        
     

if __name__ == '__main__':
    main()
