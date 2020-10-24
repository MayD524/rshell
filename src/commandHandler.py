from errorHandler import errorHandler
import aliasHandler as AH
import system
import commands
import filemgr
import env

import json

commandPair = {
	0 : 0,                  ## help
	1 : commands.changeDir, ## cd
	2 : commands.ls,        ## ls
	3 : filemgr.makeDir,    ## mkdir
	4 : filemgr.removeFile, ## rm
	5 : commands.cwd,       ## cwd
	6 : filemgr.reader,     ## file reading
	7 : filemgr.writer,     ## file writing
	8 : filemgr.makeFile,   ## file creation
	9 : filemgr.rmdir,      ## remove dir
	10: AH.aliases,         ## make new aliase or view
	11: env.envCore,	    ## make new env var	
	12: commands.RUN,	    ## run command
	13: system.getProc      ## get processes
}

class commandHandler:
	def __init__(self, command=None, cmdArgs=None):
		self.command = command
		self.cmdArgs = cmdArgs

		self.getAlias()

	def getAlias(self):
		with open("C:/rshell/src/json/alias.json", "r") as aliasReader:
			self.aliases = json.load(aliasReader)

	def execute(self, commandID=0, argState=0):
		if commandID in commandPair.keys():
			if self.cmdArgs == None and argState == 0:
				commandPair[commandID]()

			elif self.cmdArgs != None and argState == 1:
				commandPair[commandID](self.cmdArgs)

			elif argState == 3 and self.cmdArgs == None or self.cmdArgs != None:
				commandPair[commandID](self.cmdArgs)
			elif argState == 4 and self.cmdArgs == None or self.cmdArgs != None:
				commandPair[commandID](self.cmdArgs)
			elif argState == 1 and self.cmdArgs == None:
				errorHandler(102, command=self.command)

			else:
				return 0

		else:
			errorHandler(101, command=self.command)

	def preRunner(self):
		self.command = self.command.lower()
		if self.command.startswith("$"):
			tmp = env.getVars()
			self.command = self.command.replace("$", "")
			if self.command in tmp.keys():
				env.envExe(self.command)
			elif self.command != None:
				if self.cmdArgs == None:
					env.makeEnv(tag=self.command)
				else:
					env.makeEnv(tag=self.command,value=self.cmdArgs[0])

			return



		if self.command in self.aliases.keys():
			cmdDetails = self.aliases[self.command]

			if cmdDetails[0] == 0 and self.cmdArgs == None: ## takes no args
				self.execute(commandID=cmdDetails[1])

			elif cmdDetails[0] != 0: ## requires args
				self.execute(commandID=cmdDetails[1],argState=cmdDetails[0])
		elif self.command not in self.aliases.keys():
			try:
				commands.RUN()
			except Exception as e:
				pass
		else:
			errorHandler(101,command=self.command)