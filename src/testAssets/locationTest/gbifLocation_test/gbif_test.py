# encoding: utf-8

import unittest
import sys
sys.path.insert("/home/yudi/ProjMacrofitas/src/location")
from gbif import getLocation

class TestGbifValid(unittest.TestCase):
    def setUp(self):
        pass

    def test_getGbifData(self):
        raise NotImplementedError


class TestGbifInvalid(unittest.TestCase):
    def setUp(self):
        pass

    def test_getGbifData(self):
        raise NotImplementedError

if __name__ == "__main__":
    unittest.main()