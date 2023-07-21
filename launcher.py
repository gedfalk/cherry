# ...

from cherryCore.timer import Timer
from cherryCore.mode import Mode

import click

@click.command()
@click.argument('timer_settings', type=int, nargs=-1)
def main(timer_settings):
    match len(timer_settings):
        case 0:
            pass
        case 2 | 3 | 4:
            click.echo(f'{timer_settings}')
        case _:
            click.echo(f'Error')
            return
    mode = Mode(1, 2, 3, 4)

    click.echo(f'something')

    timer = Timer(timer_settings, mode)
    timer.run()


if __name__ == '__main__':
    main()

