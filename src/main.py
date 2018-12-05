#coding: utf-8
from flask import request, render_template
from web import app
from web.forms.searchForm import SearchForm
from scrapping.floraDoBrasil import getOneEntry
from scrapping.plantList import getOneEntry as getOneEntryPlantList
from location.gbif import getLocation

@app.route('/busca', methods=['GET', 'POST'])
# Implementar função de buscar plantas
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

if __name__ == "__main__":
    app.run(debug=True)