from wtforms import Form, StringField

class SearchForm(Form):
    plant = StringField('Nome:', render_kw={'autofocus': True})