import time


class PomodoroTimer:
    def __init__(self, time: int):
        # default 25 minutes working session and 5 minutes break
        self.time = 1500
        self.breakTime = 300

    def setWorkTimer(self, time: int):
        self.time = time * 60

    def setBreakTimer(self, time: int):
        self.breakTime = time * 60

    def startWorkTimer(self) -> str:
        self.startTimer(self.time)
        message = (
            "Good work! Hope you were productive in the last "
            + str(int(self.time / 60))
            + " minutes! :grinning:"
        )
        return message

    def startBreakTimer(self) -> str:
        self.startTimer(self.breakTime)
        message = (
            "Hope you had a good "
            + str(int(self.breakTime / 60))
            + " minutes break! :zany_face:"
        )
        return message

    def startTimer(self, t) -> None:
        while t:
            mins, secs = divmod(t, 60)
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print("ALL DONE")
