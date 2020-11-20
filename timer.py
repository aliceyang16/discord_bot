# Pomodoro Timer Class
import time

class PomodoroTimer:
	def __init__(self, time):
		self.time = time * 60

	def setTimer(self, time):
		self.time = time * 60

	def startTimer(self):
		while self.time:
			mins, secs = divmod(self.time, 60)
			timer = '{:02d}:{:02d}'.format(mins, secs)
			print(timer, end='\r')
			time.sleep(1)
			self.time -= 1
		print("ALL DONE")
		return "TIME'S UP!"

# session = PomodoroTimer(5)
# session.startTimer()
