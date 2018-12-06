import requests

def getLocation(sciName, outputPath, writeOutputFlag=True):
    urlTemplate = 'http://api.gbif.org/v1/occurrence/search?scientificName={}'

    response = requests.get(urlTemplate.format(sciName))
    response_json = response.json()["results"]
    resultsParsed = []

    for result in response_json:

        scientificName, municipality, state, country, latitude, longitude, date = parseResult(result, sciName)
        oneResult = [scientificName, municipality, state, country, latitude, longitude, date]
        resultsParsed.append(oneResult)

        if writeOutputFlag:
            writeOutput(outputPath, '{},{},{},{},{},{},{}'.format(scientificName, municipality, state, country, latitude, longitude, date))

    return resultsParsed

def parseResult(result, sciName):
    name_splited = result['scientificName'].encode('utf8').split()
    scientificName = "{} {}".format(name_splited[0], name_splited[1])

    municipality, state, country, latitude, longitude, date = "", "", "", "", "", ""

    if scientificName.lower() == sciName.lower():
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


def writeOutput(path ,line):
    try:
        outputLocation = open(path, 'a')
    except:
        outputLocation = open(path, 'w')

    outputLocation.write(line + "\n")

if __name__ == '__main__':
    input = open('../data/result.csv', 'r')
    errors = open('../data/errors.csv', 'a')
    lines = input.readlines()

    for line in lines:
        try:
            if line.split(',')[1] == 'ok':
                getLocation(line.split(',')[0].replace('\n',''), "../data/gbifLocations.csv")
            else:
                getLocation(line.split(',')[0].replace('\n',''), "../data/gbifLocations.csv")
        except:
            errors.write(line)