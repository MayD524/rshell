from errorHandler import errorHandler
import os

def writer(args=None):
	if args != None:
		args = args[0].split(" ",1)
		if os.path.exists(args[0]):
			with open(args[0], "w+") as writer:
				writer.write(args[1])
		else:
			errorHandler(105)
	else:
		errorHandler(102, "writer")

def makeDir(directory=None):
	if directory != None:
		if os.path.exists(directory[0]):
			errorHandler(106)

		elif not os.path.exists(directory[0]):
			cwd = os.getcwd()
			path = os.path.join(cwd, directory[0])
			os.mkdir(path)
	else:
		errorHandler(102, "mkdir")

def rmdir(directory=None):
	if directory != None:
		if os.path.exists(directory[0]):
			os.rmdir(directory[0])
		else:
			errorHandler(3)
	else:
		errorHandler(102, "rmdir")

def removeFile(filename=None):
	if os.path.exists(filename[0]):
		os.remove(filename[0])
	else:
		errorHandler(102, "remove file")


def makeFile(filename=None):
	if filename != None:
		if os.path.exists(filename[0]):
			errorHandler(1)

		else:
			with open(filename[0], "w+"): pass
	else:
		errorHandler(102, "mkf")

def reader(filename=None, args=None):
	if filename != None:
		if os.path.exists(filename[0]):
			with open(filename[0], "r") as reader:

				if args != None:
					if args[0] == "print":
						print(reader.read())
					elif "=" in args[0]:
						arg = args[0].split("=")
						if arg[0] == "write":
							writer(arg[1],reader.read())

				elif args == None:
					print(reader.read())

		else:
			errorHandler(102, command="reader")
	else:
		errorHandler(105)