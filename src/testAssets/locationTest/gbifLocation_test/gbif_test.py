# encoding: utf-8
import json
import unittest
import sys
sys.path.insert(0, "/home/suporte/ProjMacrofitas/src/location")
from gbif import getLocation, parseResult

class TestGbifInvalid(unittest.TestCase):
    def setUp(self):
        outputFile = open('outputGbif.txt', 'w')

    def test_parseDataValid(self):
        getLocation('Invalid Name', 'outputGbif.txt')
        output = open('outputGbif.txt', 'r')
        outputContent = output.readlines()
        self.assertEqual(len(outputContent), 0)

class TestGbifValid(unittest.TestCase):
    def setUp(self):
        outputFile = open('outputGbif.txt', 'w')
        mockFile = open('outputGbif.txt', 'w')
        mockFile.write("{\"installationKey\":\"b38ff2b7c8af454eb5afee760f0d5bca\",\"protocol\":\"DWC_ARCHIVE\",\"taxonKey\":7685550,\"family\":\"Poaceae\",\"institutionCode\":\"Universidade Regional de Blumenau, FURB\",\"lastInterpreted\":\"2018-10-24T15:39:00.4290000\",\"municipality\":\"Ilhota\",\"speciesKey\":4125200,\"month\":8,\"identifiedBy\":\"Funez, L.A.\",\"lastParsed\":\"2018-10-24T15:38:18.7340000\",\"phylum\":\"Tracheophyta\",\"orderKey\":1369,\"year\":2017,\"facts\":[],\"taxonomicStatus\":\"SYNONYM\",\"species\":\"Panicum schwackeanum\",\"issues\":[\"COORDINATE_ROUNDED\",\"GEODETIC_DATUM_ASSUMED_WGS84\"],\"gbifID\":\"1658203036\",\"language\":\"pt\",\"acceptedScientificName\":\"Panicum schwackeanum Mez\",\"occurrenceID\":\"BRA:FURB:FURB:0000054617\",\"countryCode\":\"BR\",\"basisOfRecord\":\"PRESERVED_SPECIMEN\",\"recordNumber\":\"34\",\"stateProvince\":\"Santa Catarina\",\"relations\":[],\"eventDate\":\"2017-08-19T00:00:00.0000000\",\"type\":\"Collection\",\"classKey\":196,\"catalogNumber\":\"54617\",\"scientificName\":\"Trichanthecium schwackeanum (Mez) Zuloaga & Morrone\",\"taxonRank\":\"SPECIES\",\"familyKey\":3073,\"kingdom\":\"Plantae\",\"decimalLatitude\":-26.806944,\"rightsHolder\":\"FURB - Herbário Dr. Roberto Miguel Klein\",\"publishingOrgKey\":\"34e6e625-47cf-4d42-8054-af0c2f1b6e64\",\"geodeticDatum\":\"WGS84\",\"datasetName\":\"FURB - Herbario Dr. Roberto Miguel Klein\",\"kingdomKey\":6,\"collectionCode\":\"FURB\",\"lastCrawled\":\"2018-11-23T15:39:26.6810000\",\"class\":\"Liliopsida\",\"genusKey\":2705064,\"locality\":\"Morro do Bafa.\",\"key\":1658203036,\"acceptedTaxonKey\":4125200,\"phylumKey\":7707728,\"genericName\":\"Trichanthecium\",\"day\":19,\"crawlId\":121,\"publishingCountry\":\"BR\",\"identifier\":\"BRA:FURB:FURB:0000054617\",\"networkKeys\":[],\"license\":\"http://creativecommons.org/licenses/by-nc/4.0/legalcode\",\"datasetKey\":\"b9a43c60-d2b6-445c-9362-2db65465c963\",\"specificEpithet\":\"schwackeanum\",\"identifiers\":[],\"decimalLongitude\":-48.943333,\"extensions\":{},\"dateIdentified\":\"2017-08-25T00:00:00.0000000\",\"country\":\"Brazil\",\"recordedBy\":\"Farias, D.M.\",\"ownerInstitutionCode\":\"Universidade Regional de Blumenau, FURB\",\"genus\":\"Panicum\",\"order\":\"Poales\"}")

    def test_parseResult(self):
        inputMock = open('mock.txt', 'r')
        mock = inputMock.readlines()[0]
        mock = json.loads(mock, strict=False)
        (scientificName, municipality, state, country, latitude, longitude, date) = parseResult(mock, 'Trichanthecium schwackeanum')
        self.assertEqual((scientificName, municipality, state, country, latitude, longitude, date), ("Trichanthecium schwackeanum", "Ilhota", "Santa Catarina", "Brazil", -26.806944, -48.943333, "19/8/2017") )

if __name__ == "__main__":
    unittest.main()