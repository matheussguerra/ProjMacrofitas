# encoding: utf-8
import sys
sys.path.insert(0, '/home/yudi/ProjMacrofitas/src/scrapping')
from floraDoBrasil import getData
import unittest

class TestDataGatheringMethods(unittest.TestCase):
    def setUp(self):
        inputFile = open('input_test.txt', 'w')
        inputFile.write('Dicliptera ciliaris\n')

    def test_getData(self):
        getData(allDataset=True, inputFile='input_test.txt', outputPath='output_test.txt')
        output = open('output_test.txt', 'r')
        outputLine = output.readline()
        status = outputLine.split(',')[1]
        self.assertEqual(status,'NOME_ACEITO')


class TestDataGatheringMethodsSynonymous(unittest.TestCase):
    def setUp(self):
        inputFile = open('input_test.txt', 'w')
        outputFile = open('output_test.txt', 'w')
        inputFile.write('Chenopodium ambrosioides\n')

    def test_getData(self):
        getData(allDataset=True, inputFile='input_test.txt', outputPath='output_test.txt', notFoundPath='notFound.txt')
        output = open('output_test.txt', 'r')
        outputLine = output.readline()
        status = outputLine.split(',')[1]
        self.assertEqual(status, 'SINONIMO')


class TestDataGatheringMethodsInvalidName(unittest.TestCase):
    def setUp(self):
        inputFile = open('input_test.txt', 'w')
        outputFile = open('output_test.txt', 'w')
        notFoundFile = open('notFound.txt', 'w')
        inputFile.write('Random Name\n')

    def test_getData(self):
        getData(allDataset=True, inputFile='input_test.txt', outputPath='output_test.txt', notFoundPath='notFound.txt')
        output = open('output_test.txt', 'r')
        outputLine = output.readline()
        outputLenght = len(outputLine)
        self.assertEqual(outputLenght, 0)

if __name__ == "__main__":
    unittest.main()