from prettytable import PrettyTable
from errorHandler import errorHandler
import psutil
import math

def calc(equa=None):
	if equa != None:
		print(eval(equa[0]))
	else:
		errorHandler(102, "calc")

def getProc():
	table = PrettyTable()
	table.field_names = ["#", "Name", "PID"]
	i = 0
	# Iterate over all running process
	for proc in psutil.process_iter():
	    try:
	        # Get process name & pid from process object.
	        processName = proc.name()
	        processID = proc.pid
	        table.add_row([i, processName, processID])

	    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
	        pass

	    i += 1

	print(table)