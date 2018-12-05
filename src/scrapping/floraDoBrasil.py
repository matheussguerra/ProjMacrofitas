# coding: utf-8

"""
- Script para obtenção de dados de plantas da base Flora do Brasil
- Formato: {Nome que foi pesquisado},{Status: NOME_ACEITO/SINÔNIMO},{Nome aceito -> caso a planta pesquisada seja sinônimo}
"""

# Bibliotecas utilizadas
import requests
import json
import csv

# Método principal. Obtenção de informações de todas as plantas de um arquivo de entrada
# Obtenção de informações de uma planta específica
def getData(searchTerm='', allDataset=False, inputFile='../data/ListaMacrofitasResult.csv', outputPath='../data/floraDoBrasil.csv', notFoundPath='../data/notFoundFDB.csv'):
	# URL Modelo para pesquisas de plantas
	urlRequestTemplate = "http://servicos.jbrj.gov.br/flora/taxon/{}"

	# Caso a flag seja verdadeira, a busca de informações é feita para todas as plantas da base de dados
	if allDataset:
		getManyEntries(urlRequestTemplate, inputFile, outputPath, notFoundPath)
	# Obtenção de informações da planta especificada
	else:
		getOneEntry(searchTerm, outputPath, notFoundPath)

def getOneEntry( searchTerm, outputPath, notFoundPath):
	urlRequestTemplate="http://servicos.jbrj.gov.br/flora/taxon/{}"
	if(searchTerm == ''):
		# Caso o nome da planta (searchTerm) não for especificado, retorna uma exceção
		raise BaseException
	# Formata a URL Modelo para buscar informações da planta desejada
	urlRequest = urlRequestTemplate.format(searchTerm)
	# Obtém a resposta da requisição HTML
	response = requests.get(urlRequest.strip())

	try:
		# Obtém os dados através da resposta da requisição HTML
		unicode_queryResult = response.json()[u'result']
	except:
		# Caso não houver resposta, é registrado em um arquivo
		parseAndWriteJSON(searchTerm, notFoundPath, isNone=True, writeOutput=False)
		return 0
	# Obtém o resultado convertido em JSON
	queryResult = json.dumps(unicode_queryResult,indent=4, ensure_ascii=False)
	# Método para retirar informações do JSON e registrá-las
	return parseAndWriteJSON(queryResult, outputPath, writeOutput=False)

def getManyEntries(urlRequestTemplate, inputFile, outputPath, notFoundPath):
	results = []
	# Arquivo de entrada é aberto para leitura
	with open(inputFile) as inputFile:
		# Linhas do arquivo são lidas
		lines = inputFile.readlines()
		# Itera sobre todas as linhas do arquivo
		for line in lines:
			# Formata a URL para pesquisar sobre determinada planta
			urlRequest = urlRequestTemplate.format(line)
			# Obtém a resposta da requisição HTML
			response = requests.get(urlRequest.strip())
			# Obtém o JSON da resposta da requisição HTML
			unicode_queryResult = response.json()[u'result']
			# Caso não haja resultado para a pesquisa
			if(unicode_queryResult == None):
				# É registrado em um arquivo
				parseAndWriteJSON(line, notFoundPath, isNone=True)
				continue
			# Resultado é transformado em JSON
			queryResult = json.dumps(unicode_queryResult,indent=4, ensure_ascii=False)
			# Método é chamado para extração de informações do JSON e é registrado
			parseAndWriteJSON(queryResult, outputPath)

def parseAndWriteJSON(json_data, outputPath, isNone=False, writeOutput=True):
	# Abre o arquivo de saída para registro de informações
	if writeOutput:
		outputFile = open(outputPath,'a')
		output = csv.writer(outputFile)

	if isNone:
		# Caso a planta não foi encontrada, é registrado como : "{Nome científico}, Not Found"
		output.writerow((json_data.split()[0] + " " + json_data.split()[1], 'Not Found'))
		return 0

	# Obtém o os dados do JSON
	json_data = json.loads(json_data)[0]
	# Obtém o status da planta pesquisada -> {NOME_ACEITO , SINÔNIMO}
	status = json_data["taxonomicstatus"]
	# Inicializa variáveis
	name, accepted_name = '', ''

	# Caso a planta pesquisada seja um sinônimo:
	if status == 'SINONIMO':
		try:
			# Nome pesquisado é obtido
			name = json_data["scientificname"].split()[0] + ' ' + json_data["scientificname"].split()[1]
		except:
			# Caso o nome não esteja especificado
			family = 'Not Specified'
			name = 'Not Specified'
		try:
			# Obtém o nome aceito para a planta pesquisada
			accepted_name = json_data["NOME ACEITO"][0]["scientificname"].split()[0] + ' ' + json_data["NOME ACEITO"][0]["scientificname"].split()[1]
		except:
			# Caso não haja o campo "NOME ACEITO" no JSON, o nome aceito é definido como "Not Specified"
			accepted_name = "Not Specified"
			pass

	else:
		# Caso a planta seja aceita, é obtido apenas o nome e o status
		name = json_data["scientificname"].split()[0] + ' ' + json_data["scientificname"].split()[1]

	# Dados são registrados
	if writeOutput:
		output.writerow((name, status, accepted_name))
	return name, status, accepted_name

def main():
	getData(allDataset=True)

if __name__ == '__main__':
	main()