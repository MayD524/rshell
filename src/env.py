from errorHandler import errorHandler
from prettytable import PrettyTable
import commands
import subprocess
import json
import os

jsonFile = "C:/rshell/src/env.json"
def getVars():
	with open(jsonFile, "r") as jsReader:
		return json.load(jsReader)
def saveVars(newVars):
	with open(jsonFile, "w") as jsWriter:
		json.dump(newVars, jsWriter, indent=4)

def envExe(com):
	Vars = getVars()
	tmp = Vars[com]

	if tmp[1] == "EXE" or tmp[1] == "PY":
		subprocess.call(tmp[0])
	elif tmp[1] == "DIR":
		os.chdir(tmp[0])

	elif tmp[1] == "VAR":
		print(tmp[0])

	elif tmp[1] == "FUNC":
		result = getattr(commands, tmp[0])()


def printEnv(target=None):
	env = getVars()
	table = PrettyTable()
	table.field_names = ["Name", "Value", "Type"]
	if target == None:
		for key in env.keys():
			table.add_row([key, env[key][0], env[key][1]])
	elif target != None and target in env.keys():
		table.add_row([target, env[target]])
	else:
		errorHandler(107, command=target)

	print(table)

def remove(tag=None):
	Vars = getVars()
	if tag != None and tag in Vars.keys():
		del(Vars[tag])
	else:
		errorHandler(102, "remove env")
	saveVars(Vars)

def makeEnv(tag=None, value=None):
	Vars = getVars()
	tmp = []	
	if tag == None:
		tag = str(input("Tag> "))
	if value == None:
		value = str(input("Value> "))
	if value.endswith("()"):
		value = value.replace("()","")
		if "-r=" in value:

			value = value.replace("-r=", "")
			value = getattr(commands, value)()
		else:
			tmp.extend([value, "FUNC"])
	if os.path.exists(value):
		if os.path.isfile(value):
			if value.endswith(".exe") or value.endswith(".bat"):
				tmp.extend([value, "EXE"])
			elif value.endswith(".py"):
				tmp.extend([value, "PY"])


		elif os.path.isdir(value):
			tmp.extend([value, "DIR"])
	else:
		tmp.extend([value, "VAR"])
		
	Vars[tag] = tmp
	saveVars(Vars)


def envCore(args=None):
	if args == None:
		printEnv()
	elif args != None:
		if "-t=" in args[0]:
			args[0] = args[0].replace("-t=", "")
			print(args)
			printEnv(args[0])
		elif "-m" in args[0]:
			makeEnv()
		elif "-d=" in args[0]:
			args[0] = args[0].replace("-d=", "")
			remove(args[0])

