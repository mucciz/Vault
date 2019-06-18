import unittest # Importing the unittest module
from password import User # Importing the user class
from credentials import Credentials


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('1234','cartelo','kimonyoski') #create a new user object
