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
import os

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

def readAllFiles(inputPath=os.path.join("data","ListaMacrofitasResult.csv"),floraDoBrasilPath=os.path.join("data","floraDoBrasil.csv"), plantListPath=os.path.join("data","plantList.csv"), speciesLinkPath=os.path.join("data","speciesLink.csv"), gbifPath=os.path.join("data","gbifLocations.csv")):
    # Inicializa variáveis
    floraDoBrasilContent, plantListContent, speciesLinkContent, gbifContent = None, None, None, None

    inputContent = getFilesContent(inputPath)
    floraDoBrasilContent = getFilesContent(floraDoBrasilPath)
    plantListContent = getFilesContent(plantListPath)
    floraDoBrasilSynonimousContent = getFilesContent(floraDoBrasilPath[:-4] + 'Sinonimos.csv')

    generateFirstTable(inputContent, floraDoBrasilContent, plantListContent, os.path.join('web','data','Tabela1.csv'))

    generateSecondTable(floraDoBrasilSynonimousContent, os.path.join('web','data','Tabela2.csv'))
    speciesLinkContent = getFilesContent(speciesLinkPath)

    gbifContent = getFilesContent(gbifPath)
    speciesLinkContent = getFilesContent(speciesLinkPath)

    generateThirdTable( gbifContent, speciesLinkContent, os.path.join('web','data','Tabela3.csv'))


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
                elif statusPlantList == 'SINONIMO':
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


def generateSecondTable(floraDoBrasilSynonimousContent, secondTableOutputPath):
    writeOutput(secondTableOutputPath, 'w', ['Nome Aceito', 'Sinônimo'])
    for line in floraDoBrasilSynonimousContent:
        writeOutput(secondTableOutputPath, 'a', line.split(','))

def generateThirdTable(gbifContent, speciesLinkContent, fourthTableOutputPath):
    writeOutput(fourthTableOutputPath, 'w', ['Nome aceito', 'Cidade', 'Estado', 'País', 'Latitude', 'Longitude'])

    for line in gbifContent:
        fields = line.split(',')
        lineToWrite = fields
        writeOutput(fourthTableOutputPath, 'a', lineToWrite)

    for lineSpeciesLink in speciesLinkContent:
        fields = lineSpeciesLink.split(',')
        lineToWrite = fields
        writeOutput(fourthTableOutputPath, 'a', lineToWrite)

def writeOutput(filePath, mode, content):
    with open(filePath, mode) as output:
        csvWriter = csv.writer(output)
        csvWriter.writerow(content)
