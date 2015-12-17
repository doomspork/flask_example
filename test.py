#!/usr/bin/env python

import unittest
from app import app
try:
    from unittest.mock import patch
except:
    from mock import patch

class TestApp(unittest.TestCase):
    """ Test the index """

    def setUp(self):
        self.app = app.test_client()

    def test_home_page_works(self):
        """ Test the index """
        request = self.app.get('/')
        self.assertTrue(request.data)
        self.assertEqual(request.status_code, 200)
        request.close()

    def test_404_page(self):
        """ Test 404 """
        request = self.app.get('/i-am-not-found/')
        self.assertEqual(request.status_code, 404)
        request.close()

    def test_robot_request(self):
        """ Test robots.txt """
        request = self.app.get('/robots.txt')
        self.assertTrue(request.data)
        self.assertEqual(request.status_code, 200)
        request.close()

if __name__ == '__main__':
    unittest.main()
