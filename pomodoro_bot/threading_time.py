# Threading and Timer
import threading
import time

import vardata

def runTimer(thread, counter: int):
	while counter:
		if vardata.exit_flag:
			break
		time.sleep(1)
		print("%s: %s" %(thread.name, time.ctime(time.time())))
		counter -= 1

class FuncThread (threading.Thread):
	def __init__(self, name: str):
		threading.Thread.__init__(self)
		self.name = name
		self.productivity = 1500
		self.breakSession = 300

	def setProductivityTime(self, productivity: int) -> None:
		self.productivity = productivity * 60

	def setBreakTime(self, breakTime: int) -> None:
		self.breakSession = breakTime * 60

	def runProductivity(self) -> str:
		print("Running productivity session for " + self.name)
		runTimer(self, self.productivity)
		print("Exiting productivity session for " + self.name)
		return "Good work! Hope you were productive in the last " + str(int(self.productivity / 60)) + " minutes! :grinning:"
	
	def runBreak(self):
		print("Running break session for " + self.name)
		runTimer(self, self.breakSession)
		print("Exiting break session for " + self.name)
		#return "Hope you had a good " + str(int(self.breakSession / 60)) + " minutes break! :zany_face:"

	def run(self):
		self.runProductivity()
		self.runBreak()


# -------- testing --------------
# thread1 = FuncThread("thread1")
# thread1.setProductivityTime(5)
# thread1.setBreakTime(2)
# thread1.start()
# time.sleep(2)
# exit_flag = True