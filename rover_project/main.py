from rover_project import controller

def display_welcome():
	filename = ""
	while len(filename) == 0:
		filename = input("Welcome to the Rover Challenge!\nPlease, enter the filename of the input file: ")
	return filename

def main():
	filename = display_welcome()
	ctrl = controller.Controller(filename)
	ctrl.run()

if __name__ == "__main__":
	try:
		main()

	except FileNotFoundError as file_error:
		print(file_error)

	except ValueError as value_error:
		print("Invalid input file:", value_error)