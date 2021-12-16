import unittest
from Yad import *
import time

folder = 'new_folder_test'

class Test_YaD(unittest.TestCase):

    def test_create_folder(self):
        self.assertEqual(create_folder(folder=folder), 201)
        time.sleep(1)
        self.assertEqual(create_folder(folder=folder), 409)
        