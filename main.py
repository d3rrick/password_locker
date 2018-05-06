#! python3
import sys
import time
import string
import random
from user import User
from credential import Credential

def screen(x):
	print("#"*50)
	print(""*2)
	print(x)
	print(""*2)
	print("#"*50)

def login():
	
	if User.users:
		uname = input("please enter your username : " )
		masterk = input("please enter your master password ")
		if User.users['username'] == uname and User.users['password'] == masterk:
			print(f"welcome {uname}")
			return True
		else:
			print("wrong password or username")
			print("in case you have forgotten, register again")
			print("choose an optioh here:\n 1)register\n 2)try again")
			data = int(input())
			if data == 1:
				register()
			elif data == 2:
				login()
			else:
				login()
	else:
		print("Currently there are no other users, please register")
		register()
		return True

def register():
	username = input("enter your username : ")
	master1 = input("enter a password of your choice : ")
	master2 = input("please enter your password again")
	if master1 == master2:
		User(username,master1)
		return True
	else:
		register()
		landing_section = True

def addAccount():
	acc = input("please enter your account name : ")
	usname = input("please enter your username : ")
	email = input("please enter your email : " )
	passw = int(input("how long would you like your password to be ? "))

	def generate_password(i):
		_all =  string.ascii_letters+ string.punctuation+string.digits
		return "".join(random.sample(_all,i))

	Credential(acc, usname,email,generate_password(passw))

def viewall():
	print(Credential.display_accounts())
def delete_account():
	Credential.delete_credential(input("what account do you want to delete ? "))

def search_account():
	acc = input("which account are you searching for ? ")
	screen(Credential.search_credential(acc))

def landing_section():
	selecting = True;
	while selecting:
		inp = int(input("1: login, 2: register, 3: Leave : "))
		if inp == 1:
			return login()
		elif inp == 2:
			return register()
		elif inp == 3:
			screen("Thanks for comming here, see you another time")
			screen(" application closing in 3 seconds")
			sys.exit(3)
		else:
			screen("invalid choice, please try again!")

def main():
	screen("hello and welcome to password locker")
	decided = landing_section()
	if decided:
		screen("you are now logged in to the password locker!")
		loggedin = True
		while loggedin:
			choice = int(input("1)create account\n2)view all accounts\n3)delete account\n4)search account\n5)logout "))
			if choice ==1:
				print("you want to create an account?")
				addAccount()
			elif choice ==2:
				print("view all the accounts")
				viewall()
			elif choice ==3:
				print("delete an account? ")
				delete_account()
			elif choice == 4:
				print("search an account ")
				search_account()
			elif choice == 5:
				print("logging out")
				loggedin = False
				print("bye, thanks for using this app. log in again to continue enjoying..")
		else:
			print("bye")
			sys.exit(3)

if __name__ == '__main__':
	main()