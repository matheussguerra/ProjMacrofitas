import requests

def floraDoBrasil():
    urlRequestTemplate = "http://servicos.jbrj.gov.br/flora/taxon/{}"
    with open("../data/ListaMacrofitasResult.csv") as file:
        lines = file.readlines()

        for line in lines:
            line = urlRequestTemplate.format(line).replace(' ', '%20')
            r = requests.get(line.strip())
            print r.json()



def main():
    floraDoBrasil()

if __name__ == '__main__':
    main()