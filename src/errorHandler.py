
def errorHandler(errorCode, **kwargs): ## takes (int) (dynamic(dict))
	"""
	errorCode = (int)
	returns exebit (0-4) - executes will run somethingelse
	if exebit == 0 continue as normal (very minor)
	if exebit == 4 exit program, major error
	if exebit == 1 push minor error
	2 and 3  try to continue program
	3 attempt clean up
	"""
	cmd = ""
	DIR = ""
	if "command" in kwargs.keys():
		cmd = kwargs["command"]
	
	elif "Dir" in kwargs.keys():
		DIR = kwargs["Dir"]

	errorCodes = {
		## non-issues
		1   : [0, f"File already exists."],
		2 	: [0, f"Directory already exists."],
		3   : [0, f"Directory doesn't exist."],
		## minor issues
		101 : [1, f"Command {cmd} not found."],
		102 : [1, f"Command {cmd} requires args."],
		104 : [1, f"Directory {DIR} does not exist."],
		105 : [1, f"File not found or is not a file."],
		106 : [1, f"Alias not found : {cmd}."],
		107 : [1, f"Env var not found : {cmd}."]
	}

	if errorCode in errorCodes.keys():
		errorDet = errorCodes[errorCode]
		if errorDet[0] > 1:
			raise Exception(errorDet[1])
		print(errorDet[1]) ## returns (str)
	else:
		raise Exception("Major error : Unhandled error")