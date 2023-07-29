from rich.prompt import IntPrompt

class MyPrompt():
    def __init__(self):
        pass

    def run(self):
        focusTime = IntPrompt.ask('set Focus Time')
        print(focusTime)
        breakTime = IntPrompt.ask('set Break Time')
        round = IntPrompt.ask('set amount of Rounds')
        breakTime = IntPrompt.ask('set Long Break Time')
