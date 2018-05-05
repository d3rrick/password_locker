#! python3

def screen(x):
	print("#"*50)
	print(""*2)
	print(x)
	print(""*2)
	print("#"*50)

def landing():
	selecting = True:
	while selecting:
		input = int(input("1: login, 2: register, 3: Leave"))
		if input == 1:
			# enter your master key
			# forgotten? enter your email
		elif input == 2:
			# create a new user instance

def main():
	screen("hello and welcome to password locker")
	

if __name__ == '__main__':
	main()