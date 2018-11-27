# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

import requests
import pandas as pd

urlSearchTemplate = "http://www.splink.org.br/mod_perl/searchHint?ts_genus={}&offset={}"

def toUnicode(s):
    if type(s) is unicode:
        return s
    elif type(s) is str:
        d = chardet.detect(s)
        (cs, conf) = (d['encoding'], d['confidence'])
        if conf > 0.80:
            try:
                return s.decode( cs, errors = 'replace' )
            except Exception as ex:
                pass
    # force and return only ascii subset
    return unicode(''.join( [ i if ord(i) < 128 else ' ' for i in s ]))

def getData(searchTerm, offset=0, inputFile='../data/ListaMacrofitasResult.csv'):

	print 'Searching {},offset = {}'.format(searchTerm, offset)
	response = requests.get(urlSearchTemplate.format(searchTerm, offset))

	registries = []
	not_found_registries = []

	if response.ok:
		# Fetch enconding used from source
		http_encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
		html_encoding = EncodingDetector.find_declared_encoding(response.content, is_html=True)
		encoding = html_encoding or http_encoding
		soup = BeautifulSoup(response.content, 'lxml', from_encoding=encoding)

		divs = soup.findAll("div", {"class":"record"})

		try:
			page_hint = soup.find("div", {"id":"div_hint_summary"})
		except:
			writeNotFoundOutput(searchTerm)
			return

		# If no results are found, write searchTerm to file
		if page_hint == None or "Nenhum registro encontrado" in page_hint.find("b").text:
			writeNotFoundOutput(searchTerm)
		else:
			hints = page_hint.findAll('ll')

			offset = int(hints[1].text)
			max_registries = int(hints[2].text)

			for div in divs[1:]:
				try:
					generic_name = div.find("span", {"class":"tGa"}).text.encode('utf8')
				except:
					generic_name = ''
				try:
					specie_name = div.find("span", {"class":"tEa"}).text.encode('utf8').strip()
				except:
					specie_name = ''
				try:
					credit = div.find("span", {"id":"credit"}).text.replace('&#169; ', '').encode('utf8').strip()
				except:
					credit = ''

				try:
					municipality = div.find("span", {"class":"lM"}).text.encode('utf8').strip()
				except:
					municipality = ''
				try:
					state = div.find("span", {"class":"lS"}).text.encode('utf8').strip()
				except:
					state = ''
				try:
					country = div.find("span", {"class":"lC"}).text.encode('utf8').strip()
				except:
					country = ''
				try:
					latitude = div.find("span", {"class":"lA"}).text.replace('[lat:', '').encode('utf8').strip()
				except:
					latitude = ''
				try:
					longitude = div.find("span", {"class":"lO"}).text.replace('long:', '').encode('utf8').strip()
				except:
					longitude = ''
				try:
					date = div.find("span", {"class":"cY"}).text.encode('utf8').strip()
				except:
					date = ''

				scientificName = "{} {}".format(generic_name.strip(), specie_name.strip())

				registries.append('{},{},{},{},{},{},{}'.format(scientificName, municipality, state, country, latitude, longitude, date))

			writeOutput(registries)

			if(offset < max_registries):
				getData(searchTerm, offset)

	else:
		response.raise_for_status()

def writeOutput(registries, outputPath='../data/speciesLink.csv', notFoundPath='../data/notFoundSPLK.csv'):
    try:
        outputLocation = open(outputPath, 'a')
    except:
        outputLocation = open(outputPath, 'w')

    for i in registries:
        outputLocation.write(i + "\n")

def writeNotFoundOutput(searchTerm, notFoundPath='../data/notFoundSPLK.csv'):
	try:
		outputLocation = open(notFoundPath, 'a')
	except:
		outputLocation = open(notFoundPath, 'w')

	outputLocation.write(searchTerm)

if __name__ == '__main__':
	with open('../data/floraDoBrasil.csv', 'r') as file:
		lines = file.readlines()

		for line in lines:
			plant = line.split(',') 
			if plant[1] == 'SINONIMO':
				getData(plant[2].strip())
			else:
				getData(plant[0].strip())