import commandHandler as ch
from threading import Thread
import termcolor
import os

def commandParser(commandLine):

	if " " in commandLine:
		commandLine = commandLine.split(" ", 1)
		command = commandLine[0]
		commandArgs = commandLine[1:]
	else:
		command = commandLine
		commandArgs = None

	cmdh = ch.commandHandler(command, commandArgs)
	cmdh.preRunner()

def main():
	while True:
		command = input(termcolor.colored(f"{ch.commands.cwd(state=1)}> ", "green"))

		if command == "clear":
			os.system("cls" if os.name == 'nt' else 'clear')
		elif command == 'exit' or command == 'quit':
			break

		elif command != "":
			Thread(commandParser(command)).start()

if __name__ == "__main__":
	main()