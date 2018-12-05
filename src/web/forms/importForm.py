from wtforms import Form, FileField

class ImportForm(Form):
    arquivo = FileField('Arquivo')