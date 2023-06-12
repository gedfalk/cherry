# DELETE this
# just demo of Rich and readchar libraries together

from rich.console import Console
from readchar import readkey, key

def main():
    console = Console()

    menu = ['Start', 'Pause', 'Refresh', 'Exit']
    currentOption = 0

    while True:
        console.clear()
        
        for i, option in enumerate(menu):
            if currentOption == i:
                console.print(f'[green]{option}[/green]')
            else:
                console.print(f'{option}')

        k = readkey()
        if k == key.DOWN:
            currentOption = (currentOption + 1) % len(menu)
        elif k == key.UP:
            currentOption = (currentOption - 1) % len(menu)
        elif k == key.ENTER and currentOption == 3:
            break
     

if __name__ == '__main__':
    main()
