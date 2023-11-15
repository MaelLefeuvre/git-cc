import os, random, time
import numpy as np

class WorkSimulator(object):
    """
    Mock random shell commands (just as if you were working on your thesis project!)

    """
    def __init__(self, history_path="~/.bash_history"):
        """
        Basic constructor for WorkSimulator

        Keyword arguments:
        history_path -- a directory leading to a file containing random command
                        line arguments, such as the user's bash_history.
                        (default "$HOME/.bash_history")

        Return: WorkSimulator
        """
        self.history_path = os.path.expanduser(history_path)
        self.commands     = self.__dump_history()
        self.len          = len(self.commands)

    def open_history(self, mode="r"):
        return open(self.history_path, mode, encoding="utf8", errors='ignore')
    
    def update_history(self):
        self.commands = self.__dump_history()

    def stall_randomly(self, mean=0.0, sigma=1.0):
        """
        Wait for an interval that is randomly sampled from a lognormal distribution
        """
        time.sleep(np.random.lognormal(mean, sigma, size=None))  # Fixed with love, xoxo, UserLambda

    def fake_work(self):
        while True:
            print(self._random_command())
            self.stall_randomly()
            self.update_history()


    def __dump_history(self):
        with self.open_history() as history:
            return [command.strip() for command in history]

    def _random_command(self):
        return self.commands[random.randrange(self.len)]

