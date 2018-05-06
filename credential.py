import string
import random

class Credential:
	credential_list = []
	dots = "*"*70
	def __init__(self, account, username,email,password):
		self.account = account
		self.username = username
		self.email = email
		self.password = password
		Credential.credential_list.append({"account":self.account,"username":self.username,"email":self.email,"password":self.password})


	@classmethod
	def search_credential(cls,account):
		if cls.credential_list:
			for i in cls.credential_list:
				for k,v in i.items():
					if v == account:
						return f"{cls.dots} \n  || account name || username  || email  || password \n {cls.dots} \n  || {i['account']} ||  {i['username']} || {i['email']} || {i['password']}"
		else:
			print("credentials list is empty")
		
	@classmethod
	def display_accounts(cls):
		if cls.credential_list:
			print(f"{cls.dots} \n  ||    account name ||     username  ||    email  ||    password \n {cls.dots}")
			x = 1
			for i in cls.credential_list:
				print(f"\n {x} || {i['account']} ||  {i['username']} || {i['email']} || {i['password']}")
				x+=1
		else:
			print("no accounts yet")


	@classmethod
	def delete_credential(cls,account):
		if cls.credential_list:
			for x in cls.credential_list:
				if x['account'] == account:
					cls.credential_list.remove(x)

		else:
			print("there are no accounts yet")
	@classmethod
	def generate_password(cls, length):
		_all =  string.ascii_letters+ string.punctuation+string.digits
		print("".join(random.sample(_all,length)))


c = Credential("github", "muriithiderro","muriithiderro@gmail.com","hhrh4ui4jr")
c2 =  Credential("facebook", "muriirro","muriithiderro@gmail.com","hhjeio9i")

# print(Credential.credential_list)
# Credential.delete_credential('facebook')
# print(Credential.credential_list)
# Credential.display_accounts()
# Credential.display_accounts()
# Credential.delete_credential('facebook')
# Credential.display_accounts()