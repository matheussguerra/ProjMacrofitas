#coding: utf-8
from flask import request, render_template
from web import app
from web.forms.searchForm import SearchForm
from scrapping.floraDoBrasil import getOneEntry
from scrapping.floraDoBrasil import getData as getDataFloraDoBrasil
from scrapping.plantList import getAllEntries as getDataSpeciesLink
from scrapping.plantList import getOneEntry as getOneEntryPlantList
from location.gbif import getLocation
from web.forms.importForm import ImportForm
from preprocessing.core import main as preProcess

# Route para buscar informações de uma única planta
@app.route('/busca', methods=['GET', 'POST'])
def busca():
    form = SearchForm(request.form)

    if (request.method == 'POST' and form.validate()):
        planta = request.form['plant']
        nome_flora, status_flora, nome_aceito_flora = getOneEntry(searchTerm=planta, outputPath='', notFoundPath='')
        if nome_aceito_flora == '':
            nome_aceito_flora = nome_flora

        dataComparation = [nome_flora, status_flora, nome_aceito_flora]
        locations_gbif = getLocation(planta, '', False)

        return render_template('data/searchResult.html', plant_searched=planta,form=form, dataComparation=dataComparation, dataLocation=locations_gbif)
    return render_template('search/searchPlant.html', form=form)

# Route para buscar informações de todas as plantas de um arquivo
@app.route('/inserirDados', methods=['GET','POST'])
def importar():
    form = ImportForm(request.form)
    if (request.method == 'POST' and form.validate()):
        filename = request.files['arquivo'].filename
        print filename
        extensao = filename.split('.')[1]
        request.files['arquivo'].save('data/ListaMacrofitas.{}'.format(extensao))
        preProcess()
        # Implementar threads para melhorar performance
        getDataFloraDoBrasil(allDataset=True)
        getDataSpeciesLink()
        # Script do flora do Brasil pra tabela 2 aqui
        # Scripts de localizacao aqui
        # Script de sumarizacao aqui


        return render_template('index.html')



    return render_template('import/importFile.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)