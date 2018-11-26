# coding: utf-8
"""
Geração de tabelas de saída para sumarização dos dados

1ª Tabela:
Campos (Colunas):
Nome aceito, Sinônimo
(Pode haver repetição)

2ª Tabela:
Campos (Colunas):
Nome aceito, sinônimos 1, sinônimo 2, sinônimo 3, ..., sinônimo n

3ª Tabela (?):
Campos (Colunas):
Todos os campos do site FloraDoBrasil.
Tomar como base: http://reflora.jbrj.gov.br/reflora/listaBrasil/FichaPublicaTaxonUC/FichaPublicaTaxonUC.do?id=FB15339

4ª Tabela:
Campos (Colunas):
Nome aceito, cidade, estado, país, latitude, longitude
"""
import csv

def getFilesContent(path):
    # Retorna o conteúdo do arquivo
    #try:
    # Abre o arquivo como leitura
    with open(path, 'r') as dataFile:
        # Armazena as linhas na variável content
        content = dataFile.readlines()
        # Retorna o conteúdo sem \r e \n
        return [line.rstrip() for line in content]
    #except:
    #    # Caso não encontre o arquivo, retorna exceção
    #    raise Exception('Arquivo não encontrado: {}'.format(path))
    #    return None

def readAllFiles(inputPath="../data/ListaMacrofitasResult.csv",floraDoBrasilPath="../data/floraDoBrasil.csv", plantListPath="../data/plantList.csv", speciesLinkPath="../data/speciesLink.csv", gbifPath="../data/gbifLocations.csv"):
    # Inicializa variáveis
    floraDoBrasilContent, plantListContent, speciesLinkContent, gbifContent = None, None, None, None
    inputContent = getFilesContent(inputPath)
    floraDoBrasilContent = getFilesContent(floraDoBrasilPath)
    plantListContent = getFilesContent(plantListPath)

    generateFirstTable(inputContent, floraDoBrasilContent, plantListContent, '../../output/Tabela1.csv')

    generateSecondTable(floraDoBrasilContent, plantListContent, '../../output/Tabela2.csv')
    speciesLinkContent = getFilesContent(speciesLinkPath)
    secondTableContent = getFilesContent('../../output/Tabela2.csv')
    gbifContent = getFilesContent(gbifPath)
    speciesLinkContent = getFilesContent(speciesLinkPath)
    generateFourthTable(secondTableContent, gbifContent, speciesLinkContent, '../../output/Tabela4.csv')


def generateFirstTable(inputContent, floraDoBrasilContent, plantListContent, firstTableOutputPath):
    # Adiciona o cabeçalho do csv no arquivo de saída
    writeOutput(firstTableOutputPath, 'w', ['Nome','Status Flora do Brasil', 'Nome Aceito Flora do Brasil', 'Status PlantList', 'Nome Aceito PlantList', 'Plant List x Flora do Brasil'])

    for entrada in inputContent:
        lineToWrite = []
        for floraDoBrasilEntrada in floraDoBrasilContent:
            if entrada in floraDoBrasilEntrada.split(',')[0]:
                statusFloraDoBrasil = floraDoBrasilEntrada.split(',')[1]
                if statusFloraDoBrasil == 'NOME_ACEITO':
                    statusFloraDoBrasil = "Nome Aceito"
                    nomeFloraDoBrasil = floraDoBrasilEntrada.split(',')[0]
                else:
                    nomeFloraDoBrasil = floraDoBrasilEntrada.split(',')[2]
                    statusFloraDoBrasil = "Sinônimo"
                lineToWrite = [entrada, statusFloraDoBrasil, nomeFloraDoBrasil]

        if len(lineToWrite) == 0:
            lineToWrite = [entrada, 'Não Encontrado', 'Não Encontrado']

        for plantListEntrada in plantListContent:
            if entrada in plantListEntrada.split(',')[0]:
                statusPlantList = plantListEntrada.split(',')[1]
                if statusPlantList == 'NOME_ACEITO':
                    statusPlantList = "Nome Aceito"
                    nomePlantList = plantListEntrada.split(',')[0]
                else:
                    statusPlantList = "Sinônimo"
                    nomePlantList = plantListEntrada.split(',')[2]

                lineToWrite.append(statusPlantList)
                lineToWrite.append(nomePlantList)

                break


        if len(lineToWrite) == 3:
            lineToWrite.append('Não Encontrado')
            lineToWrite.append('Não Encontrado')

        if not (lineToWrite[2] == lineToWrite[4]) and lineToWrite[2] != 'Não Encontrado':
            comparacao = 'Diferente'
            lineToWrite.append(comparacao)

        writeOutput(firstTableOutputPath, 'a', lineToWrite)



def generateSecondTable(floraDoBrasilContent, plantListContent, secondTableOutputPath):
    writeOutput(secondTableOutputPath, 'w', ['Nome Aceito', 'Sinônimo'])
    # Dicliptera ciliaris
    # plantDict: planta -> sinonimos
    plantDict = dict()

    for plantLine in floraDoBrasilContent:
        lineSplitted = plantLine.split(',')
        status = lineSplitted[1]

        if status == "SINONIMO":
            nomeAceito = lineSplitted[2]
            sinonimo = lineSplitted[0]
            try:
                plantDict[nomeAceito].append(sinonimo)
            except:
                plantDict[nomeAceito] = []
                plantDict[nomeAceito].append(sinonimo)

        elif status == "NOME_ACEITO":
            nomeAceito = lineSplitted[0]
            sinonimo = None

            if not plantDict.has_key(nomeAceito):
                plantDict[nomeAceito] = []

    for key in plantDict.keys():
        lineToWrite = [key]
        lineToWrite = lineToWrite + plantDict[key]
        writeOutput(secondTableOutputPath, 'a', lineToWrite)


def generateThirdTable():
    raise NotImplementedError

def generateFourthTable(secondTableContent, gbifContent, speciesLinkContent, fourthTableOutputPath):
    writeOutput(fourthTableOutputPath, 'w', ['Nome aceito', 'Cidade', 'Estado', 'País', 'Latitude', 'Longitude'])
    for plant in secondTableContent:
        try:
            accepted_name = plant.split(',')[0]
        except:
            accepted_name = plant

        for line in gbifContent:
            if accepted_name in line:
                fields = line.split(',')
                city = fields[1]
                state = fields[2]
                country = fields[3]
                latitude = fields[4]
                longitude = fields[5]
                lineToWrite = [accepted_name, city, state, country, latitude, longitude]
                writeOutput(fourthTableOutputPath, 'a', lineToWrite)

        for lineSpeciesLink in speciesLinkContent:
            if accepted_name in lineSpeciesLink:
                fields = lineSpeciesLink.split(',')
                city = fields[2]
                state = fields[3]
                country = fields[4]
                latitude = fields[5]
                longitude = fields[6]
                lineToWrite = [accepted_name, city, state, country, latitude, longitude]
                writeOutput(fourthTableOutputPath, 'a', lineToWrite)

def writeOutput(filePath, mode, content):
    with open(filePath, mode) as output:
        csvWriter = csv.writer(output)
        csvWriter.writerow(content)

if __name__ == "__main__":
    readAllFiles()