import requests

def getLocation(sciName):
    urlTemplate = 'http://api.gbif.org/v1/occurrence/search?scientificName={}'

    response = requests.get(urlTemplate.format(sciName))
    response_json = response.json()["results"]

    for result in response_json:
        name_splited = result['scientificName'].encode('utf8').split()
        scientificName = "{} {}".format(name_splited[0], name_splited[1])
        if scientificName == sciName:

            try:
                locality =  result['locality'].encode('utf8')
            except:
                locality = ''
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
        writeOutput('{},{},{},{},{},{},{},{}'.format(scientificName, locality, municipality, state, country, latitude, longitude, date))


def writeOutput(line):
    try:
        outputLocation = open('../data/gbifLocations.csv', 'a')
    except:
        outputLocation = open('../data/gbifLocations.csv', 'w')

    outputLocation.write(line + "\n")
