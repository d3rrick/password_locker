import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

	@classmethod
	def setUpCredentials(cls):
		print("setupe begun")

	def SetUp(self):
		""" setup method rub before each testcase"""
		self.credential1 = Credential("github", "muriithiderro","muriithiderro@gmail.com","hhrh4ui4jr")
		self.credential2 =  Credential("facebook", "muriirro","muriithiderro@gmail.com","hhjeio9i")

	def bbbb(self):
		self.assertEqual(self.credential1.account, 'github')


if __name__ == '__main__':
	unittest.main()