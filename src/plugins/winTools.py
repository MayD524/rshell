import win10toast

def notification(args=None):
	title = "Default"
	message = "Default"
	toaster = win10toast.ToastNotifier()
	args = args[0].split(" ", 1)
	if args != None:
		title = args[0]
		if len(args) > 1:
			message = args[1]

	toaster.show_toast(title, message)