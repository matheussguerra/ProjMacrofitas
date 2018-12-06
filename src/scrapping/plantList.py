 # -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector

import requests
import csv
import os

urlSearchTemplate = "http://www.theplantlist.org/tpl1.1/search?q={}"
newUrl = "http://www.theplantlist.org{}"

def getOneEntry(searchTerm):
    searchTerm = searchTerm.replace('\n', '')
    response = requests.get(urlSearchTemplate.format(searchTerm.replace(' ', '%20')))

    if response.ok:
        http_encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
        html_encoding = EncodingDetector.find_declared_encoding(response.content, is_html=True)
        encoding = html_encoding or http_encoding
        soup = BeautifulSoup(response.content, 'lxml', from_encoding=encoding)

        result = processHtml(soup, searchTerm)

        if ("/tpl" in result[0]):
           result = getOneEntry2(result[1], result[0])

        resultSplited = result.split(',')
        if len(resultSplited) == 3:
            resultSplited = [i.decode('utf-8').strip() for i in resultSplited]
            nome = resultSplited[0]
            status = resultSplited[1]
            nome_aceito = resultSplited[1]
            return nome, status, nome_aceito
        else:
            return '', '', ''

    else:
        return 'Bad Response!'

def getOneEntry2(searchTerm, searchTermAbsolute):
    response = requests.get(newUrl.format(searchTermAbsolute.replace(' ', '%20')))

    if response.ok:
        http_encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
        html_encoding = EncodingDetector.find_declared_encoding(response.content, is_html=True)
        encoding = html_encoding or http_encoding
        soup = BeautifulSoup(response.content, 'lxml', from_encoding=encoding)

        result = processHtml(soup, searchTerm)
        return result

    else:
        return 'Bad Response!'


def getAllEntries(inputPath = os.path.join('data','ListaMacrofitasResult.csv')):
    with open(inputPath) as input:
        lines = input.readlines()

    for line in lines:
        searchTerm = line.split(',')[0]
        getOneEntry(searchTerm)

    input.close()


def processHtml(soup, line):
    title = str(soup('title')[0])
    result = ""

    if "No results" in title:
        result = line + ' not found.\n'
        output = open(os.path.join('data','notFoundPlantList.csv'), 'a')
        output.write(result)
        output.close()
        result = 'none'

    elif "Search results" in title:
        identifier,genus,species = getCorrectLink(soup)

        if identifier != 'none':
            result = identifier, (genus + ' ' + species)
            #file = open('toProcess.txt', 'a')
            #file.write(identifier + ',' + genus + ' ' + species + '\n')
            #file.close()
        else:
            result = line + ' not accepted names.' '\n'
            output = open(os.path.join('data','notFoundPlantList.csv'), 'a')
            output.write(result)
            output.close()
            result = 'none'

    else:
        status = verifyStatus(soup)

        if status == 'SINONIMO':
            synonymous = getSynonymous(soup)
            result = line + ',' + status + ',' + synonymous
            result = result.replace('\n', '')

        elif status == 'NOME_ACEITO':
            result = line + ',' + status + ',' + line
            result = result.replace('\n', '')

        else:
            result = line + ',' + status

        output = open(os.path.join('data','plantList.csv'), 'a')
        output.write(result + '\n')
        output.close()

    return result



def getCorrectLink(soup):
    table = soup('table')
    trs = table[0]('tr')
    identifier = 'none'
    for tr in trs[1:]:
        genus = str(tr('td')[0]('span')[0]('i')[0].text.encode('utf-8'))
        species = str(tr('td')[0]('span')[0]('i')[1].text.encode('utf-8'))
        #author = str(tr('td')[0]('span')[1].text.encode('utf-8'))
        status = str(tr('td')[1].text.encode('utf-8'))


        if status == "Accepted":
            identifier = tr.find('a', href = True)
            identifier = identifier['href']
            break
        else:
            identifier = 'none'

    return identifier,genus,species

def verifyStatus(soup):
    tag_h1 =  soup('h1')[1]('span')[3]('a')[0]
    status = tag_h1['href']

    if 'accepted' in status:
        return 'NOME_ACEITO'
    elif 'synonym' in status:
        return 'SINONIMO'
    elif 'unresolved' in status:
        return 'UNRESOLVED'


def getSynonymous(soup):
    genus = soup('h1')[1]('span')[3]('i')[0].text
    species = soup('h1')[1]('span')[3]('i')[1].text
    return str(genus) + ' ' + str(species)

def main():
    getAllEntries()
    #getOneEntry('Dicliptera ciliaris')


if __name__ == '__main__':
    main()