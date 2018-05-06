import unittest
from user import User

class TestUser(unittest.TestCase):

	@classmethod
	def SetupUserClass(cls):
		"""This method is a life cycle hook for this class"""
		print("setup class")

	@classmethod
	"""this method is executed after each test"""
	def tearDownClass(cls):
		print("teardown class")

	def setUp(self):
		self.user1 = User("admin", "12345")
		self.user2 = User('new',"12345")
		
	"""
	This method sets up the data needed to test User class"""
	
	def test_instanciation(self):
		"""this method checks whether instances are created properly"""
		self.assertEqual(self.user1.username, 'admin')
		
	@classmethod
	def list_users(cls):
		print("hii")
		# cls.lis = []
		self.assertEqual(len(lis[cls.user1,cls.user2]),12)


if __name__ == '__main__':
	print("testing")
	unittest.main()