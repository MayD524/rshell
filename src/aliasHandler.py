from prettytable import PrettyTable
from errorHandler import errorHandler as EH
import json
jsonFile = "C:/rshell/src/json/alias.json"

def getAlias():
	with open(jsonFile, "r") as jsonReader:
		return json.load(jsonReader)

def returnAlias(target=None):
	aliases = getAlias()
	table = PrettyTable()
	table.field_names = ["Alias", "Parameter Classification", "Command ID"]
	if target == None:
		for key in aliases.keys():
			table.add_row([key, aliases[key][0], aliases[key][1]])

		print(table)
	else:
		if target in aliases.keys():
			table.add_row([target, aliases[target][0], aliases[target][1]])
			print(table)
		else:
			EH(106, command=target)
			
def removeAlias(aliasTag=None):
	aliases = getAlias()
	forbiden = ["help", "cd", "" "ls", "mkdir", "rm", "cwd", "read", "write", "mkf", "rmdir", "aliase"]
	aliasTag = aliasTag.lower()
	if aliasTag != None:
		if aliasTag in aliases.keys() and aliasTag not in forbiden:
			del aliases[aliasTag]
			with open(jsonFile, 'w') as jsonWriter:
				json.dump(aliases, jsonWriter, indent=4)
		elif aliasTag in forbiden:
			print("Cannot remove core alias")
		else:
			print(f"'{aliasTag}' doesn't exist")
	else:
		EH(102, command="remove alias")

def makeAlias(aliasNumber=None, aliasCom=None,aliasTag=None):
	aliases = getAlias()
	
	if aliasNumber > 10 or aliasNumber < 0:
		return ## error

	if aliasCom > 3 or aliasCom < 0 or aliasCom == 2: ## remove 2 if 2 is ever used
		return ## error 

	aliases[aliasTag] = [aliasCom, aliasNumber]

	with open(jsonFile, "w") as jsonWriter:
		json.dump(aliases, jsonWriter, indent = 4)

def aliases(args=None):
	if args == None:
		returnAlias()

	elif "-a" in args[0] and "-t" in args[0] or "--target" in args[0]:
		args = args[0].replace("-a", '')

		if " " in args: args = args.replace(" ", "")

		if "=" in args:
			args = args.split("=")
			#print(args)
			returnAlias(args[1])

	elif "-r" in args[0]:
		args = args[0].replace("-r ", "")
		removeAlias(args)

	elif "-m" in args[0]:
		args = args[0].replace("-m", "")
		aliasName = str(input("Alias Name> "))
		aliasNum = int(input("Alias ParamState\n[0 - none, 1 - one input, 3 - no limit]\n> "))
		aliasCom = int(input("Alias ID[1-10]> "))

		makeAlias(aliasNumber=aliasCom, aliasCom=aliasNum, aliasTag=aliasName)
