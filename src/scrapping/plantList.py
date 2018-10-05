from BeautifulSoup import BeautifulSoup
import requests

def plantList():
    response = requests.get('http://www.theplantlist.org/tpl1.1/search?q=Eclipta megapotamica')

    if response.ok:
        raw_http = response.text
        soup = BeautifulSoup(raw_http)

        isAccepted = verifyAccepted(soup)
        synonymous = getSynonymous(soup)
        
        return isAccepted, synonymous
    else:
        return 'Bad Response!'

def verifyAccepted(soup):
    header_text = soup('p')[0]
    return True if 'accepted' in header_text.text else False

def getSynonymous(soup):
    table = soup('table')
    trs = table[0]('tr')
    synonymous = []
    for tr in trs[1:]:
        data = {
            'genus' : str(tr('td')[0]('span')[0]('i')[0].text),
            'species' : str(tr('td')[0]('span')[0]('i')[1].text),
            'authorship' : str(tr('td')[0]('span')[1].text),
            'status' : str(tr('td')[1].text),
            'source' : str(tr('td')[3].text),
            'date_supplied' : str(tr('td')[4].text)
        }
        synonymous.append(data)
    return data

def main():
    plantList()

if __name__ == '__main__':
    main()