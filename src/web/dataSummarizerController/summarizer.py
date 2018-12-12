#coding: utf-8
import os
from flask import Blueprint, render_template
import pandas
from scrapping.floraDoBrasil import getFullInformation


summarizer_blueprint = Blueprint('summarizer', __name__)

# Tabela 1
@summarizer_blueprint.route('/comparacao/', methods=['GET'])
def comparacao():
    content = getContent(os.path.join('web','data','Tabela1.csv'))
    return render_template('data/firstTable.html', data=content)

@summarizer_blueprint.route('/sinonimos/', methods=['GET'])
def sinonimos():
    content = getContent(os.path.join('web','data','Tabela2.csv'))
    plants = getContent(os.path.join('web','data','Tabela1.csv'))
    formaVida_arr, substrato_arr, origem_arr, endemismo_arr, distribuicao_arr = [], [],[], [], []
    for plant in plants:
        formaVida, substrato, origem, endemismo, distribuicao = getFullInformation(plant[0])
        formaVida_arr.append(formaVida)
        substrato_arr.append(substrato)
        origem_arr.append(origem)
        endemismo_arr.append(endemismo)
        distribuicao_arr.append(distribuicao)
    return render_template('data/secondTable.html', data=content, formaVida=formaVida_arr, substrato=substrato_arr, origem=origem_arr, endemismo=endemismo_arr, distribuicao=distribuicao_arr)

@summarizer_blueprint.route('/localizacao/', methods=['GET'])
def localizacao():
    content = getContent(os.path.join('web','data','Tabela3.csv'))

    return render_template('data/thirdTable.html', data=content)

def getContent(filePath):
    data = open(filePath, 'r')

    dataLines = data.readlines()
    content = []

    for line in dataLines[1:]:
        dataContent = line.split(',')
        dataContentProcessed = [element.rstrip().decode('utf-8') for element in dataContent]
        content.append(dataContentProcessed)

    return content