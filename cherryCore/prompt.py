from rich.prompt import IntPrompt
from rich import print

class FocusPrompt(IntPrompt):
    validate_error_message = "[prompt.invalid]Please enter a number between 1 and 99"
class BreakPrompt(IntPrompt):
    validate_error_message = "[prompt.invalid]Please enter a number between 1 and 30"
class RoundsPrompt(IntPrompt):
    validate_error_message = "[prompt.invalid]Please enter a number between 1 and 12"
class LBreakPrompt(IntPrompt):
    validate_error_message = "[prompt.invalid]Please enter a number between 1 and 99"


class MyPrompt():
    def __init__(self):
        pass

    def if_default_is_given(self, value: int, default: int):
        if value == -1:
            print(f'  [bold green]Default:[/bold green] {default}')
            return default
        else:
            return value

    def run(self):
        focusTime = FocusPrompt.ask('set Focus Time', default=-1, show_default=False)
        self.focusTime = self.if_default_is_given(focusTime, 30)
        breakTime = BreakPrompt.ask('set Break Time', default=-1, show_default=False)
        self.breakTime = self.if_default_is_given(breakTime, 5)        
        rounds = RoundsPrompt.ask('set amount of Rounds', default=-1, show_default=False)
        self.rounds = self.if_default_is_given(rounds, 4)
        lbreakTime = LBreakPrompt.ask('set Long Break Time', default=-1, show_default=False)
        self.lbreakTime = self.if_default_is_given(lbreakTime, 20)

    def get_timer_settings(self):
        return (self.focusTime, self.breakTime, self.rounds, self.lbreakTime)
    
    def show_timer_settings(self):
        print(f'focusTime = {self.focusTime}')
        print(f'breakTime = {self.breakTime}')
        print(f'rounds = {self.rounds}')
        print(f'lbreakTime = {self.lbreakTime}')
