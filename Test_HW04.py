"""
   File Name:    Test_HW04.py
   Author:       Alan Clark
   Date:         2 Oct 2021
   Description:  Test get_github_commits function
"""

import unittest

from HW04_Alan_Clark import get_github_commits

# This code implements the unit test functionality

class Test_HW04(unittest.TestCase):
    """ Class for testing the one and only function in HW04 """

    # Test 0
    def testRunTheFunction(self):
        """ No actual test -- just run the function twice for demonstration purposes """
        print('No actual test here, just two demonstration runs')
        get_github_commits('Mako227')
        get_github_commits('richkempinski')
        
    # Test 1
#    def testMako227(self): 
#        self.assertEqual(get_github_commits('Mako227'), """Repo: SSW567_HW02, Number of commits: 13\n
#Repo: SSW567_HW04, Number of commits: 2\n
#Repo: Student-Repository, Number of commits: 10""")


# This runs all the test case functions from the classes in this file.
if __name__ == '__main__':
    print('Running unit tests\n')
    unittest.main()
