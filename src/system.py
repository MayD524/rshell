from prettytable import PrettyTable
import psutil

def getProc(lookFor=None):
	table = PrettyTable()
	table.field_name = ["#", "Name", "PID"]
	i = 0
	# Iterate over all running process
	for proc in psutil.process_iter():
	    try:
	        # Get process name & pid from process object.
	        processName = proc.name()
	        processID = proc.pid
	        if lookFor == None:
	        	table.add_row([i, processName, processID])
	        elif lookFor != None and processName == lookFor[0] or processID == lookFor[0]:
	        	table.add_row([i], processName, processID)
	    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
	        pass

	    i += 1

	print(table)