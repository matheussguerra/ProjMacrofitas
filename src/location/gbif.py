import requests

def getLocation(sciName, outputPath):
    urlTemplate = 'http://api.gbif.org/v1/occurrence/search?scientificName={}'

    response = requests.get(urlTemplate.format(sciName))
    response_json = response.json()["results"]

    for result in response_json:

        scientificName, municipality, state, country, latitude, longitude, date = parseResult(result, sciName)

        writeOutput(outputPath, '{},{},{},{},{},{},{}'.format(scientificName, municipality, state, country, latitude, longitude, date))

def parseResult(result, sciName):
    name_splited = result['scientificName'].encode('utf8').split()
    scientificName = "{} {}".format(name_splited[0], name_splited[1])
    municipality, state, country, latitude, longitude, date = "", "", "", "", "", ""
    if scientificName == sciName:
        try:
            municipality =  result['municipality'].encode('utf8')
        except:
            municipality = ''
        try:
            state = result['stateProvince'].encode('utf8')
        except:
            state = ''

        try:
            country = result['country'].encode('utf8')
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

    return scientificName, municipality, state, country, latitude, longitude, date


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
            print line.split(',')[0].replace('\n','')
        except:
            errors.write(line)