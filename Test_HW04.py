"""
   File Name:    Test_HW04.py
   Author:       Alan Clark
   Date:         9 Oct 2021
   Description:  Modified for HW05a -- test get_github_commits function while mocking all service requests
"""

import unittest
import unittest.mock

from HW04_Alan_Clark_mod import get_github_commits

# This code implements the unit test functionality

class Test_HW04(unittest.TestCase):
    """ Class for testing the one and only function in HW04 """

    # Test 1
    @mock.patch('requests.get')
        def testMako227(self, mockedReq):
            mockedReq.return_value = MockResponse('[{"sha":1},{"sha":2},{"sha":3},{"sha":4},{"sha":5},{"sha":6}]')
            commits = get_github_commits('Mako227', 'SSW567_HW02')
            self.assertEqual(commits, 13)

# This runs all the test case functions from the classes in this file.
if __name__ == '__main__':
    print('Running unit tests\n')
    unittest.main()
