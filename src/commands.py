from errorHandler import errorHandler as EH
from prettytable import PrettyTable
import termcolor as tc
import os

def RUN(script=None, Args=None):
	os.system(f"{script}")

def cwd(state=0):
	
	if state != 0:
		return os.getcwd()
	else:
		print(os.getcwd())

def changeDir(path = None):
	if path != None:
		if os.path.exists(path[0]):
			os.chdir(path[0])

	else:
		EH(104, Dir=path[0])

def ls(args=None):
	configFiletypes = [".config", ".json", ".xml", ".yaml", ".dat"]
	def lsOut(dirList=None, types="ALL"):
		outDict = {}
		table = PrettyTable()
		for i in range(len(dirList)):
			item = dirList[i]
			if os.path.isdir(item) and types == "ALL" or types == "DIR" and not os.path.isfile(item):
				outDict[i] = ["d----", item, "DIR"]
			elif os.path.isfile(item) and types == "ALL" or types == "FILE" and not os.path.isdir(item):
				outDict[i] = ["-f---", item, str(os.path.getsize(item))]
				if item.endswith(".exe"):
					outDict[i][0] = "-fx--"
				elif item.endswith(".zip") or item.endswith(".rar"):
					outDict[i][0] = "df--a"
				elif item.endswith(".lnk"):
					outDict[i][0] = "-f-l-"
				else:
					for ext in range(len(configFiletypes)):
						if item.endswith(configFiletypes[ext]):
							outDict[i][0] = "-f-c-"

		table.field_names = [tc.colored("#","green"), tc.colored("Type","green") ,tc.colored("Name","green"),tc.colored("Size","green")]
		for key in outDict.keys():

			tmp = outDict[key]
			table.add_row([key, tmp[0], tc.colored(tmp[1], "green" if tmp[0] == "d----" else "cyan"), tmp[2]])

		print(table)
	
	dirList = os.listdir()
	types = "ALL"
	
	if type(args) == list and len(args) > 0 and args[0].startswith("type"):
		if " " in args[0]:
			arg = args[0].replace(" ","")
			arg = arg.split("=")

		else:
			arg = args[0].split("=")

		if arg[1].lower() == "file":
			types = "FILE"

		elif arg[1].lower() == "dir":
			types = "DIR"

	lsOut(dirList=dirList, types=types)