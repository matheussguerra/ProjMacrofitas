from BeautifulSoup import BeautifulSoup
import unittest
import requests

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from scrapping.plantList import getData
from scrapping.plantList import verifyAccepted
from scrapping.plantList import getSynonymous

class TestPlantList(unittest.TestCase):

	def setUp(self):
		self.valid_query = self.get_soup("Eclipta megapotamica")
		self.invalid_query = self.get_soup("Eucaliptus")

	def get_soup(self, searchTerm):
		response = requests.get('http://www.theplantlist.org/tpl1.1/search?q=' + searchTerm)
		raw_http = response.text

		raw_http = response.text
		soup = BeautifulSoup(raw_http)

		return soup
	
	def test_verifyAccepted(self):
		self.assertTrue(verifyAccepted(self.valid_query))
		self.assertFalse(verifyAccepted(self.invalid_query))

	def test_getSynonymous(self):
		self.assertTrue(getSynonymous(self.valid_query))
		self.assertFalse(getSynonymous(self.invalid_query))
		



if __name__ == '__main__':
	unittest.main()