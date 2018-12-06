#coding: utf-8
import requests
import os

def getLocation(sciName, outputPath=os.path.join('data','gbifLocations.csv'), writeOutputFlag=True):
    urlTemplate = 'http://api.gbif.org/v1/occurrence/search?scientificName={}&limit=200'
    response = requests.get(urlTemplate.format(sciName))
    response_json = response.json()["results"]
    resultsParsed = []
    outputPath404 = outputPath[:-4] + 'NotFound.csv'

    if len(response_json) == 0:
        writeOutput(outputPath404, sciName.rstrip())
        return 'Não Encontrado'

    scientificName, municipality, state, country, latitude, longitude, date= '', '', '', '', '', '', ''

    for result in response_json:
        try:
            scientificName, municipality, state, country, latitude, longitude, date = parseResult(result, sciName)
        except:
            pass

        oneResult = [scientificName, municipality, state, country, latitude, longitude, date]
        resultsParsed.append(oneResult)

        if writeOutputFlag:
            if scientificName == '' and municipality == '' and state == '' and country == '':
                return None
            writeOutput(outputPath, '{},{},{},{},{},{},{}'.format(scientificName.encode('utf-8'), municipality.encode('utf-8'), state.encode('utf-8'), country.encode('utf-8'), latitude, longitude, date))

    return resultsParsed

def parseResult(result, sciName):
    name_splited = result['scientificName'].encode('utf8').split()
    scientificName = "{} {}".format(name_splited[0], name_splited[1])

    municipality, state, country, latitude, longitude, date = "", "", "", "", "", ""
    if scientificName.rstrip().lower() == sciName.rstrip().lower():
        try:
            municipality =  result['municipality'].encode('utf-8')
        except:
            municipality = ''
        try:
            state = result['stateProvince'].encode('utf-8')
        except:
            state = ''

        try:
            country = result['country'].encode('utf-8')
        except:
            country = ''
        try:
            latitude = result['decimalLatitude']
            longitude = result['decimalLongitude']
        except:
            latitude = ''
            longitude = ''
        try:
            date = '{}/{}/{}'.format(result['day'], result['month'], result['year'])

        except:
            date = ''

        return scientificName.decode('utf-8'), municipality.decode('utf-8'), state.decode('utf-8'), country.decode('utf-8'), latitude, longitude, date
    return None

def getAllLocations(inputFile=os.path.join('data','ListaMacrofitasResult.csv')):
    writeOutput(os.path.join('data','gbifLocations.csv'), '', True)
    writeOutput(os.path.join('data','gbifLocationsNotFound.csv'), '', True)
    inputContent = open(inputFile, 'r')
    lines = inputContent.readlines()
    for plant in lines:
        getLocation(plant)

def writeOutput(path ,line, clearFlag=False):

    if clearFlag:
        outputLocation = open(path, 'w')
        return

    try:
        outputLocation = open(path, 'a')
    except:
        outputLocation = open(path, 'w')

    outputLocation.write(line + "\n")

#if __name__ == '__main__':
#    input = open(os.path.join('data','result.csv'), 'r')
#    errors = open(os.path.join('data','errors.csv'), 'a')
#    lines = input.readlines()
#
#    for line in lines:
#        try:
#            if line.split(',')[1] == 'ok':
#                getLocation(line.split(',')[0].replace('\n',''), os.path.join("data','gbifLocations.csv"))
#            else:
#                getLocation(line.split(',')[0].replace('\n',''), os.path.join("data','gbifLocations.csv"))
#        except:
#            errors.write(line)