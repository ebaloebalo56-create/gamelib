import time

class Timer:
    def __init__(self, seconds, action):
        self.seconds = seconds
        self.action = action
    def countdowntimer(self):
        while self.seconds > 0:
            time.sleep(1)
            self.seconds -= 1
        return self.action