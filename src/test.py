import unittest

try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import patch

from scrapping.plantList import plantList
from scrapping.floraDoBrasil import floraDoBrasil

class TestPlantList(unittest.TestCase):

	def test_plantList(self):
		pass


if __name__ == '__main__':
	unittest.main()