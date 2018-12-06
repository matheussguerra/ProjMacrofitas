#coding: utf-8
import os
from flask import Blueprint, render_template
import pandas
summarizer_blueprint = Blueprint('summarizer', __name__)

# Tabela 1
@summarizer_blueprint.route('/comparacao/', methods=['GET'])
def comparacao():
    content = getContent(os.path.join('web','data','Tabela1.csv'))
    return render_template(os.path.join('data','firstTable.html'), data=content)

@summarizer_blueprint.route('/localizacao/', methods=['GET'])
def localizacao():
    content = getContent(os.path.join('web','data','Tabela4.csv'))
    return render_template(os.path.join('data','thirdTable.html'), data=content)


def getContent(filePath):
    data = open(filePath, 'r',)

    dataLines = data.readlines()
    content = []

    for line in dataLines[1:]:
        dataContent = line.split(',')
        dataContentProcessed = [element.rstrip().decode('utf-8') for element in dataContent]
        content.append(dataContentProcessed)

    return content