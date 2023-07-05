# ...

from cherryCore.timer import Timer
from cherryCore.mode import Mode


def main():
    # input args
    args = [1, 2, 3]
    currentMode = Mode(args)

    timer = Timer(currentMode)
    timer.run()
    pass


if __name__ == '__main__':
    main()

