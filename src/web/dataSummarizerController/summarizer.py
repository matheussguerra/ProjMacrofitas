#coding: utf-8

from flask import Blueprint, render_template
import pandas
summarizer_blueprint = Blueprint('summarizer', __name__)

# Tabela 1
@summarizer_blueprint.route('/comparacao/', methods=['GET'])
def comparacao():
    data = open('web/data/Tabela1.csv', 'r',)

    dataLines = data.readlines()
    content = []

    for line in dataLines[1:]:
        dataContent = line.split(',')
        dataContentProcessed = [element.rstrip().decode('utf-8') for element in dataContent]
        content.append(dataContentProcessed)
    return render_template('data/firstTable.html', data=content)
