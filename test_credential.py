import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
	def setUp(self):
		"""this method runs before each test"""
		self.c= Credential("github", "muriithiderro","muriithiderro@gmail.com","hhrh4ui4jr")
		self.newlist = []
		self.newlist.append(self.c)
	def test_init(self):
		"""this method checks whether instantiation is correctly done"""

		self.assertEqual(self.c.account, 'github')
		self.assertEqual(self.c.username, 'muriithiderro')
		self.assertEqual(self.c.email, 'muriithiderro@gmail.com')
		self.assertEqual(self.c.password, 'hhrh4ui4jr')
	
	def test_number_of_credential(self):
		"""this methods searches for the number of credentials for a given user"""
		print(self.newlist)
		self.assertEqual(len(self.newlist),1)
		
	def test_search_for_credentials(self):
		"""this method checks whether the searched account matches to any account in the system"""
		test_credential = Credential("github", "muriithiderro","muriithiderro@gmail.com","hhrh4ui4jr")
		found_credential = Credential("github", "muriithiderro","muriithiderro@gmail.com","hhrh4ui4jr")
		self.assertEqual(found_credential.account, "github")









if __name__ == '__main__':
	unittest.main()