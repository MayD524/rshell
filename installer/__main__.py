
from subprocess import check_output, check_call
import sys
import os


newDir = "C:/rshell"
cmd = "git clone https://github.com/RyanD524/rshell.git C:/rshell"

def install(package):
    check_call([sys.executable, "-m", "pip", "install", package])
def main():
	if not os.path.exists(newDir):
		os.mkdir(newDir)

	check_output(cmd, shell=True).decode()
	install("termcolor")
	install("prettytable")



if __name__ == "__main__":
	main()