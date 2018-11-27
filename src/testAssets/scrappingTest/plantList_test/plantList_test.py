# encoding: utf-8
import sys
sys.path.insert(0, '/home/guerra/Área de trabalho/UTFPR/Eng2/src/scrapping')
from plantList import getAllEntries
import unittest

class TestDataGatheringMethods(unittest.TestCase):
	def setUp(self):
		inputFile = open('input_test.txt', 'w')
		inputFile.write('Dyschoriste maranhois\n')


	def test_getAllEntries(self):
		getAllEntries(inputPath='input_test.txt', outputPath='output_test.txt', notFoundPath='notFound_test.txt')
		output = open('output_test.txt', 'r')
		outputLine = output.readline()
		print 'aaa ' + outputLine
		status = outputLine.split(',')[1]
		self.assertEqual(status,'NOME_ACEITO')





if __name__ == "__main__":
	unittest.main()