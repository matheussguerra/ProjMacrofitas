from BeautifulSoup import BeautifulSoup
import requests

def getData(searchTerm):
    response = requests.get('http://www.theplantlist.org/tpl1.1/search?q=' + searchTerm)
    raw_http = response.text

    if response.ok:
        raw_http = response.text
        soup = BeautifulSoup(raw_http)

        isAccepted = verifyAccepted(soup)
        synonymous = getSynonymous(soup)
        
        #print isAccepted, synonymous
        return isAccepted, synonymous
    else:
        return 'Bad Response!'

def verifyAccepted(soup):
    header_text = soup('p')[0]
    return True if 'accepted' in header_text.text else False

def getSynonymous(soup):
    title = str(soup('title')[0])
    
    if(title[7:17] == "No results"):
        return False

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
    return synonymous