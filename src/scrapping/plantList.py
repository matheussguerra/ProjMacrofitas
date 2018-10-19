from BeautifulSoup import BeautifulSoup
import requests
import csv

urlSearchTemplate = "http://www.theplantlist.org/tpl1.1/search?q={}"

def getOneEntry(searchTerm):
    response = requests.get(urlSearchTemplate.format(searchTerm))
    raw_http = response.text

    if response.ok:
        raw_http = response.text
        soup = BeautifulSoup(raw_http)

        isAccepted = verifyAccepted(soup)
        synonymous = getSynonymous(soup)

        return isAccepted, synonymous
    else:
        return 'Bad Response!'

def getAllEntries(inputPath='../data/ListaMacrofitasResult.csv', outputPath='../data/plantList.csv', notFoundPath = '../data/notFoundPlantList.csv'):
    outputFile = open(outputPath, 'a')
    output = csv.writer(outputFile)
    allResponses = []
    with open(inputPath) as input:
        lines = input.readlines()

        for line in lines:
            response = requests.get(urlSearchTemplate.format(line))

            if response.ok:
                raw_http = response.text
                soup = BeautifulSoup(raw_http)

                isAccepted = verifyAccepted(soup)
                synonymous = getSynonymous(soup)

                status = 'NOME_ACEITO' if isAccepted else 'SINONIMO'

                if not synonymous:
                    with open(notFoundPath, 'a') as notFound:
                        notFound.write('{} not found.\n'.format(line.replace('\n', '')))
                        continue

                output.writerow((line.replace('\n', ''),status, synonymous[0]['genus'] + ' ' + synonymous[0]['species'],synonymous[0]['status']))


def verifyAccepted(soup):
    firstTableRow = soup('tbody')[0]
    firstRow = firstTableRow('tr')[0]
    print firstRow.text
    print '--------------------------------------------------'
    return True if 'Accepted' in firstRow.text else False

def getSynonymous(soup):
    title = str(soup('title')[0])

    if("No results" in title):
        return False

    table = soup('table')
    trs = table[0]('tr')
    synonymous = []
    for tr in trs[1:]:
        data = {
            'genus' : str(tr('td')[0]('span')[0]('i')[0].text.encode('utf-8')),
            'species' : str(tr('td')[0]('span')[0]('i')[1].text.encode('utf-8')),
            'status' : str(tr('td')[1].text.encode('utf-8')),
        }
        synonymous.append(data)
    return synonymous

def main():
    getAllEntries()

if __name__ == '__main__':
    main()