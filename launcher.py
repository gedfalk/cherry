# ...

from rich.console import Console
from cherryCore.timer import Timer


def main():
    console = Console()
    timer = Timer(console)
    timer.run()
    pass


if __name__ == '__main__':
    main()

