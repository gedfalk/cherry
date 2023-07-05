# ...

from rich.console import Console
from cherryCore.timer import Timer
from cherryCore.mode import Mode


def main():
    # input args
    args = [1, 2, 3]

    mode = Mode(args)
    console = Console()
    timer = Timer(console)
    timer.run()
    pass


if __name__ == '__main__':
    main()

