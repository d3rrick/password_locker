class User:
	counter = 0
	users = dict()
	
	def __init__(self, username, masterkey):
		self.username = username
		self.masterkey = masterkey
		User.users = {"username":self.username,"password":self.masterkey}
		User.counter+=1

	@classmethod
	def number_of_users(cls):
		return f"there are(is) currently {cls} user(s)"
	@classmethod
	def list_users(cls):
		return cls.users
		
	def __repr__(self):
		return self

# u1 = User("derrick", '123')
# u2 = User("admin", "iu348f934jfinkj439","hhhh")
# if User.users['username'] and User.users['password']:
# 	print("ok")
# else:
# 	print("furious")
	
# for x in User.users.username:
# 	print(x.username)