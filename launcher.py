# ...

from cherryCore.timer import Timer
from cherryCore.mode import Mode
from cherryCore.prompt import MyPrompt
from cherryCore.interactiveMenu import runInteractiveMenu

import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-p', '--prompt', is_flag=True)
@click.option('-i', '--interactive', is_flag=True)
@click.argument('timer_settings', type=int, nargs=-1)
def main(timer_settings, prompt, interactive):
    '''
    \b
      Cherry is yet another Pomodoro timer app that helps you organize your
    work, stay focused and improve overall productivity.

    \b
          TIMER_SETTINGS
      Optional argument. A series of integers separated by spaces,
    representing the desired timer settings in the following order:
     - focus time: The length of the focused work interval in minutes
     - break time: The length of the short break interval in minutes
     - rounds: The number of work and break intervals to complete
    before triggering a long break
     - long break time: The length of the longer break interval in
    minutes
      If you decide to pass timer settings, then it is required to specify
    at least two values - focus time and break time. The 3rd and 4th
    values correspond to the amount of rounds and long break time
    respectively and may or may not be passed at will. Passing only one
    value or more than four will result in an error.
      If timer settings are not set manually, the default values will be
    applied.

    '''
    if prompt:
        p = MyPrompt()
        p.run()
        timer_settings = p.get_timer_settings()
    elif interactive:
        timer_settings = runInteractiveMenu()
    else:
        match len(timer_settings):
            case 0:
                pass
            case 2 | 3 | 4:
                click.echo(f'{timer_settings}')
            case _:
                click.echo(f'Error')
                return
    mode = Mode(1, 2, 3, 4)

    #click.echo(timer_settings)

    timer = Timer(timer_settings, mode)
    timer.run()


if __name__ == '__main__':
    main()

