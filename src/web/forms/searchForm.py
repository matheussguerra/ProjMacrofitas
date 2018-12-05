from wtforms import Form, IntegerField, StringField, TextAreaField, SelectField, validators

class SearchForm(Form):
    plant = StringField('Nome:', render_kw={'autofocus': True})