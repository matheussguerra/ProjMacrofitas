#coding: utf-8
from flask import request, render_template
from web import app
from web.forms.searchForm import SearchForm

@app.route('/busca', methods=['GET', 'POST'])
# Implementar função de buscar plantas
def busca():
    form = SearchForm(request.form)

    if (request.method == 'POST' and form.validate()):
        return render_template('search/searchPlant.html', form=form)
    return render_template('search/searchPlant.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)