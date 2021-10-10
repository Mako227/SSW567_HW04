"""
   File Name:    Test_HW04.py
   Author:       Alan Clark
   Date:         9 Oct 2021
   Description:  Modified for HW05a -- test get_github_commits function while mocking its service request
"""

import unittest
# Determined by trial and error that I needed some of these
import unittest.mock
from unittest.mock import patch
from requests import Response
from unittest.mock import Mock
#import json

from HW04_Alan_Clark_mod import get_github_commits

# This code implements the unit test functionality

class Test_HW04(unittest.TestCase):
    """ Class for testing the one and only function in HW04 """

    # Test 1
    @patch('requests.get')
    def testSSW567_HW02(self, mockedReq):
        mockedReq.return_value = Response('[{"sha":1},{"sha":2},{"sha":3},{"sha":4},{"sha":5},{"sha":6}]')
        commits = get_github_commits('Mako227', 'SSW567_HW02')
        self.assertEqual(commits, 6)

    # Test 2
    @patch('requests.get')
    def testSSW567_HW03(self, mockedReq):
        mockedReq.return_value = Response('[{"sha":1},{"sha":2},{"sha":3},{"sha":4}]')
        commits = get_github_commits('Mako227', 'SSW567_HW03')
        self.assertEqual(commits, 4)

# This runs all the test case functions from the classes in this file.
if __name__ == '__main__':
    print('Running unit tests\n')
    unittest.main()
